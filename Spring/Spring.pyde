import fix_path
from physics.graphics import horizontal_spring
from physics.rungekutta import runge_kutta
from physics.vectors import Vector, make_rect
from physics.objects import Block

#Constant scalars:
k = 5.0 #Spring constant in N/m
m = 0.5 #mass of bob in kg
l = 1.0 #Rest length of spring in m
w = 0.4 #Width of bob in m

SCALE = 100  #Simulation scale in pixels/m
COILS = 10   #Number of coils for display purposes
HISTORY_SIZE = 1000 #history points to save

#Positions [x, y] in m
POS_ORIGIN = Vector(-2.5, 0) #Origin coords from center of screen
POS_WALL = Vector(-w / 8.0, 0) #Position of the wall
POS_SPRING_REST = Vector(0, - w / 2.0) #position of the top left corner of spring at rest measured from origin
POS_SPRING_REST_RIGHT = POS_SPRING_REST + [l, 0] #position of the top right corner of spring measured from right
POS_HISTORY = POS_ORIGIN + [l + w / 2.0, 0] #bob history origin mesaured from origin

#Dimensions [w, h] in m
DIMS_WALL = Vector(w / 4.0, 2.0 * w) #Dimensions of wall
DIMS_SPRING_REST = Vector(l, w) #Dimensions of spring at rest
DIMS_BOB = Vector(w, w) #Dimensions of bob

#Objects
wall = Block(POS_WALL, DIMS_WALL)

def spring_motion(vec):
    x, v = vec
    return [v, -k / m * x]

def setup():
    global center
    global past
    global spring_state
    past = []
    size(640, 480)
    center = [width / 2.0, height / 2.0]
    spring_state = [-0.5, 0]
    
def draw():
    pass
    global spring_state
    spring_state = runge_kutta(spring_motion, spring_state)
    x, v = spring_state

    pos_delta = Vector(x, 0)
    
    rect_spring = make_rect(POS_SPRING_REST, DIMS_SPRING_REST + pos_delta)
    spring_params = list(SCALE * rect_spring) + [COILS]
    
    bob_offset = POS_SPRING_REST_RIGHT + pos_delta
    rect_bob = make_rect(bob_offset, DIMS_BOB)

    if len(past) < HISTORY_SIZE:
        past.append(x)
    centerX, centerY = center
    
    background(0)
    noFill()
    
    stroke(255, 0, 0)
    pushMatrix()
    translate(*center)
    translate(*(SCALE * POS_HISTORY))
    for pastX in past:
        point(pastX * SCALE, 0)
    popMatrix()
    
    stroke(255)
    pushMatrix()
    translate(*center)
    translate(*(SCALE * POS_ORIGIN))
    wall.draw(SCALE)
    horizontal_spring(*spring_params)
    translate(*bob_offset)    
    rect(*(SCALE * rect_bob))
    popMatrix()