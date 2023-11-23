from .material import Material

CarbonT300_Epoxy5208 = Material(
    E_x=181.0e9, E_y=10.3e9, E_s=7.17e9, V_xy=0.28, V_yx=None, 
    matrix_name="Epoxy", matrix_type="5208", reinforcement_name="Carbon", reinforcement_type="T300", Vf=.70
)

BoronB4_Epoxy5505 = Material(
    E_x=204e9, E_y=18.5e9, E_s=5.59e9, V_xy=0.23, V_yx=None, 
    matrix_name="Epoxy", matrix_type="5505", reinforcement_name="Boron", reinforcement_type="B(4)", Vf=.50
)

GraphiteAS_Epoxy3501 = Material(
    E_x=138e9, E_y=8.96e9, E_s=7.1e9, V_xy=0.30, V_yx=None, 
    matrix_name="Epoxy", matrix_type="3501", reinforcement_name="Graphite", reinforcement_type="AS", Vf=.66
)

GlassScotchply_Epoxy1002 = Material(
    E_x=38.6e9, E_y=8.27e9, E_s=4.14e9, V_xy=0.26, V_yx=None, 
    matrix_name="Epoxy", matrix_type="1002", reinforcement_name="Glass", reinforcement_type="Scotchply", Vf=.45
)

AramidKevlar49_Epoxy = Material(
    E_x=76e9, E_y=5.5e9, E_s=2.3e9, V_xy=0.34, V_yx=None, 
    matrix_name="Epoxy", matrix_type="-", reinforcement_name="Aramid", reinforcement_type="Kevlar49", Vf=.60
)