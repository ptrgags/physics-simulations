import fix_path
from DoublePendulumSystem import DoublePendulumSystem
from physics.vectors import Vector

#constant scalars
l1 = 1.0
m1 = 1.0
l2 = 1.0
m2 = 1.0

SCALE = 100
INITIAL_STATE = [0.9 * PI, 0.0, 0.0 * PI, 0.0]

def setup():
    global system
    size(640, 480)
    system = DoublePendulumSystem(l1, l2, m1, m2, 0.2, 0.2, INITIAL_STATE)

def draw():
    system.step()
    
    center = Vector(width/2.0, height / 2.0)
    phase_origin = center + Vector(0, -150)
    
    background(0)
    noFill()
    
    colors = [color(0, 255, 0), color(255, 255, 0)]
    
    system.draw_history(center, SCALE)
    system.draw_system(center, SCALE)
    
    system.draw_phase(phase_origin, 10, 3)
    system.draw_phase(phase_origin, 10, 3, 1)
    system.draw_phase_axes(phase_origin, 10, 3, Vector(0, TAU), Vector(-10, 10), xlabel='theta', vlabel='omega')