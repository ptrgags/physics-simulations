from sympy import symbols
from sympy import Function
from sympy import diff
from sympy import Eq
from sympy import cos
from sympy import sin
from sympy import solve
from sympy import simplify
from sympy import factor
from sympy import expand
from sympy import latex

#symbols
m1, m2, l, g = symbols('m1, m2, l, g')
t = symbols('t')


#position and its derivatives
x = Function('x')
x_dot = diff(x(t), t)
x_dot_dot = diff(x_dot, t)

#Mass of system
M = m1 + m2

T = M / 2 * x_dot ** 2
V = - m1 * g * x(t) - m2 * g * (l - x(t))

L = T - V

lhs = diff(diff(L, x_dot), t)
rhs = diff(L, x(t))

print latex(solve(Eq(lhs, rhs), x_dot_dot))