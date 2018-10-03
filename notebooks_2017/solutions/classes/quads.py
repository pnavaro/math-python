class Rectangle:
    def __init__(self, Lx, Ly):
        self.Lx, self.Ly = Lx, Ly
    def area(self):
        return self.Lx * self.Ly
    def __repr__(self):
        return "".join([self.Ly*"#"+'\n' for i in range(self.Lx)])

class Square(Rectangle):
    def __init__(self, L):
        self.Lx = L
        self.Ly = L

print(Rectangle(4,12))
print(Square(4))
