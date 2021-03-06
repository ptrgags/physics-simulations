def circle(x, y, radius):
    '''
    Draw a circle. Why doesn't Processing have this??
    x -- x coordinate of the circle's center
    y -- y coordinate of the circle's center
    radius -- radius of circle
    '''
    ellipse(x, y, radius, radius)

def vertical_wall(x, y, w, h, lines, left=False, right=False):
    '''
    Draw a wall with lines like in physics diagrams
    x, y -- position of the top left corner
    w, h -- dimensions of the wall (bounding box)
    left -- if True, draw a line on the left side
    right -- if True, draw a line on the left side
    '''
    dy = float(h) / lines
    pushMatrix()
    translate(x, y)
    for i in xrange(lines):
        line(0, i * dy, w, (i + 0.5) * dy)
    if left:
        line(0, 0, 0, h)
    if right:
        line(w, 0, w, h)
    popMatrix()

def horizontal_wall(x, y, w, h, lines, top=False, bottom=False):
    '''
    Draw a wall with lines like in physics diagrams
    x, y -- position of the top left corner
    w, h -- dimensions of the wall (bounding box)
    top -- if True, draw a line on the left side
    bottom -- if True, draw a line on the left side
    '''
    dx = float(w) / lines
    pushMatrix()
    translate(x, y)
    for i in xrange(lines):
        line(i * dx, 0, (i + 0.5) * dx, h)
    if top:
        line(0, 0, w, 0)
    if bottom:
        line(0, h, w, h)
    popMatrix()

def horizontal_spring(x, y, w, h, coils):
    '''
    Draw a spring on the screen horizontally
    x -- the x coordinate of the top left corner
    y -- the y component of the top left corner
    w -- width of the spring
    h -- height of the spring
    coils -- the number of coils to draw for this spring
    '''
    dx = float(w) / coils
    pushMatrix()
    translate(x, y)
    for i in xrange(coils):
        line(i * dx, 0, (i + 0.5) * dx, h)
        line((i + 0.5) * dx, h, (i + 1) * dx, 0)
    popMatrix()

def vertical_spring(x, y, w, h, coils):
    '''
    Draw a spring on the screen vertically
    x -- the x coordinate of the top left corner
    y -- the y component of the top left corner
    w -- width of the spring
    h -- height of the spring
    coils -- the number of coils to draw for this spring
    '''
    dy = float(h) / coils
    for i in xrange(coils):
        line(x, y + i * dy, x + w, y + (i + 0.5) * dy)
        line(x + w, y + (i + 0.5) * dy, x, y + (i + 1) * dy)
