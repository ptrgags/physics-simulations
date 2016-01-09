import fix_path
from physics.graphics import horizontal_spring
from physics.rungekutta import runge_kutta
from physics.vectors import vadd, vscale

#Constant scalars:
k = 5.0 #Spring constant in N/m
m = 0.5 #mass of bob in kg
l = 1.0 #Rest length of spring in m
w = 0.4 #Width of bob in m

SCALE = 100  #Simulation scale in pixels/m
COILS = 10   #Number of coils for display purposes
HISTORY_SIZE = 1000 #history points to save

#Coordinates [x, y] in m -> pixels
ORIGIN = vscale(SCALE, [-2.5, 0]) #Position of the origin measured from center of screen
OFFSET_SPRING_REST = vscale(SCALE, [l, 0]) #offset of the spring at rest measured from ORIGIN.
OFFSET_HISTORY = vadd(ORIGIN, vscale(SCALE, [l + w / 2.0, 0])) #history point origin measured from center of screen

#Dimensions [x, y, w, h] in m -> pixels
RECT_WALL = vscale(SCALE, [0, -w, 0, 2.0 * w]) #dimensions of wall measured from ORIGIN  
RECT_SPRING_REST = vscale(SCALE, [0, -w / 2.0, l, w]) #dimensions of spring at rest measured from ORIGIN
RECT_BOB = vscale(SCALE, [0, -w / 2.0, w, w]) #dimensions of bob measured from OFFSET_BOB

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
    global spring_state
    spring_state = runge_kutta(spring_motion, spring_state)
    x, v = spring_state

    x_delta = vscale(SCALE, [x, 0])
    x_area_delta = [0, 0] + x_delta

    spring_box = vadd(RECT_SPRING_REST, x_area_delta) + [COILS]
    bob_offset = vadd(OFFSET_SPRING_REST, x_delta)

    if len(past) < HISTORY_SIZE:
        past.append(x)
    centerX, centerY = center
    
    background(0)
    noFill()
    
    stroke(255, 0, 0)
    pushMatrix()
    translate(*center)
    translate(*OFFSET_HISTORY)
    for pastX in past:
        point(pastX * SCALE, 0)
    popMatrix()
    
    stroke(255)
    pushMatrix()
    translate(*center)
    translate(*ORIGIN)
    rect(*RECT_WALL)
    horizontal_spring(*spring_box)
    translate(*bob_offset)    
    rect(*RECT_BOB)
    popMatrix()