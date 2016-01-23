from sympy import symbols
from sympy import Function
from sympy import diff
from sympy import sin
from sympy import cos
from sympy import Eq
from sympy import solve
from sympy import latex

l, m, g, k, t = symbols('l m g k t')

r = Function('r')
r_dot = diff(r(t), t)
r_dot_dot = diff(r_dot, t)
theta = Function('theta')
theta_dot = diff(theta(t), t)
theta_dot_dot = diff(theta_dot, t)

#positions in polar coordinates
x = (l + r(t)) * sin(theta(t))
y = -(l + r(t)) * cos(theta(t))

#velocities in polar coordinates
x_dot = diff(x, t)
y_dot = diff(y, t)

#Energy
V = m * g * y + k /2 * r(t) ** 2
T = m / 2 * (x_dot ** 2 + y_dot ** 2)
L = T - V

#Radial component
rhs_r = diff(L, r(t))
lhs_r = diff(diff(L, r_dot), t)

#Angular component
rhs_th = diff(L, theta(t))
lhs_th = diff(diff(L, theta_dot), t)

motion_r = solve(Eq(lhs_r, rhs_r), r_dot_dot)
motion_th = solve(Eq(lhs_th, rhs_th), theta_dot_dot)

print motion_r
print motion_th
