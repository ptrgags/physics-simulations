import fix_path
from SatelliteSystem import SatelliteSystem
from physics.vectors import Vector

m_sun = 1
m_earth = 1
d = 1

#Angular Speed of earth's orbit
omega_earth = 1

SCALE = 150
INITIAL_STATE = [d, 0, 0, omega_earth]
print INITIAL_STATE

def setup():
    global system
    global center
    global phase_origin
    
    size(640, 480)
    system = SatelliteSystem(m_earth, INITIAL_STATE)
    
    center = Vector(width / 2.0, height / 2.0)
    phase_origin = center + Vector(-200, -150)

def draw():
    system.step()
    background(0)
    
    system.draw_history(center, SCALE)
    system.draw_system(center, SCALE)
 
    system.draw_phase(phase_origin, 10, 3, 1)
    system.draw_phase_axes(phase_origin, 10, 3, Vector(0, TAU), Vector(-10, 10), xlabel='theta', vlabel='omega') 