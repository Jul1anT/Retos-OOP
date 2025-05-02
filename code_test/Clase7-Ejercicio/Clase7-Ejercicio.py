class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return f"Point created at ({self.x}, {self.y})"

class Rectangule:
  def __init__(self, *args):
    self.bottom_left = args[0]
    self.top_right = args[1]
    self.width = self.top_right.x - self.bottom_left.x
    self.height = self.top_right.y - self.bottom_left.y
    self.center = Point(
      self.bottom_left.x + self.width / 2, self.bottom_left.y + self.height / 2
    )
    print(
      f"Rectangle ["
      f"Width: {self.width}, "
      f"Height: {self.height}, "
      f"Center: ({self.center.x}, {self.center.y})]"
    )

  def compute_perimeter(self):
    perimeter = 2 * (self.width + self.height)
    print(f"Perimeter of Rectangle: {perimeter}")
    return perimeter

  def compute_area(self):
    area = self.width * self.height
    print(f"Area of Rectangle: {area}")
    return area

  def compute_interference_point(self, point):
    # Verifica si el punto está dentro de los límites del rectángulo
    if (self.bottom_left.x <= point.x <= self.top_right.x and
        self.bottom_left.y <= point.y <= self.top_right.y):
      print(f"Point ({point.x}, {point.y}) is inside the rectangle.")
      return True
    else:
      print(f"Point ({point.x}, {point.y}) is outside the rectangle.")
      return False

class Square(Rectangule):
  pass

def __main__():
  # Crear puntos
  point_1 = Point(x=1, y=1)
  point_2 = Point(x=3, y=3)
  print(point_1)  # Imprimir el primer punto
  print(point_2)  # Imprimir el segundo punto

  # Crear el rectángulo
  rectangule = Rectangule(point_1, point_2)

  # Imprimir área y perímetro
  rectangule.compute_area()
  rectangule.compute_perimeter()

  # Verificar si un punto está dentro del rectángulo
  point_3 = Point(x=2, y=2)
  rectangule.compute_interference_point(point_3)

if __name__ == "__main__":
  __main__()
