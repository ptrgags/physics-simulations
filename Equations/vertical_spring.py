from sympy import symbols
from sympy import Function
from sympy import diff
from sympy import Eq
from sympy import solve

#constants and variables
l, m, g, k, t = symbols('l m g k t')

#x and its derivatives
x = Function('x')(t)
x_dot = diff(x, t)
x_dot_dot = diff(x_dot, t)

V = m * g * (x + l) + k / 2 * x ** 2
T = m / 2 * x_dot ** 2
L = T - V

rhs = diff(L, x)
lhs = diff(diff(L, x_dot), t)

motion = solve(Eq(lhs, rhs), x_dot_dot)
print motion
