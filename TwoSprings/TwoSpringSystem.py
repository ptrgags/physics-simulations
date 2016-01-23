from physics.vectors import Vector
from physics.System import System
from physics.objects import SpringBob, Wall

class TwoSpringSystem(System):
    def __init__(self, k1, k2, m1, m2, l1, l2, w1, w2, initial_state, history_size = 100):
        super(TwoSpringSystem, self).__init__(initial_state, history_size)
        self.k1 = k1
        self.k2 = k2
        self.m1 = m1
        self.m2 = m2

        w = max(w1, w2)
        l = l1 + l2

        self.spring1 = SpringBob(k1, m1, l1, w1, 15)
        self.spring2 = SpringBob(k2, m2, l2, w2, 15)

        wall_pos= Vector(-w / 4.0, -w * 3.0 / 2.0)
        wall_dims = Vector(w / 4.0, w * 2.0)
        self.wall = Wall(wall_pos, wall_dims, 10, right=True)

        floor_pos = Vector(0, w / 2.0)
        floor_dims = Vector(l * 2.0, w / 4.0)
        self.floor = Wall(floor_pos, floor_dims, 20, top=True)

    def motion(self, state):
        x1, v1, x2, v2 = state
        k1 = self.spring1.spring_constant
        k2 = self.spring2.spring_constant
        m1 = self.spring1.bob_mass
        m2 = self.spring2.bob_mass
        a1 = (k2 * x2 - k1 * x1 - k2 * x1) / m1
        a2 = (k2 * x1 - k2 * x2) / m2
        return Vector(v1, a1, v2, a2)

    def history_points(self, scale, state):
        x1, _, x2, _ = state
        rest_x1 = self.spring1.rest_length + self.spring1.bob_width / 2.0
        rest_x2 = (self.spring1.rest_length + self.spring1.bob_width
            + self.spring2.rest_length + self.spring2.bob_width / 2.0)
        point1 = scale * Vector(rest_x1 + x1, 0)
        point2 = scale * Vector(rest_x2 + x2, 0)
        return point1, point2

    def draw_walls(self, origin, scale, wall_color):
        self.wall.draw(origin, scale, wall_color)
        self.floor.draw(origin, scale, wall_color)

    def draw(self, origin, scale, colors):
        x1, _, x2, _ = self.state

        self.spring1.stretch = x1
        self.spring2.stretch = x2 - x1

        origin2 = scale * self.spring1.right_pos + origin

        self.spring1.draw(origin, scale, colors[0])
        self.spring2.draw(origin2, scale, colors[1])
