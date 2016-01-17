import fix_path
from PendulumSystem import PendulumSystem
from physics.vectors import Vector

#constant scalars
l = 1.0
m = 1.0

SCALE = 100
INITIAL_STATE = [0.9 * PI, 0.0]

def setup():
    global system
    size(640, 480)
    system = PendulumSystem(l, m, 20, INITIAL_STATE)

def draw():
    system.step()
    
    center = Vector(width/2.0, height / 2.0)
    phase_origin = center + Vector(0, -150)
    
    background(0)
    noFill()
    
    colors = [color(0, 255, 0)]
    
    system.draw_history(center, SCALE)
    system.draw(center, SCALE, colors)
    
    system.draw_phase(phase_origin, 10, 3, colors[0])
    system.draw_phase_axes(phase_origin, 10, 3, Vector(-4, 4), Vector(-10, 10))