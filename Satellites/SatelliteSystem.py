from physics.vectors import Vector, polar2rect
from physics.constants import g
from physics.System import System
from physics.graphics import circle

class SatelliteSystem(System):
    def __init__(self, m, initial_state, history_size = 100):
        super(SatelliteSystem, self).__init__(initial_state, history_size)
        self.m = m

    def motion(self, state):
        r, r_dot, theta, theta_dot = state
        r_accel = r * theta_dot * theta_dot - self.m / r / r
        theta_accel = 0
        return Vector(r_dot, r_accel, theta_dot, theta_accel)

    def history_points(self, scale, state):
        r, _, theta, _ = state
        polar = Vector(r, theta)
        p = scale * polar2rect(polar, flip_y = True)
        return [p]
    
    def draw_phase(self, origin, x_scale, v_scale, component = 0):
        '''
        This version of draw_phase is special, we need to
        modulo the angles to keep them within the bounds of the graph
        '''
        pushMatrix()
        translate(*origin)
        stroke(self.colors[component])
        index = component * 2
        past = [state[index:index + 2] for state in self.simulation.history]
        for x, v in past:
            x = (x + HALF_PI) % TAU
            point(x_scale * x, -v_scale * v)
        popMatrix()

    def draw(self, origin, scale, colors):
        r, _, theta, _ = self.state
        pushMatrix()
        translate(*origin)
        stroke(colors[1])
        circle(0, 0, 30)
        
        polar = Vector(r, theta)
        x, y = scale * polar2rect(polar, flip_y = True)
        stroke(colors[0])
        circle(x, y, 30)
        popMatrix()