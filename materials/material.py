import numpy as np


class Material():
    def __init__(self, E_x:float, E_y:float, E_s:float, V_xy:float, V_yx:float, *args, **kwargs) -> None:
        """
        units:
            E -> Pa
        """
        self.matrix_name = kwargs.get("matrix_name")
        self.matrix_type = kwargs.get("matrix_type")
        self.reinforcement_name = kwargs.get("reinforcement_name")
        self.reinforcement_type = kwargs.get("reinforcement_type")
        self.Vf = kwargs.get("Vf")

        self.E_x = float(E_x)
        self.E_y = float(E_y)
        self.E_s = float(E_s)
        self.V_xy = float(V_xy)
        if V_yx is None:
            self.V_yx = self.V_xy/self.E_x*self.E_y
        else:
            self.V_yx = float(V_yx)
    
        # stess on axis -> stain on axis
        # S in laminate
        self.S_on = np.array([
            [1.0/self.E_x, -self.V_yx/self.E_y, 0.0],
            [-self.V_xy/self.E_x, 1.0/self.E_y, 0.0],
            [0.0, 0.0, 1.0/self.E_s]
        ])
        # strain on axis -> stress on axis
        self.C_on = np.linalg.inv(self.S_on)

    @staticmethod
    def find_properties_with_S_matrix(S:np.array):
        E_x = 1.0/S[0,0]
        E_y = 1.0/S[1,1]
        E_s = 1.0/S[2,2]
        V_yx = -E_y*S[0,1]
        V_xy = -E_x*S[1,0]
        return E_x, E_y, E_s, V_yx, V_xy
