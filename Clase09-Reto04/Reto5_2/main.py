from paquete.Point import Point
from paquete.Line import Line
from paquete.Rectangle import Rectangle
from paquete.Triangle import Triangle
from paquete.RectangleTypes.Square import Square
from paquete.TriangleTypes.Isosceles import Isosceles
from paquete.TriangleTypes.Equilateral import Equilateral
from paquete.TriangleTypes.Scalene import Scalene
from paquete.TriangleTypes.Trirectangle import TriRectangle

def __main__():
    point_1 = Point(1, 2)
    point_2 = Point(3, 4)

    line_1 = Line(point_1, point_2)
    print(line_1)

    point_3 = Point(2, 1)
    point_4 = Point(4, 3)
    line_2 = Line(point_3, point_4)
    rectangle = Rectangle(line_1, line_2)
    print(rectangle)

    square = Square(line_1)
    print(square)

    point_5 = Point(0, 0)
    point_6 = Point(0, 3)
    point_7 = Point(4, 0)
    line_3 = Line(point_5, point_6)
    line_4 = Line(point_6, point_7)
    line_5 = Line(point_7, point_5)
    triangle = Triangle(line_3, line_4, line_5)
    print(triangle)

    right_triangle = TriRectangle(line_3, line_4, line_5)
    print(right_triangle)

if __name__ == "__main__":
    __main__()
