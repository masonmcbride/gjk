import math

class Shape:
    def __init__(self, vertices):
        # vertices is a list of Points
        self.vertices = vertices
        self.num_points = len(vertices)

    @property
    def center(self):
        return sum(self.vertices)/self.num_points

    def __getitem__(self, key):
        return self.vertices[key]

class Point:

    # This point class is just for GJK hence why z is default 0
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point(x, y, z)
    
    def __radd__(self, other):
        x = self.x + other
        y = self.y + other
        z = self.z + other
        return Point(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Point(x, y, z)

    def __rsub__(self, other):
        x = other - self.x
        y = other - self.y
        z = other - self.z
        return Point(x, y, z)


    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z
        return Point(x, y, z)

    def __truediv__(self, other):
        x = self.x / other
        y = self.y / other
        z = self.z / other
        return Point(x, y, z)

    def __neg__(self):
        return Point(-self.x, -self.y, -self.z)

    def __repr__(self):
        return f'Point(x:{self.x}, y:{self.y}, z:{self.z})'

ORIGIN = Point(0,0,0)

def normalize(point):
    sx = point.x ** 2
    sy = point.y ** 2
    sz = point.z ** 2
    norm = math.sqrt(sx + sy + sz)
    x = point.x / norm
    y = point.y / norm
    z = point.z / norm
    return Point(x, y, z)

def dot(a: Point, b: Point):
    # This is JUST for dotting 3D vectors
    # shape (3,1)
    x = a.x * b.x
    y = a.y * b.y
    z = a.z * b.z
    return x + y + z
    
def tripleProduct(a: Point, b: Point, c: Point):
    # This is JUST triple product for 3D vectors
    ac = dot(a, c)
    bc = dot(b, c)
    
    x = b.x * ac - a.x * bc
    y = b.y * ac - a.y * bc
    return Point(x, y)


