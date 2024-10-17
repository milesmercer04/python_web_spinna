
from math import pi, sqrt

class Circle:
    def __init__(self, x, y, r):
        if r < 0:
            raise ValueError("r must be a non-negative value.")
        self._x = x
        self._y = y
        self._r = r

    def area(self):
        return pi * self._r ** 2

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def r(self):
        return self._r

class Line:
    def __init__(self, x_1, y_1, x_2, y_2):
        self._x_1 = x_1
        self._y_1 = y_1
        self._x_2 = x_2
        self._y_2 = y_2

    def length(self):
        return sqrt((self._x_2 - self._x_1) ** 2 + (self._y_2 - self._y_1) ** 2)

    @property
    def x_1(self):
        return self._x_1

    @property
    def y_1(self):
        return self._y_1

    @property
    def x_2(self):
        return self._x_2

    @property
    def y_2(self):
        return self._y_2

def objects_intercect(object_1, object_2):
    if isinstance(object_1, Line) and isinstance(object_2, Line):
        return lines_intercect(object_1, object_2)
    elif isinstance(object_1, Line) and isinstance(object_2, Circle):
        pass
    elif isinstance(object_1, Circle) and isinstance(object_2, Line):
        pass
    elif isinstance(object_1, Circle) and isinstance(object_2, Circle):
        return circles_intersect(object_1, object_2)
    else:
        raise ValueError("object_1 and object_2 must both be of types Line or Circle.")

def lines_intercect(line_1, line_2):
    if not isinstance(line_1, Line) or not isinstance(line_2, Line):
        raise ValueError("line_1 and line_2 must both be of type Line.")

    m_1 = (line_1.y_2() - line_1.y_1()) / (line_1.x_2() - line_1.x_1())
    # y = mx + b
    # b = y - mx
    b_1 = line_1.y_1() - m_1 * line_1.x_1()

    m_2 = (line_2.y_2() - line_2.y_1()) / (line_2.x_2() - line_2.x_1())
    b_2 = line_2.y_1() - m_2 * line_2.x_1()

    # check for parallel and identical lines
    if m_1 == m_2:
        if b_1 == b_2:
            # lines identical, do segments overlap?
            if line_1.x_1() <= line_2.x_1() and line_2.x_1() <= line_1.x_2() or line_1.x_1() <= line_2.x_2() and line_2.x_2() <= line_1.x_2() or line_1.x_2() <= line_2.x_1() and line_2.x_1() <= line_1.x_1() or line_1.x_2() <= line_2.x_2() and line_2.x_2() <= line_1.x_1():
                return True
            else:
                return False
        else:
            return False

    ### Calculate the theoretical point of intersection for the two non-parallel lines
    # y_1 = m_1 * x_1 + b_1
    # y_2 = m_2 * x_2 + b_2
    # Suppose y_1 = y_2
    # then m_1 * x_1 + b_1 = m_2 * x_2 + b_2
    # Suppose also x_1 = x_2
    # then m_1 * x_1 + b_1 = m_2 * x_1 + b_2
    # then b_1 - b_2 = m_2 * x_1 - m_1 * x_1
    # then b_1 - b_2 = x_1 * (m_2 - m_1)
    # then x_1 = (b_1 - b_2) / (m_2 - m_1)
    intersection_x = (b_1 - b_2) / (m_2 - m_1)

    ### Verify that the two line segments contain the x-value of the theoretical intersection
    if line_1.x_1() <= intersection_x and intersection_x <= line_1.x_2() or line_1.x_2() <= intersection_x and intersection_x <= line_1.x_1():
        if line_2.x_1() <= intersection_x and intersection_x <= line_2.x_2() or line_2.x_2() <= intersection_x and intersection_x <= line_2.x_1():
            return True
        else:
            return False
    else:
        return False
    
def circles_intersect(circle_1, circle_2):
    if not isinstance(circle_1, Circle) or not isinstance(circle_2, Circle):
        raise ValueError("circle_1 and circle_2 must both be of type Circle.")
    
    # Create a Line object to represent the path between the circle's centres
    origin_line = Line(circle_1.x(), circle_1.y(), circle_2.x(), circle_2.y())

    if origin_line.length() <= (circle_1.r() + circle_2.r()):
        return True
    else:
        return False

def line_intersects_circle(line, circle):
    pass
