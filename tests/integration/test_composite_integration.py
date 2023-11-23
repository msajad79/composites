import unittest
import numpy as np
from decimal import Decimal

from composite import Laminate, Composite
from materials import datasets, material

class CompositeIntegrationTest(unittest.TestCase):

    ############################## Three-point bend page (208) ############################
    def test_three_point_bend_composite(self):
        th = 12.5e-6*4
        laminates = [
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=90, thickness=th),
            Laminate(datasets.CarbonT300_Epoxy5208, off_axis_angle=0, thickness=th),
        ]
        composite = Composite(laminates)
        moment = np.array([250.0,0.0,0.0])
        print("**********")
        print(composite.moment_apply(moment))


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