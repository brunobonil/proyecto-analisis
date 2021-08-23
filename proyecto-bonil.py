from sympy.core.function import diff
from sympy.core.sympify import sympify

def formula_iterar(fn):
    fn = sympify(fn)
    formula = sympify('x') - (fn/diff(fn))
    sympify(formula)
    return formula


if __name__ == '__main__':
    fn = (str(input("Ingrese la función a iterar: ")))
    xi = (float(input("Ingrese el x inicial: ")))
    prec = float(input("Ingrese el error aproximado: "))
    max_iter = 20
    error = 1
    i = 0
    g = formula_iterar(fn)
    num_it = xi
    while i != max_iter and prec < error:
        i += 1
        print(f'\n\t--------------------Iteración N°{i}--------------------')
        print(f'Fórmula Iterativa {g}')
        print(f'xi = {num_it}')
        result = float(g.subs('x', num_it))
        print(f'g(xi) = {result}')
        error = abs(result - num_it)
        print(f"Error: {error}")
        num_it = result
