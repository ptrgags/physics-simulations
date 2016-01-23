from graphics import circle
from graphics import horizontal_spring
from graphics import horizontal_wall, vertical_wall
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
        l = scale * self.length
        r = scale * self.bob_radius
        rotate(-self.__origin_theta - self.angle)
        line(0, 0, l, 0)
        circle(l, 0, r)
        popMatrix()

class SpringBob(object):
    def __init__(self, k, m, l, w, coils):
        self.spring_constant = k
        self.bob_mass = m
        self.bob_width = w
        self.rest_length = l
        self.coils = coils

    @property
    def length(self):
        return self.rest_length + self.stretch

    @property
    def right_pos(self):
        right = self.rest_length + self.stretch + self.bob_width
        return Vector(right, 0)

    def draw(self, origin, scale, color):
        pushMatrix()
        translate(*origin)
        stroke(color)
        l = scale * self.length
        w = scale * self.bob_width
        top = -w / 2.0
        horizontal_spring(0, top, l, w, self.coils)
        rect(l, top, w, w)
        popMatrix()

class Wall(object):
    def __init__(self, pos, dimensions, lines, left=False, right=False, top=False, bottom=False):
        self.pos = pos
        self.dims = dimensions
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.lines = lines

    def draw(self, origin, scale, color):
        pushMatrix()
        translate(*origin)
        stroke(color)
        x, y = scale * self.pos
        w, h = scale * self.dims
        if self.top or self.bottom:
            horizontal_wall(x, y, w, h, self.lines, top=self.top,
                bottom=self.bottom)
        elif self.left or self.right:
            vertical_wall(x, y, w, h, self.lines, left=self.left,
                right=self.right)
        popMatrix()
