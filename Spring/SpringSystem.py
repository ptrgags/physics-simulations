from physics.graphics import horizontal_spring, vertical_wall, horizontal_wall
from physics.rungekutta import RungeKuttaSimulation
from physics.vectors import Vector

class SpringSystem(object):
    def __init__(self, k, m, l, w, initial_state):
        self.k = k
        self.m = m
        self.simulation = RungeKuttaSimulation(self.motion, initial_state, history_size = 100)
        self.state = initial_state
        
        self.wall_pos= Vector(-w / 4.0, -w * 3.0 / 2.0)
        self.wall_dims = Vector(w / 4.0, w * 2.0)
        self.floor_pos = Vector(0, w / 2.0)
        self.floor_dims = Vector(l * 2.0, w / 4.0)
        self.spring_pos = Vector(0, -w / 2.0)
        self.spring_dims_rest = Vector(l, w)
        self.bob_pos_rest = Vector(l, -w / 2.0)
        self.bob_dims = Vector(w, w)
        self.history_origin = Vector(l + w / 2.0, 0)
                               
    def step(self):
        self.state = next(self.simulation)
    
    def motion(self, state):
        x, v = state
        return Vector(v, -self.k / self.m * x)
    
    def draw_history(self, origin, scale):
        pushMatrix()
        translate(*origin)
        for past_x, _ in self.simulation.history:
            point(*(scale * (self.history_origin + [past_x, 0])))
        popMatrix()
    
    def draw_phase(self, origin, x_scale, v_scale):
        pushMatrix()
        translate(*origin)
        for past_x, past_v in self.simulation.history:
            point(x_scale * past_x, v_scale * past_v)
        popMatrix()
    
    def draw_phase_axes(self, origin, x_scale, v_scale, x_limits, v_limits):
        pushMatrix()
        translate(*origin)
        x_min, x_max = x_limits * x_scale
        line(x_min, 0, x_max, 0)
        text("x", x_max, 10)
        v_min, v_max = v_limits * v_scale
        line(0, v_min, 0, v_max)
        text("v", 10, -v_max)
        popMatrix()

    def draw(self, origin, scale):
        springX, _ = self.state
        
        pushMatrix()
        translate(*origin)
        #Wall
        x, y = self.wall_pos * scale
        w, h = self.wall_dims * scale
        vertical_wall(x, y, w, h, 10, right=True)
        
        #Floor
        x, y = self.floor_pos * scale
        w, h = self.floor_dims * scale
        horizontal_wall(x, y, w, h, 20, top=True)
        
        #Spring
        x, y = self.spring_pos * scale
        w, h = (self.spring_dims_rest + [springX, 0]) * scale
        horizontal_spring(x, y, w, h, 10)
    
        #Bob
        x, y = (self.bob_pos_rest + [springX, 0]) * scale
        w, h = self.bob_dims * scale
        rect(x, y, w, h)        
        popMatrix()