from graphics import circle
from vectors import Vector

class PendulumBob(object):
    def __init__(self, l, m, r, origin_theta=-HALF_PI):
        self.length = l
        self.mass = m
        self.bob_radius = r
        self.angle = 0
        self.__origin_theta = origin_theta

    @property
    def bob_pos(self):
        x = self.length * sin(self.angle)
        y = self.length * cos(self.angle)
        return Vector(x, y)

    def draw(self, origin, scale, color):
        pushMatrix()
        translate(*origin)
        stroke(color)
        rotate(-self.__origin_theta - self.angle)
        line(0, 0, scale * self.length, 0)
        circle(scale * self.length, 0, self.bob_radius)
        popMatrix()
