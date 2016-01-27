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
    global center
    global phase_origin
    
    size(640, 480)
    system = PendulumSystem(l, m, 0.2, INITIAL_STATE)

    #positions on the screen
    center = Vector(width / 2.0, height / 2.0)
    phase_origin = center + Vector(0, -150)

def draw():
    system.step()
    
    background(0)
    
    system.draw_history(center, SCALE)
    system.draw_system(center, SCALE)
    
    system.draw_phase(phase_origin, 10, 3)
    system.draw_phase_axes(phase_origin, 10, 3, Vector(-4, 4), Vector(-10, 10), xlabel='theta', vlabel='omega')

def keyReleased():
    if key == ' ':
        system.toggle_paused()