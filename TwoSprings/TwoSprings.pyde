import fix_path
from physics.graphics import horizontal_spring
from physics.rungekutta import runge_kutta
from physics.vectors import vadd, vscale

k1 = 5.0
m1 = 0.5
k2 = 5.0
m2 = 0.5
l1 = 1.0
l2 = 1.0
w1 = 0.4
w2 = 0.4

h = 0.01
wallX = -2.5

SCALE=100

def spring_motion(vec):
    x1, v1, x2, v2 = vec
    a1 = (k2 * x2 - k1 * x1 - k2 * x1) / m1
    a2 = (k2 * x1 - k2 * x2) / m2
    return [v1, a1, v2, a2]

def setup():
    global center
    global past
    global spring_state
    past = []
    size(640, 480)
    center = [width / 2.0, height / 2.0]
    spring_state = [-0.5, 0, -0.5, 0]

def draw():
    global spring_state
    spring_state = runge_kutta(spring_motion, spring_state)
    x1, v1, x2, v2 = spring_state

    if len(past) < 1000:
        past.append((x1, x2))
    centerX, centerY = center

    background(0)
    noFill()

    stroke(255, 0, 0)
    for pastX1, pastX2 in past:
        point(centerX + (wallX + l1 + pastX1 + w1 / 2.0) * SCALE, centerY)
        point(centerX + (wallX + l1 + pastX1 + w1 + l2 + pastX2 + w2 / 2.0) * SCALE, centerY)
    stroke(255)

    #Wall
    line(centerX + wallX * SCALE, centerY - 50, centerX + wallX * SCALE, centerY + 50)

    #Spring + Bob 1
    horizontal_spring(centerX + wallX * SCALE, centerY - w1 / 2.0 * SCALE, (l1 + x1) * SCALE, w1 * SCALE, 10)
    rect(centerX + (wallX + l1 + x1) * SCALE, centerY - w1 / 2.0 * SCALE, w1 * SCALE, w1 * SCALE)

    #Spring + Bob 2
    horizontal_spring(centerX + (wallX + l1 + x1 + w1) * SCALE, centerY - w2 / 2.0 * SCALE, (l2 + x2) * SCALE, w2 * SCALE, 10)
    rect(centerX + (wallX + l1 + x1 + w1 + l2 + x2) * SCALE, centerY - w2 / 2.0 * SCALE, w2 * SCALE, w2 * SCALE)