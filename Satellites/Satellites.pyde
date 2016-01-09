import fix_path
from physics.graphics import circle
from physics.rungekutta import runge_kutta
from physics.vectors import vadd, vscale

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

def to_rect(r, theta):
    return [r * cos(theta), r * sin(theta)]
    
def setup():
    global center
    global earth_state
    global past
    past = []
    size(640, 480)
    center = [width / 2.0, height / 2.0]
    earth_state = [d, 0, 0, omega_earth]
    
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