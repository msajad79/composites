import unittest
import numpy as np
from decimal import Decimal

from composite import Laminate
from materials import datasets, material

class LaminateTest(unittest.TestCase):
    def test_laminate_on_axis_stress2stress_CarbonT300_Epoxy5208(self):
        S = np.array([
            [5.525e-12,  -1.547e-12, 0.0      ],
            [-1.547e-12, 97.09e-12,  0.0      ],
            [0.0,        0.0,        139.5e-12]
        ])
        strain_correct = np.array(
            [2.117e-3, 5.206e-3, 2.092e-3]
        )
        stress = np.array([400e6,60e6,15e6])
        laminate = Laminate(datasets.CarbonT300_Epoxy5208) #dont care material becouse pass S to func
        strain = laminate.stress2strain(stress, S=S)
        self.assertAlmostEqual(strain[0], strain_correct[0], delta=10**Decimal(str(strain_correct[0])).as_tuple().exponent)
        self.assertAlmostEqual(strain[1], strain_correct[1], delta=10**Decimal(str(strain_correct[1])).as_tuple().exponent)
        self.assertAlmostEqual(strain[2], strain_correct[2], delta=10**Decimal(str(strain_correct[2])).as_tuple().exponent)

    def test_laminate_on_axis_stress2stress_GlassScotchply_Epoxy1002(self):
        S = np.array([
            [25.91e-12,   -6.744e-12, 0.0      ],
            [-6.744e-12,  120.9e-12,  0.0      ],
            [0.0,         0.0,        241.5e-12]
        ])
        strain_correct = np.array(
            [9.959e-3, 4.556e-3, 3.623e-3]
        )
        stress = np.array([400e6,60e6,15e6])
        laminate = Laminate(datasets.CarbonT300_Epoxy5208) #dont care material becouse pass S to func
        strain = laminate.stress2strain(stress, S=S)
        self.assertAlmostEqual(strain[0], strain_correct[0], delta=10**Decimal(str(strain_correct[0])).as_tuple().exponent)
        self.assertAlmostEqual(strain[1], strain_correct[1], delta=10**Decimal(str(strain_correct[1])).as_tuple().exponent)
        self.assertAlmostEqual(strain[2], strain_correct[2], delta=10**Decimal(str(strain_correct[2])).as_tuple().exponent)

    ############### Q Matrix on axis and off axis #############
    def test_matrix_Q_0_CarbonT300_Epoxy5208(self):
        Q11, Q22, Q12, Q66, Q16, Q26 = 181.8, 10.3, 2.90, 7.17, 0.0, 0.0
        Q_correct = np.array([
            [Q11*1e9, Q12*1e9, Q16*1e9],
            [Q12*1e9, Q22*1e9, Q26*1e9],
            [Q16*1e9, Q26*1e9, Q66*1e9]
        ])
        laminate = Laminate(datasets.CarbonT300_Epoxy5208,off_axis_angle=0)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(laminate.Q[i,j]/1e9, Q_correct[i,j]/1e9, delta=10**Decimal(str(Q_correct[i,j]/1e9)).as_tuple().exponent)

    def test_matrix_Q_15_CarbonT300_Epoxy5208(self):
        Q11, Q22, Q12, Q66, Q16, Q26 = 160.4,11.9,12.75,17.025,38.50,4.36 #TODO: Book 17.05 (page 78)
        Q_correct = np.array([
            [Q11*1e9, Q12*1e9, Q16*1e9],
            [Q12*1e9, Q22*1e9, Q26*1e9],
            [Q16*1e9, Q26*1e9, Q66*1e9]
        ])
        laminate = Laminate(datasets.CarbonT300_Epoxy5208,off_axis_angle=15)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(laminate.Q[i,j]/1e9, Q_correct[i,j]/1e9, delta=10**Decimal(str(Q_correct[i,j]/1e9)).as_tuple().exponent)

    def test_matrix_Q_30_CarbonT300_Epoxy5208(self):
        Q11, Q22, Q12, Q66, Q16, Q26 = 109.3, 23.6, 32.46, 36.73, 54.19, 20.05 #TODO: Book 36.78 (page78)
        Q_correct = np.array([
            [Q11*1e9, Q12*1e9, Q16*1e9],
            [Q12*1e9, Q22*1e9, Q26*1e9],
            [Q16*1e9, Q26*1e9, Q66*1e9]
        ])
        laminate = Laminate(datasets.CarbonT300_Epoxy5208,off_axis_angle=30)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(laminate.Q[i,j]/1e9, Q_correct[i,j]/1e9, delta=10**Decimal(str(Q_correct[i,j]/1e9)).as_tuple().exponent) 

    def test_matrix_Q_45_CarbonT300_Epoxy5208(self):
        Q11, Q22, Q12, Q66, Q16, Q26 = 56.6, 56.6, 42.32, 46.59, 42.87, 42.87
        Q_correct = np.array([
            [Q11*1e9, Q12*1e9, Q16*1e9],
            [Q12*1e9, Q22*1e9, Q26*1e9],
            [Q16*1e9, Q26*1e9, Q66*1e9]
        ])
        laminate = Laminate(datasets.CarbonT300_Epoxy5208,off_axis_angle=45)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(laminate.Q[i,j]/1e9, Q_correct[i,j]/1e9, delta=10**Decimal(str(Q_correct[i,j]/1e9)).as_tuple().exponent)

    def test_matrix_Q_60_CarbonT300_Epoxy5208(self):
        Q11, Q22, Q12, Q66, Q16, Q26 = 23.6, 109.3, 32.46, 36.73, 20.05, 54.19 #TODO: Book 36.78 (page78)
        Q_correct = np.array([
            [Q11*1e9, Q12*1e9, Q16*1e9],
            [Q12*1e9, Q22*1e9, Q26*1e9],
            [Q16*1e9, Q26*1e9, Q66*1e9]
        ])
        laminate = Laminate(datasets.CarbonT300_Epoxy5208,off_axis_angle=60)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(laminate.Q[i,j]/1e9, Q_correct[i,j]/1e9, delta=10**Decimal(str(Q_correct[i,j]/1e9)).as_tuple().exponent)

    def test_matrix_Q_75_CarbonT300_Epoxy5208(self):
        Q11, Q22, Q12, Q66, Q16, Q26 = 11.9, 160.4, 12.75, 17.025, 4.36, 38.50  #TODO: Book 17.05 (page 78)
        Q_correct = np.array([
            [Q11*1e9, Q12*1e9, Q16*1e9],
            [Q12*1e9, Q22*1e9, Q26*1e9],
            [Q16*1e9, Q26*1e9, Q66*1e9]
        ])
        laminate = Laminate(datasets.CarbonT300_Epoxy5208,off_axis_angle=75)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(laminate.Q[i,j]/1e9, Q_correct[i,j]/1e9, delta=10**Decimal(str(Q_correct[i,j]/1e9)).as_tuple().exponent)

    def test_matrix_Q_90_CarbonT300_Epoxy5208(self):
        Q11, Q22, Q12, Q66, Q16, Q26 = 10.3, 181.8, 2.90, 7.17, 0.0, 0.0
        Q_correct = np.array([
            [Q11*1e9, Q12*1e9, Q16*1e9],
            [Q12*1e9, Q22*1e9, Q26*1e9],
            [Q16*1e9, Q26*1e9, Q66*1e9]
        ])
        laminate = Laminate(datasets.CarbonT300_Epoxy5208,off_axis_angle=90)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(laminate.Q[i,j]/1e9, Q_correct[i,j]/1e9, delta=10**Decimal(str(Q_correct[i,j]/1e9)).as_tuple().exponent)



    ############### S Matrix on axis and off axis #############
    def test_matrix_S_0_CarbonT300_Epoxy5208(self):
        S11, S22, S12, S66, S16, S26 = 5.52, 97.09, -1.55, 139.4, 0, 0
        S_correct = np.array([
            [S11, S12, S16],
            [S12, S22, S26],
            [S16, S26, S66]
        ]) #TPa^-1
        laminate = Laminate(datasets.CarbonT300_Epoxy5208,off_axis_angle=0)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(laminate.S[i,j]/1e-12, S_correct[i,j], delta=10**Decimal(str(S_correct[i,j])).as_tuple().exponent)

    def test_matrix_S_15_CarbonT300_Epoxy5208(self):
        S11, S22, S12, S66, S16, S26 = 13.77, 93.06, -3.66, 131.0, -30.20, -15.58
        S_correct = np.array([
            [S11, S12, S16],
            [S12, S22, S26],
            [S16, S26, S66]
        ]) #TPa^-1
        laminate = Laminate(datasets.CarbonT300_Epoxy5208,off_axis_angle=15)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(laminate.S[i,j]/1e-12, S_correct[i,j], delta=10**Decimal(str(S_correct[i,j])).as_tuple().exponent)

    def test_matrix_S_30_CarbonT300_Epoxy5208(self):
        S11, S22, S12, S66, S16, S26 = 34.75, 80.53, -7.88, 114.1, -46.96, -32.34
        S_correct = np.array([
            [S11, S12, S16],
            [S12, S22, S26],
            [S16, S26, S66]
        ]) #TPa^-1
        laminate = Laminate(datasets.CarbonT300_Epoxy5208,off_axis_angle=30)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(laminate.S[i,j]/1e-12, S_correct[i,j], delta=10**Decimal(str(S_correct[i,j])).as_tuple().exponent)


    def test_matrix_S_45_CarbonT300_Epoxy5208(self):
        S11, S22, S12, S66, S16, S26 = 59.75, 59.75, -9.99, 105.7, -45.78, -45.78
        S_correct = np.array([
            [S11, S12, S16],
            [S12, S22, S26],
            [S16, S26, S66]
        ]) #TPa^-1
        laminate = Laminate(datasets.CarbonT300_Epoxy5208,off_axis_angle=45)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(laminate.S[i,j]/1e-12, S_correct[i,j], delta=10**Decimal(str(S_correct[i,j])).as_tuple().exponent)
                
    def test_matrix_S_60_CarbonT300_Epoxy5208(self):
        S11, S22, S12, S66, S16, S26 = 80.53, 34.75, -7.88, 114.1, -32.34, -46.96
        S_correct = np.array([
            [S11, S12, S16],
            [S12, S22, S26],
            [S16, S26, S66]
        ]) #TPa^-1
        laminate = Laminate(datasets.CarbonT300_Epoxy5208,off_axis_angle=60)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(laminate.S[i,j]/1e-12, S_correct[i,j], delta=10**Decimal(str(S_correct[i,j])).as_tuple().exponent)
                
    def test_matrix_S_70_CarbonT300_Epoxy5208(self):
        S11, S22, S12, S66, S16, S26 = 93.06, 13.77, -3.66, 131.0, -15.58, -30.20
        S_correct = np.array([
            [S11, S12, S16],
            [S12, S22, S26],
            [S16, S26, S66]
        ]) #TPa^-1
        laminate = Laminate(datasets.CarbonT300_Epoxy5208,off_axis_angle=75)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(laminate.S[i,j]/1e-12, S_correct[i,j], delta=10**Decimal(str(S_correct[i,j])).as_tuple().exponent)
                
    def test_matrix_S_90_CarbonT300_Epoxy5208(self):
        S11, S22, S12, S66, S16, S26 = 97.09, 5.52, -1.54, 139.4, 0.0, 0.0
        S_correct = np.array([
            [S11, S12, S16],
            [S12, S22, S26],
            [S16, S26, S66]
        ]) #TPa^-1
        laminate = Laminate(datasets.CarbonT300_Epoxy5208,off_axis_angle=90)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(laminate.S[i,j]/1e-12, S_correct[i,j], delta=10**Decimal(str(S_correct[i,j])).as_tuple().exponent)


    ############# Properties on and off axis laminate ####################
    def test_properties_0_CarbonT300_Epoxy5208(self):
        E1, E6, V21, V61, V16 = 181.0, 7.17, 0.280, 0.0, 0.0
        laminate = Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0)
        self.assertAlmostEqual(laminate.E1/1e9, E1, delta=10**Decimal(str(E1)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.E6/1e9, E6, delta=10**Decimal(str(E6)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V21, V21, delta=10**Decimal(str(V21)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V61, V61, delta=10**Decimal(str(V61)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V16, V16, delta=10**Decimal(str(V16)).as_tuple().exponent)

    def test_properties_5_CarbonT300_Epoxy5208(self):
        E1, E6, V21, V61, V16 = 154.4, 7.22, 0.278, -1.673, -0.0782
        laminate = Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=5)
        self.assertAlmostEqual(laminate.E1/1e9, E1, delta=10**Decimal(str(E1)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.E6/1e9, E6, delta=10**Decimal(str(E6)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V21, V21, delta=10**Decimal(str(V21)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V61, V61, delta=10**Decimal(str(V61)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V16, V16, delta=10**Decimal(str(V16)).as_tuple().exponent)

    def test_properties_10_CarbonT300_Epoxy5208(self):
        E1, E6, V21, V61, V16 = 107.8, 7.37, 0.273, -2.273, -0.155
        laminate = Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=10)
        self.assertAlmostEqual(laminate.E1/1e9, E1, delta=10**Decimal(str(E1)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.E6/1e9, E6, delta=10**Decimal(str(E6)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V21, V21, delta=10**Decimal(str(V21)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V61, V61, delta=10**Decimal(str(V61)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V16, V16, delta=10**Decimal(str(V16)).as_tuple().exponent)

    def test_properties_15_CarbonT300_Epoxy5208(self):
        E1, E6, V21, V61, V16 = 72.62, 7.63, 0.265, -2.193, -0.230
        laminate = Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=15)
        self.assertAlmostEqual(laminate.E1/1e9, E1, delta=10**Decimal(str(E1)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.E6/1e9, E6, delta=10**Decimal(str(E6)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V21, V21, delta=10**Decimal(str(V21)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V61, V61, delta=10**Decimal(str(V61)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V16, V16, delta=10**Decimal(str(V16)).as_tuple().exponent)

    def test_properties_30_CarbonT300_Epoxy5208(self):
        E1, E6, V21, V61, V16 = 28.78, 8.76, 0.226, -1.351, -0.411
        laminate = Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=30)
        self.assertAlmostEqual(laminate.E1/1e9, E1, delta=10**Decimal(str(E1)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.E6/1e9, E6, delta=10**Decimal(str(E6)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V21, V21, delta=10**Decimal(str(V21)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V61, V61, delta=10**Decimal(str(V61)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V16, V16, delta=10**Decimal(str(V16)).as_tuple().exponent)

    def test_properties_45_CarbonT300_Epoxy5208(self):
        E1, E6, V21, V61, V16 = 16.73, 9.46, 0.167, -0.766, -0.433
        laminate = Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=45)
        self.assertAlmostEqual(laminate.E1/1e9, E1, delta=10**Decimal(str(E1)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.E6/1e9, E6, delta=10**Decimal(str(E6)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V21, V21, delta=10**Decimal(str(V21)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V61, V61, delta=10**Decimal(str(V61)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V16, V16, delta=10**Decimal(str(V16)).as_tuple().exponent)

    def test_properties_60_CarbonT300_Epoxy5208(self):
        E1, E6, V21, V61, V16 = 12.41, 8.76, 0.0978, -0.401, -0.283
        laminate = Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=60)
        self.assertAlmostEqual(laminate.E1/1e9, E1, delta=10**Decimal(str(E1)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.E6/1e9, E6, delta=10**Decimal(str(E6)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V21, V21, delta=10**Decimal(str(V21)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V61, V61, delta=10**Decimal(str(V61)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V16, V16, delta=10**Decimal(str(V16)).as_tuple().exponent)

    def test_properties_90_CarbonT300_Epoxy5208(self):
        E1, E6, V21, V61, V16 = 10.3, 7.17, 0.0159, 0.0, 0.0
        laminate = Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90)
        self.assertAlmostEqual(laminate.E1/1e9, E1, delta=10**Decimal(str(E1)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.E6/1e9, E6, delta=10**Decimal(str(E6)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V21, V21, delta=10**Decimal(str(V21)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V61, V61, delta=10**Decimal(str(V61)).as_tuple().exponent)
        self.assertAlmostEqual(laminate.V16, V16, delta=10**Decimal(str(V16)).as_tuple().exponent)
