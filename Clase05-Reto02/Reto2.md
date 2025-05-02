classDiagram
    direction TB
    class Persona {
        +id: int
        +nombre: String
        +direccion: String
    }
    class Empleado {
        +id_empleado: int
        +cargo: String
        +vender(Venta): void
        +realizar_devolucion(Devolucion): void
    }
    class Proveedor {
        +id_proveedor: int
        +telefono: String
        +modificar_stock(Producto, int): void
    }

    Persona <|-- Empleado
    Persona <|-- Proveedor
