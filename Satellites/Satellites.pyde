import time

m_sun = 1
m_earth = 1
d = 1
G = 1
#Speed of earth's orbit
v_earth = 1 #m/sec
omega_earth = v_earth / d

h = 0.01

def orbit_motion(vec):
    r, r_dot, theta, theta_dot = vec
    return [
        r_dot,
        r * theta_dot * theta_dot - G * m_sun / r / r,
        theta_dot,
        0
    ]

def vscale(r, vec):
    return [r * x for x in vec]

def vadd(*args):
    return [sum(tuple) for tuple in zip(*args)]

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
    global earth_state
    global past
    past = []
    size(640, 480)
    center = [width / 2.0, height / 2.0]
    earth_state = [d, -0.000001, 0, omega_earth]
    
def draw():
    global earth_state
    
    earth_state = runge_kutta(orbit_motion, earth_state)
    r, r_dot, theta, theta_dot = earth_state
    earthX, earthY = vscale(200, to_rect(r, theta))
    if len(past) < 1000:
        past.append((earthX, earthY))
    
    centerX, centerY = center
    
    background(0)
    noFill()
    
    stroke(255, 0, 0)
    for x, y in past:
        point(centerX + x, centerY - y)
    stroke(255)
    
    circle(centerX, centerY, 100) #Sun    
    circle(centerX + earthX, centerY - earthY, 50) #Earth