# Class 
class MenuItem:
  def __init__(self, name: str, price: float, size: str):
    self._name = name
    self._price = price
    self._size = size

  def get_name(self):
    return self._name
  def set_name(self, name: str):

    self._name = name
  def get_price(self):
    return self._price
  def set_price(self, price: float):
    self._price = price

  def get_size(self):
    return self._size
  def set_size(self, size: str):
    self._size = size

  def __str__(self):
    return f"{self._name} - ${self._price:.2f} ({self._size})"

# Subclass for Beverages
class Beverage(MenuItem):
  def __init__(self, name: str, price: float, size: str):
    super().__init__(name, price, size)
    self._size = size  # e.g., Small, Medium, Large

# Subclass for Appetizers
class Appetizer(MenuItem):
  def __init__(self, name: str, price: float, portion_size: str):
    super().__init__(name, price, portion_size)
    self._portion_size = portion_size  # e.g., 6 pieces, 1 plate

  def get_portion_size(self):
    return self._portion_size
  def set_portion_size(self, portion_size: str):
    self._portion_size = portion_size

# Subclass for Main Courses
class MainCourse(MenuItem):
  def __init__(self, name: str, price: float, size: str):
    super().__init__(name, price, size)

# Class Order
class Order:
  def __init__(self, menu_items: list):
    self._menu_items = menu_items
    self._order_items = []

  def add_item(self, index: int, amount: int):
    self._order_items.append((self._menu_items[index], amount))

  def calculate_total_price(self):
    subtotal = 0
    main_course_in_order = any(isinstance(item, MainCourse) for item, _ in self._order_items)
    for item, amount in self._order_items:
      if main_course_in_order and isinstance(item, Beverage):
        subtotal += item.get_price() * amount * 0.8  # 20% discount on beverages
      else:
        subtotal += item.get_price() * amount
    return subtotal

  def check_order(self):
    self._subtotal: float = 0
    self._index: int = 0
    self._amount: int = 0
    self._decision: str = "n"
    self._counter: int = 0

    print("\nWelcome to the restaurant!")
    value: int = 10
    print(f"If the order has more than 3 items, it will receive a {value}% discount:")

    while True:
      self._index = int(input("Type the index of the item: "))
      while True:
        if self._index < 0 or self._index >= len(self._menu_items):
          self._index = int(input("Type a valid index: "))
        else:
          break
      self._amount = int(input("Type the amount of the item: "))
      while True:
        if self._amount < 0:
          self._amount = int(input("Type a valid amount: "))
        else:
          break

      self.add_item(self._index, self._amount)
      self._counter += self._amount
      self._decision = input("Do you want to add more items? (y/n): ")
      if not self._decision == "y":
        break

    total_price = self.calculate_total_price()
    if self._counter >= 3:
      total_price *= 0.9  # 10% discount for orders with 3 or more items
    return total_price

# Class PaymentMethod
class PaymentMethod:
  def __init__(self):
    pass

  def pay(self, amount):
    raise NotImplementedError("Subclasses must implement pay()")

class Card(PaymentMethod):
  def __init__(self, number, cvv):
    super().__init__()
    self.number = number
    self.cvv = cvv

  def pay(self, amount):
    print(f"Paying {amount} with card {self.number[-4:]}")

class Cash(PaymentMethod):
  def __init__(self, amount_given):
    super().__init__()
    self.amount_given = amount_given

  def pay(self, amount):
    if self.amount_given >= amount:
      print(f"Payment made in cash. Change: {self.amount_given - amount}")
    else:
      print(
        f"Insufficient funds. Missing {amount - self.amount_given} to complete the payment."
      )

# Main function
def __main__():
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
  total_price = order.check_order()
  print(f"Order: ${total_price:.2f}")

  # Payment
  payment_method = input("Choose payment method (1 for Card, 2 for Cash): ")
  if payment_method == "1":
    card_number = input("Enter card number: ")
    card_cvv = input("Enter card CVV: ")
    payment = Card(card_number, card_cvv)
  elif payment_method == "2":
    cash_amount = float(input("Enter cash amount: "))
    payment = Cash(cash_amount)
  else:
    print("Invalid payment method")
    return

  payment.pay(total_price)

# Main
if __name__ == "__main__":
  __main__()
