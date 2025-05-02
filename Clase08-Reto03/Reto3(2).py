# Class base Item 
class MenuItem:
  def __init__(self, name: str, price: float, size: str):
    self.name = name
    self.price = price
    self.size = size
  def __str__(self):
    return f"{self.name} - ${self.price:.2f} ({self.size})"
  
# Class Beverage, Appetizer and MainCourse
class Beverage(MenuItem):
    pass
class Appetizer(MenuItem):
    pass
class MainCourse(MenuItem):
    pass

# Class Order
class Order:
  def __init__(self, menu_item: "MenuItem"):
    self.menu_item = menu_item

# Check the order
  def check_order(self):
    self.subtotal: float = 0
    self.index: int = 0
    self.amount: int = 0
    self.desicion: str = "n"
    self.counter: int = 0

    print("\nWelcome to the restaurant!")
    value: int = 10
    print(f"If the order has more than 3 items, it will receive a {value}% discount:")
    
    while True:
      self.index = int(input("Type the index of the item: "))
      while True:
        if self.index < 0 or self.index >= len(self.menu_item):
          self.index = int(input("Type a valid index: "))
        else:
          break
      self.amount = int(input("Type the amount of the item: "))
      while True:
        if self.amount < 0:
          self.amount = int(input("Type a valid amount: "))
        else:
          break

      self.subtotal += self.menu_item[self.index].price * self.amount
      self.counter += self.amount
      self.desicion = input("Do you want to add more items? (y/n): ")
      if not self.desicion == "y":
        break
    if self.counter >= 3:
      self.subtotal *= 0.9
    return f"Order: {self.subtotal:.2f}"

# Main function
def __main__():
  # Sample menu items
  menu_items = [
    Beverage("Cappuccino", 3.99, "Small"),
    Beverage("Latte", 4.50, "Medium"),
    Beverage("Iced Tea", 2.99, "Large"),
    Beverage("Smoothie", 5.49, "Large"),
    Appetizer("Nachos", 7.99, "1 plate"),
    Appetizer("Spring Rolls", 5.99, "6 pieces"),
    Appetizer("Garlic Bread", 4.99, "4 slices"),
    MainCourse("Grilled Chicken", 12.99, "Juicy chicken with herbs"),
    MainCourse("Steak", 15.99, "Tender beef steak with sides"),
    MainCourse("Pasta Primavera", 10.99, "Pasta with fresh vegetables"),
  ]
  # Display the menu
  for index, item in enumerate(menu_items):
    print(f"{index}. {item}")

  # Create an order
  order = Order(menu_items)
  print(order.check_order())

# Call the main function
if __name__() == "__main__":
  __main__()


