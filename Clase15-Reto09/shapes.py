from validatable import Validatable

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
    # Valida si start y end son instancias de Point
    Validatable._validate_instances(
      [start, end], Point, "Start and end must be Point instances"
      )
    
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

        if len(self._vertices) < 3:
            raise ValueError("A shape must have at least 3 vertices")
        if len(self._edges) < 3:
            raise ValueError("A shape must have at least 3 edges")

    @property
    def is_regular(self):
        """Getter para is_regular"""
        return self._is_regular
    
    @is_regular.setter
    def is_regular(self, value):
        """Setter para is_regular"""
        if not isinstance(value, bool):
            raise TypeError("is_regular must be a boolean")
        self._is_regular = value

    @property
    def vertices(self):
        """Getter para vertices"""
        return self._vertices

    @property
    def edges(self):
        """Getter para edges"""
        return self._edges
    
    @classmethod
    def define_shape(cls, is_regular: bool, *args):
        """Método de clase para definir la forma"""
        return cls(is_regular, *args)

    def __str__(self):
        return (f"Shape(V: {len(self.vertices)}, E: {len(self.edges)}, Regular: {self.is_regular})")


# Clase rectángulo
class Rectangle(Shape):
  def __init__(self, line_1: "Line", line_2: "Line", is_regular: bool = False):
    # Valida si line_1 y line_2 son instancias de Line
    Validatable._validate_instances(
      [line_1, line_2], Line, "Arguments must be Line instances"
      )
    
    self.line_1 = line_1
    self.line_2 = line_2
    line_3 = Line(line_1.start, line_2.end)
    line_4 = Line(line_2.start, line_1.end)

    super().__init__(
      is_regular, 
      line_1.start, line_1.end, line_2.start, line_2.end,
      line_1, line_2, line_3, line_4
      )

  def __str__(self):
    return (
      f"Rectangle(P: {2 * (self.line_1.length + self.line_2.length):.2f}, "
      f"A: {self.line_1.length * self.line_2.length:.2f}) "
      f"{super().__str__()}"
    )

# Clase cuadrado
class Square(Rectangle):
  def __init__(self, line: "Line"):
    # Valida si line es una instancia de Line
    Validatable._validate_instances(
      [line], Line, "Argument must be a Line instance"
      )
    super().__init__(line, line, is_regular=True)

  def __str__(self):
    return f"Square - {super().__str__()}"

# Clase triángulo
class Triangle(Shape):
  def __init__(self, line_1: "Line", line_2: "Line",
    line_3: "Line", is_regular: bool = False
    ):
    # Valida si line_1, line_2 y line_3 son instancias de Line
    Validatable._validate_instances(
      [line_1, line_2, line_3], Line, "Arguments must be Line instances"
      )

    super().__init__(
      is_regular, line_1.start, line_1.end, line_2.start, line_2.end, 
      line_3.start, line_3.end, line_1, line_2, line_3
    )
    self.line_1 = line_1
    self.line_2 = line_2
    self.line_3 = line_3

  def __str__(self):
    perimeter = self.line_1.length + self.line_2.length + self.line_3.length
    s = perimeter / 2
    area = (
      s * (s - self.line_1.length) * (s - self.line_2.length) * (s - self.line_3.length))** 0.5
    return f"Triangle(P: {perimeter:.2f}, A: {area:.2f}) {super().__str__()}"

# Clase triángulo Isósceles
class Isosceles(Triangle):
  def __init__(self, line_1: "Line", line_2: "Line", line_3: "Line"):
    super().__init__(line_1, line_2, line_3, is_regular=False)

    # Lanzar una excepción si las líneas no forman un triángulo isósceles
    if not (line_1.length == line_2.length or 
            line_1.length == line_3.length or 
            line_2.length == line_3.length
            ):
      raise ValueError("Lines do not form an isosceles triangle")

  def __str__(self):
    return f"Isosceles - {super().__str__()}"

# Clase triángulo Equilátero
class Equilateral(Triangle):
  def __init__(self, line_1: "Line", line_2: "Line", line_3: "Line"):
    super().__init__(line_1, line_2, line_3, is_regular=True)
    # Lanzar una excepción si las líneas no forman un triángulo equilátero
    if not (line_1.length == line_2.length == line_3.length):
      raise ValueError("Lines do not form an equilateral triangle")

  def __str__(self):
    return f"Equilateral - {super().__str__()}"

# Clase triángulo Escaleno
class Scalene(Triangle):
  def __init__(self, line_1: "Line", line_2: "Line", line_3: "Line"):
    super().__init__(line_1, line_2, line_3, is_regular=False)

  def __str__(self):
    return f"Scalene - {super().__str__()}"

# Clase triángulo Rectángulo
class TriRectangle(Triangle):
  def __init__(self, line_1: "Line", line_2: "Line", line_3: "Line"):
    super().__init__(line_1, line_2, line_3, is_regular=False)
    # Lanza una excepción si las líneas no forman un triángulo rectángulo
    if not self._is_right_triangle():
      raise ValueError("Lines do not form a right triangle")

  def _is_right_triangle(self):
    lengths = sorted(
      [self.line_1.length, self.line_2.length, self.line_3.length]
      )
    return abs(lengths[0]**2 + lengths[1]**2 - lengths[2]**2) < 1e-9

  def __str__(self):
    return f"TriRectangle - {super().__str__()}"
