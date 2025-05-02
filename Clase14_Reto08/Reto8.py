import json
from collections import namedtuple, deque
from typing import List, Dict, Iterator

# Define una namedtuple para organizar categorías de menú
MenuCategory = namedtuple("MenuCategory", ["name", "items"])

# Clase base para ítems del menú
class MenuItem:
    def __init__(self, name: str, price: float, size: str):
        self.name = name
        self.price = price
        self.size = size

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.size})"

    def to_dict(self):
        """Convierte un ítem del menú a un diccionario."""
        return {"name": self.name, "price": self.price, "size": self.size}

    @classmethod
    def from_dict(cls, data: Dict):
        """Crea un ítem del menú desde un diccionario."""
        return cls(data["name"], data["price"], data["size"])

# Clase para gestionar el menú con funciones de modificación
class MenuManager:
    def __init__(self):
        self.menu = {"Beverages": [], "Appetizers": [], "Main Courses": []}
    
    def add_item(self, category: str, item: MenuItem):
        if category in self.menu:
            self.menu[category].append(item.to_dict())
        else:
            print(f"Category '{category}' does not exist.")
    
    def update_item(self, category: str, item_name: str, new_item: MenuItem):
        if category in self.menu:
            for i, item in enumerate(self.menu[category]):
                if item["name"] == item_name:
                    self.menu[category][i] = new_item.to_dict()
                    break
            else:
                print(f"Item '{item_name}' not found in category '{category}'.")
        else:
            print(f"Category '{category}' does not exist.")
    
    def delete_item(self, category: str, item_name: str):
        if category in self.menu:
            self.menu[category] = [item for item in self.menu[category] if item["name"] != item_name]
        else:
            print(f"Category '{category}' does not exist.")
    
    def save_menu(self, filename: str):
        with open(filename, "w") as file:
            json.dump(self.menu, file, indent=4)
        print(f"Menu saved to {filename}.")
    
    def load_menu(self, filename: str):
        with open(filename, "r") as file:
            self.menu = json.load(file)
        print(f"Menu loaded from {filename}.")

# Clase para manejar órdenes en una cola FIFO
class OrderManager:
    def __init__(self):
        self.orders = deque()
    
    def add_order(self, order):
        self.orders.append(order)
        print(f"Order added: {order}")
    
    def process_order(self):
        if self.orders:
            completed_order = self.orders.popleft()
            print(f"Processing order: {completed_order}")
        else:
            print("No orders to process.")
    
    def show_orders(self):
        if self.orders:
            print("\nPending Orders:")
            for i, order in enumerate(self.orders):
                print(f"{i + 1}. {order}")
        else:
            print("No pending orders.")

# Clase iterable para manejar una orden
class OrderIterator:
    def __init__(self, order_items: List[tuple]):
        self.order_items = order_items
        self.index = 0
    
    def __iter__(self) -> Iterator:
        return self
    
    def __next__(self):
        if self.index < len(self.order_items):
            item = self.order_items[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

# Clase para manejar una orden individual
class Order:
    def __init__(self, menu_items: List[MenuItem]):
        self.menu_items = menu_items
        self.items = []
    
    def check_order(self):
        subtotal = 0
        counter = 0

        print("\nWelcome to the restaurant!")
        discount_threshold = 3
        discount_rate = 0.9

        while True:
            try:
                index = int(input("Type the index of the item: "))
                if index < 0 or index >= len(self.menu_items):
                    print("Invalid index. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue
            
            try:
                amount = int(input("Type the amount of the item: "))
                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue
            except ValueError:
                print("Invalid amount. Please enter a valid integer.")
                continue
            
            self.items.append((self.menu_items[index], amount))
            subtotal += self.menu_items[index].price * amount
            counter += amount

            if input("Do you want to add more items? (y/n): ").lower() != "y":
                break

        if counter >= discount_threshold:
            subtotal *= discount_rate
        return f"Total Order: ${subtotal:.2f}"

    def __iter__(self):
        return OrderIterator(self.items)
    
    def __str__(self):
        return ", ".join(f"{item.name} x{amount}" for item, amount in self.items)

# Función principal
def __main__():
    menu_manager = MenuManager()
    menu_manager.load_menu("menu.json")
    
    menu_items = [MenuItem.from_dict(item) for category in menu_manager.menu.values() for item in category]
    
    order_manager = OrderManager()

    while True:
        action = input("\nChoose an action: (1) Add Order, (2) Process Order, (3) Show Orders, (4) Manage Menu, (5) Exit: ")

        if action == "1":
            order = Order(menu_items)
            print(order.check_order())
            order_manager.add_order(order)
        elif action == "2":
            order_manager.process_order()
        elif action == "3":
            order_manager.show_orders()
        elif action == "4":
            print("Menu management is currently unchanged.")
        elif action == "5":
            menu_manager.save_menu("menu.json")
            print("Exiting program.")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    __main__()
