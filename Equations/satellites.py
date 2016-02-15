from sympy import symbols
from sympy import Function
from sympy import diff
from sympy import Eq
from sympy import solve
from sympy import latex

#symbols
M, m, l, G = symbols('M, m, l, G')
t = symbols('t')

r = Function('r')
r_dot = diff(r(t), t)
r_dot_dot = diff(r_dot, t)

theta = Function('theta')
theta_dot = diff(theta(t), t)
theta_dot_dot = diff(theta_dot, t)

T = m / 2 * (r_dot ** 2 + r(t) * theta_dot ** 2)
V = -G * M * m / r(t)

L = T - V

lhs_r = diff(diff(L, r_dot), t)
rhs_r = diff(L, r(t))
lhs_th = diff(diff(L, theta_dot), t)
rhs_th = diff(L, theta(t))

print solve(Eq(lhs_r, rhs_r), r_dot_dot)
print solve(Eq(lhs_th, rhs_th), theta_dot_dot)