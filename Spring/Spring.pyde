import fix_path
from SpringSystem import SpringSystem
from physics.vectors import Vector, make_rect

#Constant scalars:
k = 10.0 #Spring constant in N/m          Should be a property of a Spring object
m = 0.5 #mass of bob in kg               Should be a property of the bob block
l = 2.0 #Rest length of spring in m      Should be a property of the Spring object
w = 0.4 #Width of bob in m               Should be a property of the bob Block

SCALE = 100  #Simulation scale in pixels/m
COILS = 10   #Number of coils for display purposes   Should be a property of the Spring object

INITIAL_STATE = [-0.5, 0]

def setup():
    global system
    global origin
    global phase_origin
    
    size(640, 480)
    system = SpringSystem(k, m, l, w, INITIAL_STATE)
    
    #Positions on the screen
    center = Vector(width / 2.0, height / 2.0)
    origin = center + SCALE * Vector(-2.5, 0)
    phase_origin = center + Vector(0, -150)
    
def draw():
    system.step()
    
    background(0)
    
    system.draw_history(origin, SCALE)
    system.draw_system(origin, SCALE)
    
    system.draw_phase(phase_origin, 100, 20)
    system.draw_phase_axes(phase_origin, 100, 20, Vector(-0.6, 0.6), Vector(-3, 3))

def keyReleased():
    if key == ' ':
        system.toggle_paused()