import fix_path
from physics.graphics import horizontal_spring
from physics.rungekutta import runge_kutta
from physics.vectors import vadd, vscale

k = 5.0
m = 0.5
l = 1.0
w = 0.4

h = 0.01

wallX = -2.5
SCALE = 100

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
    spring_state = [-0.005, 0]
    
def draw():
    global spring_state
    spring_state = runge_kutta(spring_motion, spring_state)
    x, v = spring_state
    x *= 100

    if len(past) < 1000:
        past.append(x)
    centerX, centerY = center
    
    background(0)
    noFill()
    
    stroke(255, 0, 0)
    for pastX in past:
        point(centerX + (wallX + l + pastX + w / 2.0) * SCALE, centerY)
    stroke(255)
    
    line (centerX + wallX * SCALE, centerY - 50, centerX + wallX * SCALE, centerY + 50)
    horizontal_spring(centerX + wallX * SCALE, centerY - w / 2.0 * SCALE, (l + x) * SCALE, w * SCALE, 10)
    rect(centerX + (wallX + l + x) * SCALE, centerY - w / 2.0 * SCALE, w * SCALE, w * SCALE)