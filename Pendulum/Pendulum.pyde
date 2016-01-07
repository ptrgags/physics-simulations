import time

g = 9.807
l = 1.0
m = 1.0

h = 0.01

def pendulum_motion(vec): 
    theta, omega = vec
    return [omega, -g / l * sin(theta)]

def vscale(r, vec):
    return [r * x for x in vec]

def vadd(*args):
    return [sum(tuple) for tuple in zip(*args)]

#Angular position and velocity
pendulum_state = [0.9 * PI, 0.0]

def runge_kutta(f, state):
    a = f(state)
    b = f(vadd(state, vscale(h / 2.0, a)))
    c = f(vadd(state, vscale(h / 2.0, b)))
    d = f(vadd(state, vscale(h, b)))
          
    #Apply the weights h/6 * (a + 2b + 2c + d)
    a = vscale(h / 6.0, a)
    b = vscale(h / 3.0, b)
    c = vscale(h / 3.0, c)
    d = vscale(h / 6.0, d)
    return vadd(state, a, b, c, d)

def to_rect(r, theta):
    return [r * cos(theta), r * sin(theta)]

def circle(x, y, radius):
    ellipse(x, y, radius, radius)

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