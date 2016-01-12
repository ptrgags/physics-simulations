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
    size(640, 480)
    system = SpringSystem(k, m, l, w, INITIAL_STATE)
    
def draw():
    system.step()
    
    center = Vector(width/2.0, height / 2.0)
    origin = center + SCALE * Vector(-2.5, 0)
    
    background(0)
    noFill()
    stroke(255, 0, 0)
    system.draw_history(origin, SCALE)
    stroke(255)
    system.draw(origin, SCALE)