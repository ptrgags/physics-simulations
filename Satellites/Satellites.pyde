import fix_path
from SatelliteSystem import SatelliteSystem
from physics.vectors import Vector

#Note: this simulation is NOT to scale, and the two 
#planets here do not interact with each other, even though
#with the choice of constants, they should interact.

G = 2
m_sun = 1
m_earth = 1
d = 1

#Angular Speed of earth's orbit
omega_earth = 1

SCALE = 150
INITIAL_STATE = [d, 0, 0, omega_earth]
INITIAL_STATE2 = [d, -1, 5.0 * PI / 6.0, 0.90]

def setup():
    global system
    global system2
    global center
    global phase_origin
    
    size(640, 480)
    
    system = SatelliteSystem(G, m_sun, INITIAL_STATE)
    
    system2 = SatelliteSystem(G, m_sun, INITIAL_STATE2)
    system2.colors = [color(0, 255, 0), color(0, 255, 255)]
    
    center = Vector(width / 2.0, height / 2.0)
    phase_origin = center + Vector(-250, -150)

def draw():
    system.step()
    system2.step()
    background(0)
    
    system.draw_history(center, SCALE)
    system.draw_system(center, SCALE)
 
    system2.draw_history(center, SCALE)
    system2.draw_system(center, SCALE)
    
    system.draw_phase(phase_origin, 10, 3, 1)
    system2.draw_phase(phase_origin, 10, 3, 1)
    system.draw_phase_axes(phase_origin, 10, 3, Vector(0, TAU), Vector(-20, 20), xlabel='theta', vlabel='omega') 
    
def keyReleased():
    if key == ' ':
        system.toggle_paused()
        system2.toggle_paused()