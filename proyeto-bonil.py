import sympy
from sympy.core.function import diff
from sympy.core.sympify import sympify

def derivar(fn, xi):
    sympify(fn)
    fprima = diff(fn, 'x')
    sympify(fprima)
    formula = xi - (fn/fprima)
    sympify(formula)
    return formula

if __name__ == '__main__':
    fn = (str(input("Ingrese la función a iterar: ")))
    xi = (int(input("Ingrese el x inicial: ")))

    print(derivar(fn, xi))