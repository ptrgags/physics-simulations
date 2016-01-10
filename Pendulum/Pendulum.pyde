import fix_path
from physics.graphics import circle
from physics.rungekutta import runge_kutta
from physics.vectors import vadd, vscale

def to_rect(r, theta, flip_y = True):
    if flip_y:
        return [r * cos(theta), -r * sin(theta)]
    else:
        return [r * cos(theta), r * sin(theta)]

#constant scalars
g = 9.807
l = 1.0
m = 1.0

SCALE = 100
HISTORY_SIZE = 1000

#Coordinates [r, theta] in [m, rad]
ORIGIN_POLAR = [l, -HALF_PI] #Position of the origin measured from center of the screen

def pendulum_motion(vec): 
    theta, omega = vec
    return [omega, -g / l * sin(theta)]

def setup():
    global center
    global past 
    global pendulum_state
    past = []
    size(640, 480)
    center = [width / 2.0, height / 2.0]
    pendulum_state = [0.9 * PI, 0.0]

def draw():
    global pendulum_state
    pendulum_state = runge_kutta(pendulum_motion, pendulum_state)
    theta, omega = pendulum_state
    
    polar_delta = [0, theta]
    
    bob_polar = vadd(ORIGIN_POLAR, polar_delta)
    bob_position = vscale(SCALE, to_rect(*bob_polar)) #Relative to center
    bob_line = [0, 0] + bob_position
    bob_circle = bob_position + [20 * m]
 
    if len(past) < HISTORY_SIZE:
        past.append(bob_polar)
    centerX, centerY = center
    
    background(0)
    noFill()
    
    stroke(255, 0, 0)
    pushMatrix()
    translate(*center)
    for coords in past:
        point(*vscale(SCALE, to_rect(*coords)))
    popMatrix()
    
    stroke(255)
    pushMatrix()
    translate(*center)
    line(*bob_line)
    circle(*bob_circle)
    popMatrix()