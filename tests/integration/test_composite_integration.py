import unittest
import numpy as np
from decimal import Decimal

from composite import Laminate, Composite
from materials import datasets, material

class CompositeIntegrationTest(unittest.TestCase):

    ############################## Three-point bend page (208) ############################
    def test_three_point_bend_composite(self):
        K_correct = [2.34, -.213, 0.0] #TODO: Book 0.212 page(209)
        strain_0_correct = [2.34e-3,-.213e-3, 0.0] #TODO Book .212 page209
        stress_0_correct = [425, 4.57, 0.0]# MPa #TODO Book 424 page(209)
        strain_90_correct = [1.17e-3, -.106e-3, 0.0]
        stress_90_correct = [11.8, -16.0, 0.0]# MPa #TODO: BOOK 11.7, -15.88 page(210)

        th = 125e-6*4.0
        laminates = [
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=th),
        ]
        composite = Composite(laminates)
        moment = np.array([250,0.0,0.0])
        properties = composite.moment_apply(moment)

        for i in range(3):
            self.assertAlmostEqual(properties["K"][i], K_correct[i], delta=10**Decimal(str(K_correct[i])).as_tuple().exponent)
        
        

        for i in range(3):
            self.assertAlmostEqual(properties["strain"][laminates[0]][i], strain_0_correct[i], delta=10**Decimal(str(strain_0_correct[i])).as_tuple().exponent)
            self.assertAlmostEqual(properties["stress"][laminates[0]][i]/1e6, stress_0_correct[i], delta=10**Decimal(str(stress_0_correct[i])).as_tuple().exponent)
            self.assertAlmostEqual(properties["strain"][laminates[1]][i], strain_90_correct[i], delta=10**Decimal(str(strain_90_correct[i])).as_tuple().exponent)
            self.assertAlmostEqual(properties["stress"][laminates[1]][i]/1e6, stress_90_correct[i], delta=10**Decimal(str(stress_90_correct[i])).as_tuple().exponent)


    ############################## stress and strain ply #######################3
    def test_symetric_stress_every_laminate(self):

        th = 125e-6
        stress_composite = np.array([1.0e6,0.0,0.0])
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
        strain_off_c = composite.stress2strain(stress_composite)

        strain_0_off_l = strain_off_c
        strain_0_on_l = composite.laminates[0].transpose_strain.dot(strain_0_off_l)
        stress_0_off_l = composite.laminates[0].strain2stress(strain_0_off_l)
        stress_0_on_l = composite.laminates[0].transpose_stress.dot(stress_0_off_l)

        strain_90_off_l = strain_off_c
        stress_90_off_l = composite.laminates[5].strain2stress(strain_90_off_l)
        strain_90_on_l = composite.laminates[5].transpose_strain.dot(strain_90_off_l)
        stress_90_on_l = composite.laminates[5].transpose_stress.dot(stress_90_off_l)


        print()