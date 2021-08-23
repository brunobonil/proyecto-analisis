from sympy.core.function import diff
from sympy.core.sympify import sympify

def formula_iterar(f):
    f = sympify(f)
    formula = sympify('x') - (f/diff(f))
    sympify(formula)
    return formula


if __name__ == '__main__':
    funcion = (str(input("Ingrese la función a iterar: ")))
    xi = (float(input("Ingrese el x inicial: ")))
    prec = float(input("Ingrese el error deseado: "))
    tope = 20
    error = 1
    i = 0
    g = formula_iterar(funcion)

    while i != tope and prec < error:
        i += 1
        print(f'\n\t--------------------Iteración N°{i}--------------------')

        print(f'f(x) = {funcion}')
    
        print(f'\nFórmula Iterativa: \t{g}')

        print(f'\nxi = {xi}')

        result = float(g.subs('x', xi))
        print(f'g(xi) = {result}')
    
        error = abs(result - xi)
        print(f'\nError aproximado: {error}')

        xi = result
