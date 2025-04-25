import math
class Shape():
    def __init__(self, length = 0, breadth = 0, height = 0, radius = 0):
        self.l = length
        self.b = breadth
        self.h = height
        self.r = radius
        
    def rectangle_perimeter(self):
        return (self.l + self.b) * 2
    
    def rectangle_area(self):
        return self.l * self.b
    
    def circle_perimeter(self):
        return 2 * math.pi * self.r
    
    def circle_area(self):
        return math.pi * self.r**2
    
    def triangle_area(self):
        return (self.l * self.h) / 2
    
    def triangle_perimeter(self):
        return self.l + self.h + math.sqrt(self.l**2 + self.h**2)
    
    def display(self, *data):
        for ele in data:
            print(f"{ele.__name__} is : {ele()}")
        
s1 = Shape(length = 10, breadth = 20)
s1.display(s1.rectangle_area, s1.rectangle_perimeter)
s2 = Shape(length = 1, height = 1)
s2.display(s2.triangle_area,s2.triangle_perimeter)