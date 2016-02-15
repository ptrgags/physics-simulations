from sympy import symbols
from sympy import Function
from sympy import diff
from sympy import Eq
from sympy import solve

#constants and variables
l1, l2, m1, m2, g, k1, k2, t = symbols('l1 l2 m1 m2 g k1 k2 t')

#x and its derivatives
x1 = Function('x1')(t)
x_dot1 = diff(x1, t)
x_dot_dot1 = diff(x_dot1, t)
x2 = Function('x2')(t)
x_dot2 = diff(x2, t)
x_dot_dot2 = diff(x_dot2, t)

V = k1 / 2 * x1 ** 2 + k2 / 2 * (x2 - x1) ** 2
T = m1 / 2 * x_dot1 ** 2 + m2 / 2 * x_dot2 ** 2
L = T - V

rhs1 = diff(L, x1)
lhs1 = diff(diff(L, x_dot1), t)
rhs2 = diff(L, x2)
lhs2 = diff(diff(L, x_dot2), t)

motion1 = solve(Eq(lhs1, rhs1), x_dot_dot1)
print motion1

motion2 = solve(Eq(lhs2, rhs2), x_dot_dot2)
print motion2