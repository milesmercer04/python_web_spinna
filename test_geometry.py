from pytest import *
from math import *
import geometry as ge

def test_init_circle():
    test_circle = ge.Circle(0, 0, 1)
    assert test_circle.x() == 0
    assert test_circle.y() == 0
    assert test_circle.r() == 1

def test_circle_area():
    test_circle = ge.Circle(0, 0, 1)
    assert test_circle.area() == pi

def test_init_line():
    test_line = ge.Line(0, 0, 1, 1)
    assert test_line.x_1() == 0
    assert test_line.y_1() == 0
    assert test_line.x_2() == 1
    assert test_line.y_2() == 1

def test_line_length():
    test_line = ge.Line(0, 0, 1, 1)
    assert test_line.length() == sqrt(2)



