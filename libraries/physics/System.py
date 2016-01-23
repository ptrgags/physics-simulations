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

    def step(self):
        self.state = next(self.simulation)

    def motion(self, state):
        raise NotImplementedError
