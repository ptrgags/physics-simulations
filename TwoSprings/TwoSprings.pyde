import fix_path
from TwoSpringSystem import TwoSpringSystem
from physics.vectors import Vector

k1 = 5.0
m1 = 0.5
k2 = 5.0
m2 = 0.5
l1 = 1.0
l2 = 1.0
w1 = 0.4
w2 = 0.4

SCALE=100
INITIAL_STATE = [-0.5, 0.0, -0.5, 0.0]

def setup():
    global system
    global origin
    global phase_origin
    
    size(640, 480)
    system = TwoSpringSystem(k1, k2, m1, m2, l1, l2, w1, w2, INITIAL_STATE, 200)
    
    center = Vector(width / 2.0, height / 2.0)
    origin = center + SCALE * Vector(-2.5, 0)
    phase_origin = center + Vector(0, -150)

def draw():
    system.step()
    
    background(0)
    
    system.draw_history(origin, SCALE)
    system.draw_system(origin, SCALE)
    
    system.draw_phase(phase_origin, 100, 20)
    system.draw_phase(phase_origin, 100, 20, 1)
    system.draw_phase_axes(phase_origin, 100, 20, Vector(-0.6, 0.6), Vector(-3, 3))