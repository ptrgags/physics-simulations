from physics.vectors import Vector, polar2rect
from physics.constants import g
from physics.System import System
from physics.objects import PendulumBob

class PendulumSystem(System):
    def __init__(self, l, m, bob_r, initial_state, history_size = 100):
        super(PendulumSystem, self).__init__(initial_state, history_size)
        self.pendulum = PendulumBob(l, m, bob_r)
        self.history_origin = Vector(l, -HALF_PI)

    def motion(self, state):
        theta, theta_dot = state
        return Vector(theta_dot, -g / self.pendulum.length * sin(theta))

    def history_points(self, scale, state):
        theta, _ = state
        polar = [self.pendulum.length, theta - HALF_PI]
        p = scale * polar2rect(polar, flip_y = True)
        return [p]

    def draw(self, origin, scale, colors):
        bob_theta, _ = self.state
        self.pendulum.angle = bob_theta
        self.pendulum.draw(origin, scale, colors[0])
