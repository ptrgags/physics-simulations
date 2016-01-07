k = 5
m = 0.5

h = 0.01

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
    x *= 100

    if len(past) < 1000:
        past.append(x)
    centerX, centerY = center
    
    background(0)
    noFill()
    
    stroke(255, 0, 0)
    for pastX in past:
        point(centerX + pastX, centerY)
    stroke(255)
    
    line (centerX - 200, centerY + 10, centerX + 100, centerY + 10)
    line (centerX - 200, centerY - 50, centerX - 200, centerY + 10)
    line (centerX - 200, centerY, centerX + x - 10, centerY)    
    rect(centerX + x - 10, centerY - 10, 20, 20)