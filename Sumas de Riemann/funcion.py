
import numpy as np

class Funcion:
    def __init__(self) -> None:
        self._funcion = ""


    @property
    def get_funcion(self) -> str:
        return self._funcion


    @get_funcion.setter
    def set_funcion(self, funcion: str) -> None:

        equivalencias = {
            "sin": "np.sin",
            "cos": "np.cos",
            "tan": "np.tan",
            "arcsin": "np.arcsin",
            "arccos": "np.arccos",
            "arctan": "np.arctan",
            "sinh": "np.sinh",
            "cosh": "np.cosh",
            "tanh": "np.tanh",
            "arcsinh": "np.arcsinh",
            "arccosh": "np.arccosh",
            "arctanh": "np.arctanh",
            "exp": "np.exp",
            "log": "np.log",
            "log10": "np.log10",
            "sqrt": "np.sqrt",
            "cbrt": "np.cbrt",
            "^": "**"
        }

        for org, sust in equivalencias.items():
            funcion = funcion.replace(org, sust)

        self._funcion = funcion


    def evaluar_funcion(self, x: float):
        return eval(self._funcion)
