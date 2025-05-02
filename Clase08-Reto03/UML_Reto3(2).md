classDiagram
    class MenuItem {
        +str name
        +float price
        +str size
        +__init__(name: str, price: float, size: str)
        +__str__() str
    }

    class Beverage {
        +__init__(name: str, price: float, size: str)
    }

    class Appetizer {
        +__init__(name: str, price: float, portion_size: str)
    }

    class MainCourse {
        +__init__(name: str, price: float, size: str)
    }

    class Order {
        +MenuItem menu_item
        +float subtotal
        +int index
        +int amount
        +str desicion
        +int counter
        +__init__(menu_item: MenuItem)
        +check_order() str
    }

    MenuItem <|-- Beverage
    MenuItem <|-- Appetizer
    MenuItem <|-- MainCourse
    Order *-- MenuItem : contains
