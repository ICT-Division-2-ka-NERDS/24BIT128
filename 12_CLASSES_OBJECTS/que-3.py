import math
class Solid():
    def __init__(self, length = 0, breadth = 0, height = 0, radius = 0):
        self.l = length
        self.b = breadth
        self.h = height
        self.r = radius
        
    def cuboid_volume(self):
        return self.l * self.b * self.h
    
    def cuboid_area(self):
        return 2 * ((self.l * self.b) + (self.l * self.h) + (self.b * self.h))
    
    def sphere_volume(self):
        return (4 * math.pi * self.r**3) / 3
    
    def sphere_area(self):
        return 4 * math.pi * self.r**2
    
    def cylinder_volume(self):
        return math.pi * self.r**2 * self.h
    
    def cylinder_area(self):
        return (2 * math.pi * self.r**2) + (2 * math.pi * self.r * self.h)
    
    def cone_volume(self):
        return (math.pi * self.r**2 * self.h) / 3
    
    def cone_area(self):
        return (math.pi * self.r**2) + (math.pi * self.r * self.l)
    
    def display(self, *data):
        for ele in data:
            print(f"{ele.__name__} is : {ele()}")
        
s1 = Solid(length = 10, breadth = 20 , height = 15)
s1.display(s1.cuboid_volume, s1.cuboid_area)
s2 = Solid(radius = 1, length = 5)
s2.display(s2.cone_area)