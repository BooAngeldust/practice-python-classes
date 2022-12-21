class Vector3:
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        return f"({self.x},{self.y},{self.z})"

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        return Vector3(self.x / other.x, self.y / other.y, self.z / other.z)

    def __eq__(self,other):
        if isinstance(other, tuple):
            return self.x == other[0] and self.y == other[1] and self.z == other[2]
        
        return self.x == other.x and self.y == other.y and self.z == other.z

class Vector2:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"({self.x},{self.y})"
    
    def __add__(self,other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self,other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other.x, self.y * other.y)

    def __truediv__(self,other):
        return Vector2(self.x / self.x, self.y / self.y)

    def __eq__(self,other):
        if isinstance(other,tuple):
            return self.x == other[0] and self.y == other[1]
        
        return self.x == other.x and self.y == other.y
