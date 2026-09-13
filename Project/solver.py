def solve(expr_input, choice):
    import sympy as sp
    x = sp.symbols('x')

    expr = sp.sympify(expr_input)

    if "Deriv" in choice:
        return sp.diff(expr, x)
    else:
        return sp.integrate(expr, x)