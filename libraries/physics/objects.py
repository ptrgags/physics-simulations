class Block(object):
    '''
    Defines a rectangular block
    '''
    def __init__(self, position, dimensions, mass=None):
        self.position = position
        self.dimensions = dimensions
        self.mass = mass

    @property
    def center(self):
        return self.position

    @property
    def right(self):
        w, h = self.dimensions
        return self.position + [w / 2.0, 0]

    def draw(self, scale=1.0):
        x, y = scale * (self.position - 0.5 * self.dimensions)
        w, h = scale * self.dimensions
        rect(x, y, w, h)
        point(x, y)
