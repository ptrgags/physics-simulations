from physics.graphics import circle
from physics.System import System
from physics.vectors import Vector, polar2rect
from physics.constants import g

from physics.objects import PendulumBob

class DoublePendulumSystem(System):
    def __init__(self, l1, l2, m1, m2, bob_r1, bob_r2, initial_state, history_size = 100):
        super(DoublePendulumSystem, self).__init__(initial_state, history_size)

        self.pendulum1 = PendulumBob(l1, m1, bob_r1)
        self.pendulum2 = PendulumBob(l2, m2, bob_r2)

        #These are in POLAR coordinates [r, theta]
        #self.history_origin1 = Vector(l1, -HALF_PI)
        #self.history_origin2 = Vector(l2, -HALF_PI)

    def motion(self, state):
        theta1, theta_dot1, theta2, theta_dot2 = state

        #Localize these for convenience
        m1 = self.pendulum1.mass
        m2 = self.pendulum2.mass
        l1 = self.pendulum1.length
        l2 = self.pendulum2.length

        #convenience substitutions
        M = m1 + m2
        m2_half = m2 / 2.0

        #Do trig stuff once
        a = theta1 - theta2
        cos_a = cos(a)
        sin_a = sin(a)
        cos_sq_a = cos_a * cos_a
        b = theta1 - 2.0 * theta2
        sin_b = sin(b)
        th1_dot_sq = theta_dot1 * theta_dot1
        th2_dot_sq = theta_dot2 * theta_dot2
        sin_th1 = sin(theta1)
        sin_th2 = sin(theta2)

        #denominators for the two equations are very similar
        denom = (M - m2 * cos_sq_a)
        denom1 = -denom * l1
        denom2 = denom * l2

        #Numerator for angular accel 1:
        term1 = l1 * m2 * th1_dot_sq * sin_a * cos_a
        term2 = th2_dot_sq * l2 * m2 * sin_a
        term3 = g * m1 * sin_th1
        term4 = g * m2_half * sin_th1
        term5 = g * m2_half * sin_b
        num1 = term1 + term2 + term3 + term4 + term5

        #Numerator for angular accel 2:
        term1 = -th1_dot_sq * l1 * sin_a
        term2 = g * sin_th2
        half_one = - M * (term1 + term2)
        term1 = th2_dot_sq * l2 * m2 * sin_a
        term2 = g * M * sin_th1
        half_two = (term1 + term2) * cos_a
        num2 = half_one + half_two

        #Finally, we have our angular acceleration values!
        #Good luck debugging this if the formula is wrong...
        alpha1 = num1 / denom1
        alpha2 = num2 / denom2

        return Vector(theta_dot1, alpha1, theta_dot2, alpha2)

    def draw_history(self, origin, scale, c=color(255, 0, 0)):
        pushMatrix()
        translate(*origin)
        stroke(c)
        for state in self.simulation.history:
            for p in self.history_points(scale, state):
                point(*p)
        popMatrix()

    def history_points(self, scale, state):
        theta1, _, theta2, _ = state
        polar1 = [self.pendulum1.length, theta1 - HALF_PI]
        polar2 = [self.pendulum2.length, theta2 - HALF_PI]
        point1 = scale * polar2rect(polar1, flip_y = True)
        point2 = scale * polar2rect(polar2, flip_y = True)
        return point1, point1 + point2

    def draw_phase(self, origin, x_scale, v_scale, c, component = 0):
        pushMatrix()
        translate(*origin)
        stroke(c)
        index = component * 2
        past = [state[index:index + 2] for state in self.simulation.history]
        for x, v in past:
            x = (x + HALF_PI) % TAU
            point(x_scale * x, v_scale * v)
        popMatrix()

    def draw_phase_axes(self, origin, x_scale, v_scale, x_limits, v_limits, c=color(255, 255, 255)):
        pushMatrix()
        translate(*origin)
        stroke(c)
        x_min, x_max = x_limits * x_scale
        line(x_min, 0, x_max, 0)
        text("theta", x_max, 10)
        v_min, v_max = v_limits *- v_scale
        line(0, v_min, 0, v_max)
        text("omega", 10, -v_max)
        popMatrix()

    def draw(self, origin, scale, colors):
        theta1, _, theta2, _ = self.state
        self.pendulum1.angle = theta1
        self.pendulum2.angle = theta2

        #Origin of second bob depends on first bob
        origin2 = scale * self.pendulum1.bob_pos + origin

        self.pendulum1.draw(origin, scale, colors[0])
        self.pendulum2.draw(origin2, scale, colors[1])
