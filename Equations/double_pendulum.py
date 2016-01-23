from sympy import symbols
from sympy import Function
from sympy import diff
from sympy import Eq
from sympy import cos
from sympy import sin
from sympy import solve
from sympy import latex

#Symbols
l1, l2 = symbols('l1 l2')
m1, m2 = symbols('m1 m2')
g, t = symbols('g t')
alpha1, alpha2 = symbols("\\theta''_1 \\theta''_2")
omega1, omega2 = symbols("\\theta'_1 \\theta'_2")
th1, th2 = symbols('theta1 theta2')

# Theta and its derivatives
theta1 = Function('theta1')
theta_dot1 = diff(theta1(t), t)
theta_dot_dot1 = diff(theta_dot1, t)
theta2 = Function('theta2')
theta_dot2 = diff(theta2(t), t)
theta_dot_dot2 = diff(theta_dot2, t)

# positions in polar coordinates
x1 = l1 * sin(theta1(t))
y1 = -l1 * cos(theta1(t))
x2 = x1 + l2 * sin(theta2(t))
y2 = y1 - l2 * cos(theta2(t))

# velocities in polar coordinates
x_dot1 = diff(x1, t)
y_dot1 = diff(y1, t)
x_dot2 = diff(x2, t)
y_dot2 = diff(y2, t)

# Energy of the system in polar coordinates
V1 = m1 * g * y1
V2 = m2 * g * y2
V = V1 + V2
T1 = m1 / 2 * (x_dot1 ** 2 + y_dot1 ** 2)
T2 = m2 / 2 * (x_dot2 ** 2 + y_dot2 ** 2)
T = T1 + T2
L = T - V

rhs1 = diff(L, theta1(t))
lhs1 = diff(diff(L, theta_dot1), t)

rhs2 = diff(L, theta2(t))
lhs2 = diff(diff(L, theta_dot2), t)
motion = solve([Eq(lhs1, rhs1), Eq(lhs2, rhs2)], [theta_dot_dot1, theta_dot_dot2])
for sym in motion:
    eqn = Eq(sym, motion[sym])
    print eqn.subs(theta_dot_dot1, alpha1)
        .subs(theta_dot_dot2, alpha2)
        .subs(theta_dot1, omega1)
        .subs(theta_dot2, omega2)
        .subs(theta1(t), th1)
        .subs(theta2(t), th2)
