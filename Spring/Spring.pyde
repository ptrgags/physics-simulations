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

def draw_spring(x, y, w, h, coils):
    dx = w * 1.0 / coils
    for i in xrange(coils):
        line(x + i * dx, y, x + (i + 0.5) * dx, y + h)
        line(x + (i + 0.5) * dx, y + h, x + (i + 1) * dx, y)

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
    draw_spring(centerX + wallX * SCALE, centerY - w / 2.0 * SCALE, (l + x) * SCALE, w * SCALE, 11)
    rect(centerX + (wallX + l + x) * SCALE, centerY - w / 2.0 * SCALE, w * SCALE, w * SCALE)