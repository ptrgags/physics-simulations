def vscale(r, vec):
    return [r * x for x in vec]

def vadd(*args):
    return [sum(tuple) for tuple in zip(*args)]

class Vector(object):
    def __init__(self, *components):
        self.components = components

    def __getitem__(self, i):
        return self.components[i]

    def __setitem__(self, i, value):
        self.components[i] = value

    def __len__(self):
        return len(self.components)

    def __iter__(self):
        return iter(self.components)

    def __str__(self):
        return str(tuple(self.components))

    def __repr__(self):
        return "Vector({})".format(self.components)

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be the same size!")
        return Vector(*[a + b for a, b in zip(self, other)])

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.components = [a + b for a, b in zip(self, other)]
        return self

    def __sub__(self, other):
        return self + -1.0 * other

    def __rsub__(self, other):
        return other + -1.0 * self

    def __isub__(self, other):
        self += -1.0 * other
        return self

    def __mul__(self, scale):
        return Vector(*[scale * x for x in self])

    def __rmul__(self, scale):
        return self * scale

    def __imul__(self, scale):
        self.components = [scale * x for x in self]
        return self

#Not sure what to do with these:
def make_rect(position, dimensions):
    return Vector(*(list(position) + list(dimensions)))

def make_circle(position, radius, scale):
    return Vector(*(list(position) + [radius]))

def make_line(position1, position2):
    return Vector(*(list(position) + list(dimensions)))
