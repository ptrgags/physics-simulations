from physics.System import System
from physics.vectors import Vector
from physics.objects import SpringBob, Wall

class SpringSystem(System):
    def __init__(self, k, m, l, w, initial_state, history_size = 100):
        super(SpringSystem, self).__init__(initial_state, history_size)

        self.spring = SpringBob(k, m, l, w, 15)

        wall_pos= Vector(-w / 4.0, -w * 3.0 / 2.0)
        wall_dims = Vector(w / 4.0, w * 2.0)
        self.wall = Wall(wall_pos, wall_dims, 10, right=True)

        floor_pos = Vector(0, w / 2.0)
        floor_dims = Vector(l * 2.0, w / 4.0)
        self.floor = Wall(floor_pos, floor_dims, 20, top=True)

    def motion(self, state):
        x, v = state
        k = self.spring.spring_constant
        m = self.spring.bob_mass
        return Vector(v, -k / m * x)

    def history_points(self, scale, state):
        x, _ = state
        rest_x = self.spring.rest_length + self.spring.bob_width / 2.0
        x += rest_x
        return [Vector(x * scale, 0)]

    def draw_walls(self, origin, scale, wall_color):
        self.wall.draw(origin, scale, wall_color)
        self.floor.draw(origin, scale, wall_color)

    def draw(self, origin, scale, colors):
        x, _ = self.state
        self.spring.stretch = x
        self.spring.draw(origin, scale, colors[0])
