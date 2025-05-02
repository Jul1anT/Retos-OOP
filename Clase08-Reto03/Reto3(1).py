# Clase punto
class Point:
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y
  def __str__(self):
    return f"Point created at ({self.x}, {self.y})"

# Clase línea
class Line:
  def __init__(self, start: "Point", end: "Point"):
    self.start = start
    self.end = end

  # Calcular la longitud de la línea
  def compute_length(self):
    self.length = (
      (self.end.x - self.start.x)**2 + (self.end.y - self.start.y)**2
      )**0.5

  # Calcular la pendiente de la línea
  def compute_slope(self):
    self.slope = (self.end.y - self.start.y) / (self.end.x - self.start.x)
  
  # Calcular el cruce con el eje vertical
  def compute_vertical_cross(self):
    vertical_cross = self.start.y - (self.slope*self.start.x)
    return vertical_cross

  # Calcular el cruce con el eje horizontal
  def compute_horizontal_cross(self):
    horizontal_cross = self.compute_vertical_cross() / self.slope
    return horizontal_cross
  
class Rectangle:
  def __init__(self, line_1: "Line", line_2: "Line"):
    self.line_1 = line_1
    self.line_2 = line_2
    self.line_3 = Line(self.line_1.start, self.line_2.start)
    self.line_4 = Line(self.line_1.end, self.line_2.end)

  def __str__(self):
    return (f"Rectangle created with points: "
            f"({self.line_1.start.x}, {self.line_1.start.y}), "
            f"({self.line_1.end.x}, {self.line_1.end.y}), "
            f"({self.line_2.start.x}, {self.line_2.start.y}), "
            f"({self.line_2.end.x}, {self.line_2.end.y})")

def __main__():
  # Crear puntos
  point_1 = Point(1, 2)
  point_2 = Point(3, 4)
  print(point_1)  # Imprimir el primer punto
  print(point_2)  # Imprimir el segundo punto

  line_1 = Line(point_1, point_2)
  # Calcular la longitud de la línea
  line_1.compute_length()
  print(f"Length of the line: {line_1.length}")
  # Calcular la pendiente de la línea
  line_1.compute_slope()
  print(f"Slope of the line: {line_1.slope}")

  # Calcular el cruce con el eje vertical
  vertical_cross = line_1.compute_vertical_cross()
  print(f"Vertical cross of the line: {vertical_cross}")
  # Calcular el cruce con el eje horizontal
  horizontal_cross = line_1.compute_horizontal_cross()
  print(f"Horizontal cross of the line: {horizontal_cross}")

  # Crear un rectángulo
  point_3 = Point(2, 1)
  point_4 = Point(4, 3)
  line_2 = Line(point_3, point_4)
  rectangle = Rectangle(line_1, line_2)
  print(rectangle)

if __main__() == "__main__":
  __main__()