import sympy as sp

x = sp.symbols('x')
expr = sp.sympify("x**2 + 3*x*x")

print(sp.diff(expr, x))
print(sp.integrate(expr, x))