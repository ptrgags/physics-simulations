from sympy import symbols
from sympy import Function
from sympy import diff
from sympy import Eq
from sympy import cos
from sympy import sin
from sympy import solve

# constants and variables
l, m, g, t = symbols('l m g t')

# Theta and its derivatives
theta = Function('theta')
theta_dot = diff(theta(t), t)
theta_dot_dot = diff(theta_dot, t)

# positions in polar coordinates
x = l * sin(theta(t))
y = -l * cos(theta(t))

# velocities in polar coordinates
x_dot = diff(x, t)
y_dot = diff(y, t)

# Energy of the system in polar coordinates
V = m * g * y
T = m / 2 * theta_dot ** 2 * l ** 2
L = T - V

rhs = diff(L, theta(t))
lhs = diff(diff(L, theta_dot), t)

motion = solve(Eq(lhs, rhs), theta_dot_dot)
print motion