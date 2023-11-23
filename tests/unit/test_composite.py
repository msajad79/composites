import unittest
import numpy as np
from decimal import Decimal

from composite import Laminate, Composite
from materials import datasets, material

class CompositeTest(unittest.TestCase):
    ################ matric A,a TABLE 4_7 page135 #########################
    def test_matrix_Aa_cross_ply1_TAble4_7(self):
        A11, A22, A12, A66, A16 = 96.08, 96.08, 2.89, 7.17, 0.0
        A26 = A16
        A_correct = np.array([
            [A11, A12, A16],
            [A12, A22, A26],
            [A16, A26, A66]
        ])
        
        a11, a22, a12, a66, a16 = 10.41, 10.41, -0.314, 139.47, 0.0
        a26 = a16
        a_correct = np.array([
            [a11, a12, a16],
            [a12, a22, a26],
            [a16, a26, a66]
        ])

        laminates = [
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=.25),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90, thickness=.25),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90, thickness=.25),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=.25),
        ]
        composite = Composite(laminates)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(composite.A[i,j]/1e9, A_correct[i,j], delta=10**Decimal(str(A_correct[i,j])).as_tuple().exponent)
                self.assertAlmostEqual(composite.a[i,j]/1e-12, a_correct[i,j], delta=10**Decimal(str(a_correct[i,j])).as_tuple().exponent)
                
    def test_matrix_Aa_cross_ply2_TAble4_7(self):
        A11, A22, A12, A66, A16 = 124.65, 67.50, 2.89, 7.17, 0.0
        A26 = A16
        A_correct = np.array([
            [A11, A12, A16],
            [A12, A22, A26],
            [A16, A26, A66]
        ])
        a11, a22, a12, a66, a16 = 8.03, 14.82, -0.344, 139.47, 0.0
        a26 = a16
        a_correct = np.array([
            [a11, a12, a16],
            [a12, a22, a26],
            [a16, a26, a66]
        ])
        CL = 6
        laminates = [
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
        ]
        composite = Composite(laminates)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(composite.A[i,j]/1e9, A_correct[i,j], delta=10**Decimal(str(A_correct[i,j])).as_tuple().exponent)
                self.assertAlmostEqual(composite.a[i,j]/1e-12, a_correct[i,j], delta=10**Decimal(str(a_correct[i,j])).as_tuple().exponent)
     
                
    def test_matrix_Aa_cross_ply3_TAble4_7(self):
        A11, A22, A12, A66, A16 = 147.51, 44.63, 2.89, 7.17, 0.0
        A26 = A16
        A_correct = np.array([
            [A11, A12, A16],
            [A12, A22, A26],
            [A16, A26, A66]
        ])
        a11, a22, a12, a66, a16 = 6.78, 22.43, -0.440, 139.47, 0.0
        a26 = a16
        a_correct = np.array([
            [a11, a12, a16],
            [a12, a22, a26],
            [a16, a26, a66]
        ])
        CL = 10
        laminates = [
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
        ]
        composite = Composite(laminates)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(composite.A[i,j]/1e9, A_correct[i,j], delta=10**Decimal(str(A_correct[i,j])).as_tuple().exponent)
                self.assertAlmostEqual(composite.a[i,j]/1e-12, a_correct[i,j], delta=10**Decimal(str(a_correct[i,j])).as_tuple().exponent)
    
    
    def test_matrix_Aa_cross_ply4_TAble4_7(self):
        A11, A22, A12, A66, A16 = 162.75, 29.39, 2.89, 7.17, 0.0
        A26 = A16
        A_correct = np.array([
            [A11, A12, A16],
            [A12, A22, A26],
            [A16, A26, A66]
        ])
        a11, a22, a12, a66, a16 = 6.15, 34.07, -0.606, 139.47, 0.0
        a26 = a16
        a_correct = np.array([
            [a11, a12, a16],
            [a12, a22, a26],
            [a16, a26, a66]
        ])
        CL = 18
        laminates = [
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
        ]
        composite = Composite(laminates)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(composite.A[i,j]/1e9, A_correct[i,j], delta=10**Decimal(str(A_correct[i,j])).as_tuple().exponent)
                self.assertAlmostEqual(composite.a[i,j]/1e-12, a_correct[i,j], delta=10**Decimal(str(a_correct[i,j])).as_tuple().exponent)
     

    ############################## matrix A and a angle ply #######################3
    def test_matrix_Aa_angle_ply1_TAble4_9(self):
        A11, A22, A12, A66, A16 = 181.8, 10.3, 2.90, 7.17, 0.0
        A26 = A16
        A_correct = np.array([
            [A11, A12, A16],
            [A12, A22, A26],
            [A16, A26, A66]
        ])        
        a11, a22, a12, a66, a16 = 5.52, 97.08, -1.54, 139.47, 0.0
        a26 = a16
        a_correct = np.array([
            [a11, a12, a16],
            [a12, a22, a26],
            [a16, a26, a66]
        ])
        CL = 4
        laminates = [
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-0, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=1/CL),
        ]
        composite = Composite(laminates)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(composite.A[i,j]/1e9, A_correct[i,j], delta=10**Decimal(str(A_correct[i,j])).as_tuple().exponent)
                self.assertAlmostEqual(composite.a[i,j]/1e-12, a_correct[i,j], delta=10**Decimal(str(a_correct[i,j])).as_tuple().exponent)
     
    
    def test_matrix_Aa_angle_ply2_TAble4_9(self):
        A11, A22, A12, A66, A16 = 160.4, 11.9, 12.75, 17.02, 0.0
        A26 = A16
        A_correct = np.array([
            [A11, A12, A16],
            [A12, A22, A26],
            [A16, A26, A66]
        ])        
        a11, a22, a12, a66, a16 = 6.80, 91.21, -7.24, 58.73, 0.0
        a26 = a16
        a_correct = np.array([
            [a11, a12, a16],
            [a12, a22, a26],
            [a16, a26, a66]
        ])
        CL = 4
        theta = 15
        laminates = [
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=theta, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-theta, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-theta, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=theta, thickness=1/CL),
        ]
        composite = Composite(laminates)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(composite.A[i,j]/1e9, A_correct[i,j], delta=10**Decimal(str(A_correct[i,j])).as_tuple().exponent)
                self.assertAlmostEqual(composite.a[i,j]/1e-12, a_correct[i,j], delta=10**Decimal(str(a_correct[i,j])).as_tuple().exponent)
     

     
    def test_matrix_Aa_angle_ply3_TAble4_9(self):
        A11, A22, A12, A66, A16 = 109.3, 23.6, 32.46, 36.73, 0.0
        A26 = A16
        A_correct = np.array([
            [A11, A12, A16],
            [A12, A22, A26],
            [A16, A26, A66]
        ])        
        a11, a22, a12, a66, a16 = 15.42, 71.36, -21.18, 27.22, 0.0
        a26 = a16
        a_correct = np.array([
            [a11, a12, a16],
            [a12, a22, a26],
            [a16, a26, a66]
        ])
        CL = 4
        theta = 30.0
        laminates = [
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=theta, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-theta, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-theta, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=theta, thickness=1/CL),
        ]
        composite = Composite(laminates)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(composite.A[i,j]/1e9, A_correct[i,j], delta=10**Decimal(str(A_correct[i,j])).as_tuple().exponent)
                self.assertAlmostEqual(composite.a[i,j]/1e-12, a_correct[i,j], delta=10**Decimal(str(a_correct[i,j])).as_tuple().exponent)
     

    def test_matrix_Aa_angle_ply4_TAble4_9(self):
        A11, A22, A12, A66, A16 = 56.6, 56.6, 42.32, 46.59, 0.0
        A26 = A16
        A_correct = np.array([
            [A11, A12, A16],
            [A12, A22, A26],
            [A16, A26, A66]
        ])        
        a11, a22, a12, a66, a16 = 39.91, 39.91, -29.81, 21.46, 0.0
        a26 = a16
        a_correct = np.array([
            [a11, a12, a16],
            [a12, a22, a26],
            [a16, a26, a66]
        ])
        CL = 4
        theta = 45.0
        laminates = [
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=theta, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-theta, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-theta, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=theta, thickness=1/CL),
        ]
        composite = Composite(laminates)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(composite.A[i,j]/1e9, A_correct[i,j], delta=10**Decimal(str(A_correct[i,j])).as_tuple().exponent)
                self.assertAlmostEqual(composite.a[i,j]/1e-12, a_correct[i,j], delta=10**Decimal(str(a_correct[i,j])).as_tuple().exponent)
     

    def test_matrix_Aa_angle_ply5_TAble4_9(self):
        A11, A22, A12, A66, A16 = 23.6, 109.3, 32.46, 36.73, 0.0
        A26 = A16
        A_correct = np.array([
            [A11, A12, A16],
            [A12, A22, A26],
            [A16, A26, A66]
        ])        
        a11, a22, a12, a66, a16 = 71.36, 15.42, -21.18, 27.22, 0.0
        a26 = a16
        a_correct = np.array([
            [a11, a12, a16],
            [a12, a22, a26],
            [a16, a26, a66]
        ])
        CL = 4
        theta = 60.0
        laminates = [
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=theta, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-theta, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-theta, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=theta, thickness=1/CL),
        ]
        composite = Composite(laminates)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(composite.A[i,j]/1e9, A_correct[i,j], delta=10**Decimal(str(A_correct[i,j])).as_tuple().exponent)
                self.assertAlmostEqual(composite.a[i,j]/1e-12, a_correct[i,j], delta=10**Decimal(str(a_correct[i,j])).as_tuple().exponent)
     

    def test_matrix_Aa_angle_ply6_TAble4_9(self):
        A11, A22, A12, A66, A16 = 11.9, 160.4, 12.75, 17.02, 0.0
        A26 = A16
        A_correct = np.array([
            [A11, A12, A16],
            [A12, A22, A26],
            [A16, A26, A66]
        ])        
        a11, a22, a12, a66, a16 = 91.21, 6.80, -7.24, 58.73, 0.0
        a26 = a16
        a_correct = np.array([
            [a11, a12, a16],
            [a12, a22, a26],
            [a16, a26, a66]
        ])
        CL = 4
        theta = 75.0
        laminates = [
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=theta, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-theta, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-theta, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=theta, thickness=1/CL),
        ]
        composite = Composite(laminates)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(composite.A[i,j]/1e9, A_correct[i,j], delta=10**Decimal(str(A_correct[i,j])).as_tuple().exponent)
                self.assertAlmostEqual(composite.a[i,j]/1e-12, a_correct[i,j], delta=10**Decimal(str(a_correct[i,j])).as_tuple().exponent)
     

    def test_matrix_Aa_angle_ply7_TAble4_9(self):
        A11, A22, A12, A66, A16 = 10.3, 181.8, 2.90, 7.17, 0.0
        A26 = A16
        A_correct = np.array([
            [A11, A12, A16],
            [A12, A22, A26],
            [A16, A26, A66]
        ])        
        a11, a22, a12, a66, a16 = 97.08, 5.52, -1.54, 139.47, 0.0
        a26 = a16
        a_correct = np.array([
            [a11, a12, a16],
            [a12, a22, a26],
            [a16, a26, a66]
        ])
        CL = 4
        theta = 90.0
        laminates = [
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=theta, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-theta, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-theta, thickness=1/CL),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=theta, thickness=1/CL),
        ]
        composite = Composite(laminates)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(composite.A[i,j]/1e9, A_correct[i,j], delta=10**Decimal(str(A_correct[i,j])).as_tuple().exponent)
                self.assertAlmostEqual(composite.a[i,j]/1e-12, a_correct[i,j], delta=10**Decimal(str(a_correct[i,j])).as_tuple().exponent)
     

    ################### MAtrix D  Figure 5.11 Eq 5.70 ###################
    def test_matrix_Dd_composite_cross_ply_m4(self):
        D11, D22, D66, D12, D16, D26 = 106.9, 21.18, 4.78, 1.93, 0.0, 0.0
        D_correct = np.array([
            [D11, D12, D16],
            [D12, D22, D26],
            [D16, D26, D66]
        ])
        d11, d22, d66, d12, d16, d26 = 9.36, 47.27, 209.2, -.85, 0.0, 0.0
        d_correct = np.array([
            [d11, d12, d16],
            [d12, d22, d26],
            [d16, d26, d66]
        ])
        th = 125e-6
        laminates = [
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0.0, thickness=th),
        ]  
        composite = Composite(laminates)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(composite.D[i,j], D_correct[i,j], delta=10**Decimal(str(D_correct[i,j])).as_tuple().exponent)
                self.assertAlmostEqual(composite.d[i,j]*1e3, d_correct[i,j], delta=10**Decimal(str(d_correct[i,j])).as_tuple().exponent)
    
    
    def test_matrix_Dd_composite_cross_ply_m8(self):
        D11, D22, D66, D12, D16, D26 = 85.48, 42.61, 4.78, 1.93, 0.0, 0.0
        D_correct = np.array([
            [D11, D12, D16],
            [D12, D22, D26],
            [D16, D26, D66]
        ])
        d11, d22, d66, d12, d16, d26 = 11.70, 23.48, 209.2, -.530, 0.0, 0.0
        d_correct = np.array([
            [d11, d12, d16],
            [d12, d22, d26],
            [d16, d26, d66]
        ])
        th = 125e-6
        laminates = [
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0.0, thickness=th),
        ]  
        composite = Composite(laminates)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(composite.D[i,j], D_correct[i,j], delta=10**Decimal(str(D_correct[i,j])).as_tuple().exponent)
                self.assertAlmostEqual(composite.d[i,j]*1e3, d_correct[i,j], delta=10**Decimal(str(d_correct[i,j])).as_tuple().exponent)

    def test_matrix_Dd_composite_angle_ply_45_m4(self):
        D11, D22, D66, D12, D16, D26 = 37.77, 37.77, 31.06, 28.21, 21.433, 21.433
        D_correct = np.array([
            [D11, D12, D16],
            [D12, D22, D26],
            [D16, D26, D66]
        ])
        d11, d22, d66, d12, d16, d26 = 66.03, 66.03, 58.35, -38.56, -18.95, -18.95
        d_correct = np.array([
            [d11, d12, d16],
            [d12, d22, d26],
            [d16, d26, d66]
        ])
        th = 125e-6
        laminates = [
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=45.0, thickness=th),
        ]  
        composite = Composite(laminates)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(composite.D[i,j], D_correct[i,j], delta=10**Decimal(str(D_correct[i,j])).as_tuple().exponent)
                self.assertAlmostEqual(composite.d[i,j]*1e3, d_correct[i,j], delta=10**Decimal(str(d_correct[i,j])).as_tuple().exponent)

    
    def test_matrix_Dd_composite_angle_ply_45_m8(self):
        D11, D22, D66, D12, D16, D26 = 37.77, 37.77, 31.06, 28.21, 10.716, 10.716
        D_correct = np.array([
            [D11, D12, D16],
            [D12, D22, D26],
            [D16, D26, D66]
        ])
        d11, d22, d66, d12, d16, d26 = 60.83, 60.83, 36.25, -43.76, -5.88, -5.88
        d_correct = np.array([
            [d11, d12, d16],
            [d12, d22, d26],
            [d16, d26, d66]
        ])
        th = 125e-6
        laminates = [
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=-45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=45.0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=45.0, thickness=th),
        ]  
        composite = Composite(laminates)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(composite.D[i,j], D_correct[i,j], delta=10**Decimal(str(D_correct[i,j])).as_tuple().exponent)
                self.assertAlmostEqual(composite.d[i,j]*1e3, d_correct[i,j], delta=10**Decimal(str(d_correct[i,j])).as_tuple().exponent)

   