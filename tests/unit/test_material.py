import unittest
import numpy as np
from decimal import Decimal

from composite import Laminate
from materials import datasets, material

class MaterialTest(unittest.TestCase):
    ################# MATRIX S ####################
    def test_matrix_S_on_CarbonT300_Epoxy5208(self):
        S_correct = np.array([
            [5.525e-12,  -1.547e-12, 0.0      ],
            [-1.547e-12, 97.09e-12,  0.0      ],
            [0.0,        0.0,        139.5e-12]
        ])
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(datasets.CarbonT300_Epoxy5208.S_on[i,j], S_correct[i,j], delta=10**Decimal(str(S_correct[i,j])).as_tuple().exponent)
        return
    
    def test_matrix_S_on_BoronB4_Epoxy5505(self):
        S_correct = np.array([
            [4.902e-12,  -1.128e-12, 0.0      ],
            [-1.128e-12, 54.05e-12,  0.0      ],
            [0.0,        0.0,        178.89e-12] #TODO:Book -> [0.0,        0.0,        172.7e-12]
        ])
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(datasets.BoronB4_Epoxy5505.S_on[i,j], S_correct[i,j], delta=10**Decimal(str(S_correct[i,j])).as_tuple().exponent)
        return
    
    def test_matrix_S_on_GraphiteAS_Epoxy3501(self):
        S_correct = np.array([
            [7.246e-12,  -2.174e-12, 0.0      ],
            [-2.174e-12, 111.6e-12,  0.0      ],
            [0.0,        0.0,        140.8e-12]
        ])
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(datasets.GraphiteAS_Epoxy3501.S_on[i,j], S_correct[i,j], delta=10**Decimal(str(S_correct[i,j])).as_tuple().exponent)
        return
    
    def test_matrix_S_on_GlassScotchply_Epoxy1002(self):
        S_correct = np.array([
            [25.91e-12,  -6.736e-12, 0.0      ],
            [-6.7e-12, 120.9e-12,  0.0      ],#TODO: Book -6.744e-12
            [0.0,        0.0,        241.5e-12]
        ])
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(datasets.GlassScotchply_Epoxy1002.S_on[i,j], S_correct[i,j], delta=10**Decimal(str(S_correct[i,j])).as_tuple().exponent)
        return
    
    def test_matrix_S_on_AramidKevlar49_Epoxy(self):
        S_correct = np.array([
            [13.16e-12,  -4.474e-12, 0.0      ],
            [-4.474e-12, 181.8e-12,  0.0      ],
            [0.0,        0.0,        434.8e-12]
        ])
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(datasets.AramidKevlar49_Epoxy.S_on[i,j], S_correct[i,j], delta=10**Decimal(str(S_correct[i,j])).as_tuple().exponent)
        return
    
    
    ################# MATRIX C ####################

    def test_matrix_C_CarbonT300_Epoxy5208(self):
        Cxx, Cyy, Cxy, Css = 205.0, 18.58, 4.275, 5.79
        C_correct = np.array([
            [181.8e9,  2.897e9, 0.0],
            [2.897e9,  10.34e9, 0.0],
            [0.0,      0.0,     7.17e9]
        ])
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(datasets.CarbonT300_Epoxy5208.C_on[i,j]/1e9, C_correct[i,j]/1e9, delta=10**Decimal(str(C_correct[i,j]/1e9)).as_tuple().exponent)
        return
    
    def test_matrix_C_BoronB4_Epoxy5505(self):
        Cxx, Cyy, Cxy, Css = 205.0, 18.59, 4.276, 5.59 #TODO: Book 4.275, 18.58, 5.79

        C_correct = np.array([
            [Cxx*1.0e9,  Cxy*1.0e9, 0.0],
            [Cxy*1.0e9,    Cyy*1.0e9, 0.0],
            [0.0,        0.0,       Css*1.0e9]
        ])
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(datasets.BoronB4_Epoxy5505.C_on[i,j]/1e9, C_correct[i,j]/1e9, delta=10**Decimal(str(C_correct[i,j]/1e9)).as_tuple().exponent)
        return

    def test_matrix_C_GraphiteAS_Epoxy3501(self):
        Cxx, Cyy, Cxy, Css = 138.8, 9.013, 2.704, 7.1

        C_correct = np.array([
            [Cxx*1.0e9,  Cxy*1.0e9, 0.0],
            [Cxy*1.0e9,    Cyy*1.0e9, 0.0],
            [0.0,        0.0,       Css*1.0e9]
        ])
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(datasets.GraphiteAS_Epoxy3501.C_on[i,j]/1e9, C_correct[i,j]/1e9, delta=10**Decimal(str(C_correct[i,j]/1e9)).as_tuple().exponent)
        return
    
    def test_matrix_C_GlassScotchply_Epoxy1002(self):
        Cxx, Cyy, Cxy, Css = 39.16, 8.392, 2.182, 4.14 

        C_correct = np.array([
            [Cxx*1.0e9,  Cxy*1.0e9, 0.0],
            [Cxy*1.0e9,    Cyy*1.0e9, 0.0],
            [0.0,        0.0,       Css*1.0e9]
        ])
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(datasets.GlassScotchply_Epoxy1002.C_on[i,j]/1e9, C_correct[i,j]/1e9, delta=10**Decimal(str(C_correct[i,j]/1e9)).as_tuple().exponent)
        return

    def test_matrix_C_AramidKevlar49_Epoxy(self):
        Cxx, Cyy, Cxy, Css = 76.64, 5.546, 1.886, 2.3

        C_correct = np.array([
            [Cxx*1.0e9,  Cxy*1.0e9, 0.0],
            [Cxy*1.0e9,    Cyy*1.0e9, 0.0],
            [0.0,        0.0,       Css*1.0e9]
        ])
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(datasets.AramidKevlar49_Epoxy.C_on[i,j]/1e9, C_correct[i,j]/1e9, delta=10**Decimal(str(C_correct[i,j]/1e9)).as_tuple().exponent)
        return
    
    ########## General function ##########

    def test_find_properties_with_S_on_matrix_CarbonT300_Epoxy5208(self):
        S = np.array([
            [5.525e-12, -1.547e-12, 0.0      ],
            [-1.547e-12, 97.09e-12, 0.0      ],
            [0.0,        0.0,       139.5e-12],
        ])
        E_x, E_y, E_s, V_yx, V_xy = material.Material.find_properties_with_S_matrix(S)
        self.assertAlmostEqual(E_x/1e9, datasets.CarbonT300_Epoxy5208.E_x/1e9, delta=10**Decimal(str(datasets.CarbonT300_Epoxy5208.E_x/1e9)).as_tuple().exponent)
        self.assertAlmostEqual(E_y/1e9, datasets.CarbonT300_Epoxy5208.E_y/1e9, delta=10**Decimal(str(datasets.CarbonT300_Epoxy5208.E_y/1e9)).as_tuple().exponent)
        self.assertAlmostEqual(E_s/1e9, datasets.CarbonT300_Epoxy5208.E_s/1e9, delta=10**Decimal(str(datasets.CarbonT300_Epoxy5208.E_x/1e9)).as_tuple().exponent)
        self.assertAlmostEqual(V_xy/1e9, datasets.CarbonT300_Epoxy5208.V_xy/1e9, delta=10**Decimal(str(datasets.CarbonT300_Epoxy5208.V_xy/1e9)).as_tuple().exponent)
        self.assertAlmostEqual(V_yx/1e9, datasets.CarbonT300_Epoxy5208.V_yx/1e9, places=5)
    
