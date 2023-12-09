import numpy as np

from materials.material import Material
from materials.datasets import CarbonT300_Epoxy5208

from matplotlib import pyplot as plt


class Laminate():
    ID = 0
    def __init__(self, material:Material, off_axis_angle:float=0.0, thickness=0.125) -> None:
        self.id = Laminate.ID + 1
        Laminate.ID += 1
        self.material:Material = material
        self.off_axis_angle = float(off_axis_angle)

        self.thickness = thickness
        m, n = np.cos(np.deg2rad(self.off_axis_angle)), np.sin(np.deg2rad(self.off_axis_angle))
        #m = 0.0 if m < 6.2e-17 else m
        #n = 0.0 if n < 6.2e-17 else n
        self.transpose_stress = np.array([
            [np.power(m,2), np.power(n,2), 2.0*m*n],
            [np.power(n,2), np.power(m,2), -2.0*m*n],
            [m*n*(-1), m*n, np.power(m,2)-np.power(n,2)]
        ])
        self.transpose_strain = np.array([
            [np.power(m,2), np.power(n,2), m*n],
            [np.power(n,2), np.power(m,2), -1.0*m*n],
            [-2.0*m*n, 2*m*n, np.power(m,2)-np.power(n,2)]
        ])
        self.Q = np.linalg.inv(self.transpose_stress).dot(self.material.C_on).dot(self.transpose_strain)
        self.S = np.linalg.inv(self.Q)

        self.Tcq = np.array([
            [m**4, n**4, 2*m**2*n**2, 4*m**2*n**2],
            [n**4, m**4, 2*n**2*m**2, 4*n**2*m**2],
            [m**2*n**2, m**2*n**2, n**4*m**4, -4*m**2*n**2],
            [m**2*n**2, m**2*n**2, -2*m**2*n**2, (m**2-n**2)**2],
            [m**3*n, -m*n**3, -m**3*n+m*n**3, 2*(m*n**3-m**3*n)],
            [m*n**3, -m**3*n, m**3*n-m*n**3, 2*(m**3*n-m*n**3)]
        ])

    def stress2strain(self, stress:np.array, S=None):
        """
        calculate strain from stress
        stain3*1 = [S]3*3[stress]3*1
        """
        if S is None:
            S = self.S
        strain = S.dot(stress)
        return strain
    
    def strain2stress(self, strain:np.array, Q=None):
        """
        calculate strain from stress
        stain3*1 = [S]3*3[stress]3*1
        """
        if Q is None:
            Q = self.Q
        stress = Q.dot(strain)
        return stress

    def MAF_Q(self):
        X = np.array([1.0, self.U2, self.U3])
        cos2t = np.cos(np.deg2rad(2.0*self.off_axis_angle))
        cos4t = np.cos(np.deg2rad(4.0*self.off_axis_angle))
        sin2t = np.sin(np.deg2rad(2.0*self.off_axis_angle))
        sin4t = np.sin(np.deg2rad(4.0*self.off_axis_angle))
        Y = np.array([
            [self.U1, cos2t, cos4t],
            [self.U1, -cos2t, cos4t],
            [self.U4, 0.0, -cos4t],
            [self.U5, 0.0, -cos4t],
            [0.0, sin2t/2.0, sin4t],
            [0.0, sin2t/2.0, -sin4t]
        ])
        return Y.dot(X)

    
    @property
    def U1(self):
        return 1.0/8.0*(3.0*self.material.C_on[0,0] + 3.0*self.material.C_on[1,1] + 2.0*self.material.C_on[0,1] + 4.0*self.material.C_on[2,2])
    @property
    def U2(self):
        return 1.0/2.0*(self.material.C_on[0,0] - self.material.C_on[1,1] )
    @property
    def U3(self):
        return 1.0/8.0*(self.material.C_on[0,0] + self.material.C_on[1,1] - 2.0*self.material.C_on[0,1] - 4.0*self.material.C_on[2,2])
    @property
    def U4(self):
        return 1.0/8.0*(self.material.C_on[0,0] + self.material.C_on[1,1] + 6.0*self.material.C_on[0,1] - 4.0*self.material.C_on[2,2])
    @property
    def U5(self):
        return 1.0/8.0*(self.material.C_on[0,0] + self.material.C_on[1,1] - 2.0*self.material.C_on[0,1] + 4.0*self.material.C_on[2,2])

    @property
    def E1(self):
        return 1/self.S[0,0]
    
    @property
    def E2(self):
        return 1/self.S[1,1]
    
    @property
    def E6(self):
        return 1/self.S[2,2]
    
    @property
    def V21(self):
        return -self.S[1,0]/self.S[0,0]
    
    @property
    def V61(self):
        return self.S[2,0]/self.S[0,0]
    
    @property
    def V62(self):
        return self.S[2,1]/self.S[1,1]
    
    @property
    def V12(self):
        return -self.S[0,1]/self.S[1,1]
    
    @property
    def V16(self):
        return self.S[0,2]/self.S[2,2]
    
    @property
    def V26(self):
        return self.S[2,1]/self.S[1,1]


class Composite():
    def __init__(self, laminates) -> None:
        self.laminates:list[Laminate] = laminates
        self.Z_laminates = self.calc_Z_laminates()
        self.A = self.calc_A()
        self.D = self.calc_D()
        self.stiffness_compliance_general = self.calc_stiffness_compliance_general()

    def calc_Z_laminates(self):
        Z_laminates = {}
        z1 = -1.0*self.composite_thikness/2.0
        for laminate in self.laminates[::-1]:
            z2 = z1 + laminate.thickness
            Z_laminates[laminate] = (z1, z2)
            z1 = z2
        return Z_laminates

    def calc_A(self):
        self.A = np.zeros((3,3))
        for laminate in self.laminates:
            for i in range(3):
                for j in range(3):
                    self.A[i,j] += laminate.Q[i,j]*laminate.thickness
        self.a = np.linalg.inv(self.A)
        return self.A
    
    def calc_B(self):
        """
        unit d : (KN.m)^-1
        unit D : (TPa)^-1
        """
        self.D = np.zeros((3,3))
        for laminate in self.laminates[::-1]:
            z1, z2 = self.Z_laminates[laminate]
            for i in range(3):
                for j in range(3):
                    self.D[i,j] += laminate.Q[i,j]*(np.power(z2, 2.0) - np.power(z1, 2.0)) / 2.0
            #z1 = z2 
        self.d = np.linalg.inv(self.D) 
        return self.D

    def calc_D(self):
        """
        unit d : (KN.m)^-1
        unit D : (TPa)^-1
        """
        self.D = np.zeros((3,3))
        for laminate in self.laminates[::-1]:
            z1, z2 = self.Z_laminates[laminate]
            for i in range(3):
                for j in range(3):
                    self.D[i,j] += laminate.Q[i,j]*(np.power(z2, 3.0) - np.power(z1, 3.0)) / 3.0
            #z1 = z2 
        self.d = np.linalg.inv(self.D) 
        return self.D
    
    def calc_stiffness_compliance_general(self):
        return np.concatenate((np.concatenate((self.A, self.B), axis=1),np.concatenate((self.A, self.B), axis=1)), axis=0)

    def moment_apply(self, M:np.array):
        K = self.d.dot(M)
        properties = {
            "K":K,
            "stress":{},
            "strain":{}
        }
        for laminate in self.laminates:
            z1, z2 = self.Z_laminates[laminate]
            max_z = max([abs(z1), abs(z2)])
            strain = K*max_z
            properties["strain"][laminate] = strain
            properties["stress"][laminate] = laminate.strain2stress(strain)
        return properties

    def stress2strain(self, stress:np.array, a=None):
        """
        calculate strain from stress
        stain3*1 = [S]3*3[stress]3*1
        """
        if a is None:
            a = self.a
        strain = a.dot(stress)
        return strain

    @property
    def composite_thikness(self):
        return sum([laminate.thickness for laminate in self.laminates])


    @property
    def E_1(self):
        return

    @property
    def V_12(self):
        return -np.linalg.inv(composite.A)[0,1]/np.linalg.inv(composite.A)[1,1]
    
    @property
    def V_21(self):
        return np.linalg.inv(composite.A)[1,0]/np.linalg.inv(composite.A)[0,0]
    
    @property
    def V_61(self):
        return np.linalg.inv(composite.A)[0,2]/np.linalg.inv(composite.A)[2,2]
    
    @property
    def V_26(self):
        return np.linalg.inv(composite.A)[1,2]/np.linalg.inv(composite.A)[2,2]
    
    @property
    def V_26(self):
        return np.linalg.inv(composite.A)[2,1]/np.linalg.inv(composite.A)[1,1]
    
    
    





if __name__ == "__main__":
    laminates = [
        Laminate(material=CarbonT300_Epoxy5208, off_axis_angle=0.0),
        Laminate(material=CarbonT300_Epoxy5208, off_axis_angle=0.0),
        Laminate(material=CarbonT300_Epoxy5208, off_axis_angle=0.0),
        Laminate(material=CarbonT300_Epoxy5208, off_axis_angle=0.0),
        Laminate(material=CarbonT300_Epoxy5208, off_axis_angle=90.0),
        Laminate(material=CarbonT300_Epoxy5208, off_axis_angle=90.0),
        Laminate(material=CarbonT300_Epoxy5208, off_axis_angle=90.0),
        Laminate(material=CarbonT300_Epoxy5208, off_axis_angle=90.0),
        Laminate(material=CarbonT300_Epoxy5208, off_axis_angle=90.0),
        Laminate(material=CarbonT300_Epoxy5208, off_axis_angle=90.0),
        Laminate(material=CarbonT300_Epoxy5208, off_axis_angle=90.0),
        Laminate(material=CarbonT300_Epoxy5208, off_axis_angle=90.0),
        Laminate(material=CarbonT300_Epoxy5208, off_axis_angle=0.0),
        Laminate(material=CarbonT300_Epoxy5208, off_axis_angle=0.0),
        Laminate(material=CarbonT300_Epoxy5208, off_axis_angle=0.0),
        Laminate(material=CarbonT300_Epoxy5208, off_axis_angle=0.0),
    ]
    composite = Composite(laminates)
    print()


