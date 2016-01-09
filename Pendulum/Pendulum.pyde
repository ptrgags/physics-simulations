import fix_path
from physics.graphics import circle
from physics.rungekutta import runge_kutta
from physics.vectors import vadd, vscale

g = 9.807
l = 1.0
m = 1.0

h = 0.01


def pendulum_motion(vec): 
    theta, omega = vec
    return [omega, -g / l * sin(theta)]

#Angular position and velocity
pendulum_state = [0.9 * PI, 0.0]

def to_rect(r, theta):
    return [r * cos(theta), r * sin(theta)]

def setup():
    global center
    global past 
    past = []
    size(640, 480)
    center = [width / 2.0, height / 2.0]

def draw():
    global pendulum_state
    pendulum_state = runge_kutta(pendulum_motion, pendulum_state)
    theta, omega = pendulum_state
    bobX, bobY = vscale(100, to_rect(l, theta - PI / 2))
    if len(past) < 1000:
        past.append((bobX, bobY))
    centerX, centerY = center
    
    background(0)
    noFill()
    
    stroke(255, 0, 0)
    for x, y in past:
        point(centerX + x, centerY - y)
    stroke(255)
    
    line(centerX, centerY, centerX + bobX, centerY - bobY)
    circle(centerX + bobX, centerY - bobY, m * 20)