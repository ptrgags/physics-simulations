from vectors import Vector
from rungekutta import RungeKuttaSimulation

class System(object):
    '''
    Abstract base class for all physics systems
    that use RungeKuttaSimulation under the cover
    '''
    def __init__(self, initial_state, history_size = 1000):
        self.simulation = RungeKuttaSimulation(self.motion, initial_state, history_size=history_size)
        self.state = initial_state
        self.history_color = color(255, 0, 0)
        self.wall_color = color(255, 255, 255)
        self.colors = [
            color(0, 255, 0),
            color(255, 255, 0),
            color(255, 0, 255),
            color(0, 255, 255)
        ]
        self.paused = False

    def step(self):
        if not self.paused:
            self.state = next(self.simulation)

    def toggle_paused(self):
        self.paused = not self.paused

    def motion(self, state):
        raise NotImplementedError

    def history_points(self, scale, state):
        raise NotImplementedError

    def draw_history(self, origin, scale):
        pushMatrix()
        translate(*origin)
        stroke(self.history_color)
        for state in self.simulation.history:
            for p in self.history_points(scale, state):
                point(*p)
        popMatrix()

    def draw_phase(self, origin, x_scale, v_scale, component = 0):
        pushMatrix()
        translate(*origin)
        stroke(self.colors[component])
        index = component * 2
        past = [state[index:index + 2] for state in self.simulation.history]
        for x, v in past:
            point(x_scale * x, v_scale * v)
        popMatrix()

    def draw_phase_axes(self, origin, x_scale, v_scale, x_limits, v_limits, c=color(255, 255, 255),
                        xlabel='x', vlabel='v'):
        pushMatrix()
        translate(*origin)
        stroke(c)
        #X axis
        x_min, x_max = x_limits * x_scale
        line(x_min, 0, x_max, 0)
        text(xlabel, x_max, 10)

        #V axis
        v_min, v_max = v_limits * v_scale
        line(0, v_min, 0, v_max)
        text(vlabel, 10, -v_max)
        popMatrix()

    def draw_walls(self, origin, scale, wall_color):
        pass

    def draw(self, origin, scale, colors):
        raise NotImplementedError

    def draw_system(self, origin, scale):
        noFill()
        self.draw_walls(origin, scale, self.wall_color)
        self.draw(origin, scale, self.colors)
