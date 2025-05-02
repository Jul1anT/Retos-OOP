import time
from shapes import Point, Line, Shape, Rectangle, Square, Triangle, TriRectangle

# Decorador para medir el tiempo de ejecución
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Execution time: {time.time() - start:.2f} seconds")
        return result
    return wrapper

@timer # Decorador para medir el tiempo de ejecución
# Función principal
def main():
    print("\n| Shapes |")

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

    square = square.define_shape(line_2)
    print(square)  

    print("")

if __name__ == "__main__":
    main()
