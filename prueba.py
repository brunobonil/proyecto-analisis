import sympy
from sympy.core.sympify import sympify
from sympy.core.function import diff

fn = (str(input("Ingrese la función a iterar: ")))
sympify(fn)
derivada = diff(fn, 'x')
print(derivada)