
from math import *

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        return pi * self.r ** 2
    
    def x(self):
        return self.x
    
    def y(self):
        return self.y
    
    def r(self):
        return self.r
    
class Line:
    def __init__(self, x_1, y_1, x_2, y_2):
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2

    def length(self):
        return sqrt((self.x_2 - self.x_1) ** 2 + (self.y_2 - self.y_1) ** 2)
    
    def x_1(self):
        return self.x_1
    
    def y_1(self):
        return self.y_1
    
    def x_2(self):
        return self.x_2
    
    def y_2(self):
        return self.y_2
    
def objects_intercept(object_1, object_2):
    if isinstance(object_1, Line) and isinstance(object_2, Line):
        pass
    elif isinstance(object_1, Line) and isinstance(object_2, Circle):
        pass
    elif isinstance(object_1, Circle) and isinstance(object_2, Line):
        pass
    elif isinstance(object_1, Circle) and isinstance(object_2, Circle):
        pass
    else:
        raise ValueError("object_1 and object_2 must both be of types Line or Circle.")


