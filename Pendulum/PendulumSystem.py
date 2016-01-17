from physics.graphics import circle
from physics.rungekutta import RungeKuttaSimulation
from physics.vectors import Vector, polar2rect
from physics.constants import g

class PendulumSystem(object):
    def __init__(self, l, m, bob_r, initial_state, history_size = 100):
        self.m = m
        self.simulation = RungeKuttaSimulation(self.motion, initial_state, history_size = history_size)
        self.state = initial_state
        
        self.bob_size = bob_r
        self.l = l
        
        #These are in POLAR coordinates [r, theta]
        self.bob_pos_rest = Vector(l, -HALF_PI)
        
        self.history_origin = self.bob_pos_rest
        
    def step(self):
        self.state = next(self.simulation)
    
    def motion(self, state):
        theta, theta_dot = state
        return Vector(theta_dot, -g / self.l * sin(theta))

    def draw_history(self, origin, scale, c=color(255, 0, 0)):
        pushMatrix()
        translate(*origin)
        stroke(c)
        for past_theta, _ in self.simulation.history:
            polar = self.history_origin + [0, past_theta]
            point(*(scale * polar2rect(polar, flip_y = True)))
        popMatrix()
        
    def draw_phase(self, origin, x_scale, v_scale, c, component = 0):
        pushMatrix()
        translate(*origin)
        stroke(c)
        index = component * 2
        past = [state[index:index + 2] for state in self.simulation.history]
        for x, v in past:
            point(x_scale * x, v_scale * v)
        popMatrix()
    
    def draw_phase_axes(self, origin, x_scale, v_scale, x_limits, v_limits, c=color(255, 255, 255)):
        pushMatrix()
        translate(*origin)
        stroke(c)
        x_min, x_max = x_limits * x_scale
        line(x_min, 0, x_max, 0)
        text("theta", x_max, 10)
        v_min, v_max = v_limits * v_scale
        line(0, v_min, 0, v_max)
        text("omega", 10, -v_max)
        popMatrix()
    
    def draw(self, origin, scale, colors):
        bob_theta, _ = self.state
        bob_delta_polar = Vector(0, bob_theta)
        
        pushMatrix()
        translate(*origin)
        stroke(colors[0])
        x, y = scale * polar2rect(bob_delta_polar + self.bob_pos_rest, flip_y = True)
        
        line(0, 0, x, y)
        circle(x, y, self.bob_size)
        popMatrix()