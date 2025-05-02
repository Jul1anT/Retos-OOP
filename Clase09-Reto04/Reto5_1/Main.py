# Clase punto
class Point:
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y

  def __str__(self):
    return f"({self.x}, {self.y})"

# Clase línea
class Line:
  def __init__(self, start: "Point", end: "Point"):
    self.start = start
    self.end = end
    self.length = ((end.x - start.x) ** 2 + (end.y - start.y) ** 2) ** 0.5

  def __str__(self):
    return f"Line({self.start}, {self.end}, {self.length:.2f})"

# Clase figura
class Shape:
  def __init__(self, is_regular: bool, *args):
    self._is_regular = is_regular
    self._vertices = [el for el in args if isinstance(el, Point)]
    self._edges = [el for el in args if isinstance(el, Line)]

  def __str__(self):
    return f"Shape(V: {len(self._vertices)}, E: {len(self._edges)}, Regular: {self._is_regular})"

# Clase rectángulo
class Rectangle(Shape):
  def __init__(self, line_1: "Line", line_2: "Line", is_regular: bool = False):
    super().__init__(
      is_regular, line_1.start, line_1.end, line_2.start, line_2.end, line_1, line_2
    )
    self.line_1 = line_1
    self.line_2 = line_2

  def __str__(self):
    return (
    f"Rectangle(P: {2 * (self.line_1.length + self.line_2.length):.2f}, "
    f"A: {self.line_1.length * self.line_2.length:.2f}) "
    f"{super().__str__()}"
  )

# Clase cuadrado
class Square(Rectangle):
  def __init__(self, line: "Line"):
    super().__init__(line, line, is_regular=True)

  def __str__(self):
    return f"Square - {super().__str__()}"

# Clase triángulo
class Triangle(Shape):
  def __init__(self, line_1: "Line", line_2: "Line", line_3: "Line", is_regular: bool = False):
    super().__init__(
    is_regular, 
    line_1.start, line_1.end, 
    line_2.start, line_2.end, 
    line_3.start, line_3.end, 
    line_1, line_2, line_3
    )
    self.line_1 = line_1
    self.line_2 = line_2
    self.line_3 = line_3

  def __str__(self):
    perimeter = self.line_1.length + self.line_2.length + self.line_3.length
    s = perimeter / 2
    area = (
      s * (s - self.line_1.length) * (s - self.line_2.length) * (s - self.line_3.length)
    ) ** 0.5
    return f"Triangle(P: {perimeter:.2f}, A: {area:.2f}) {super().__str__()}"

# Clases triángulo Isósceles
class Isosceles(Triangle):
  def __init__(self, line_1: "Line", line_2: "Line", line_3: "Line"):
    super().__init__(line_1, line_2, line_3, is_regular=False)
    if not (
    line_1.length == line_2.length or 
    line_1.length == line_3.length or 
    line_2.length == line_3.length
    ):
      raise ValueError("Lines do not form an isosceles triangle")
  def __str__(self):
    return f"Isosceles - {super().__str__()}"

# Clases triángulo Equilátero
class Equilateral(Triangle):
  def __init__(self, line_1: "Line", line_2: "Line", line_3: "Line"):
    super().__init__(line_1, line_2, line_3, is_regular=True)
    if not (line_1.length == line_2.length == line_3.length):
      raise ValueError("Lines do not form an equilateral triangle")
  def __str__(self):
    return f"Equilateral - {super().__str__()}"

# Clases triángulo Escaleno
class Scalene(Triangle):
  def __init__(self, line_1: "Line", line_2: "Line", line_3: "Line"):
    super().__init__(line_1, line_2, line_3, is_regular=False)
  def __str__(self):
    return f"Scalene - {super().__str__()}"

# Clase triángulo Rectángulo
class TriRectangle(Triangle):
  def __init__(self, line_1: "Line", line_2: "Line", line_3: "Line"):
    super().__init__(line_1, line_2, line_3, is_regular=False)
    if not self._is_right_triangle():
      raise ValueError("Lines do not form a right triangle")

  def _is_right_triangle(self):
    lengths = sorted([self.line_1.length, self.line_2.length, self.line_3.length])
    return abs(lengths[0]**2 + lengths[1]**2 - lengths[2]**2) < 1e-9
  
  def __str__(self):
    return f"TriRectangle - {super().__str__()}"

# Main
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
