# Proyecto: Reto 5 - Figuras Geométricas

## Parte 1:

#### Estructura

```
Reto 5.1/
│
├── main.py
│
└── paquete/
    │
    ├── __init__.py
    │
    └── shape.py

```


#### Descripción
1. **`main.py`**: 
   - Contiene el programa principal para instanciar y probar las clases.
   - Demuestra el uso de puntos, líneas, rectángulos, cuadrados, triángulos y sus variantes.

2. **`paquete/shape.py`**:
   - Define todas las clases relacionadas con puntos, líneas, figuras geométricas y sus subclases, como triángulos equiláteros, isósceles, escalenos y triángulos rectángulos.

---

## Parte 2:

#### Estructura

```
Reto 5.2/
│
├── main.py
│
└── paquete/
    │
    ├── __init__.py
    │
    ├── Point.py
    │
    ├── Line.py
    │
    ├── Rectangle.py
    │
    ├── Triangle.py
    │
    ├── Shape.py
    │
    ├── RectangleTypes/
    │   ├── __init__.py
    │   └── Square.py
    │
    └── TriangleTypes/
        ├── __init__.py
        ├── Isosceles.py
        ├── Scalene.py
        ├── Trirectangle.py
        └── Equilateral.py

```

#### Descripción
1. **`main.py`**:
   - Contiene el programa principal, similar a la Parte 1, pero adaptado a la nueva estructura modular.
   - Realiza pruebas instanciando puntos, líneas y figuras geométricas para verificar su funcionamiento.

2. **`paquete/`**:
   - **`Point.py`**: Define la clase `Point`, que representa un punto en el plano.
   - **`Line.py`**: Define la clase `Line`, que representa un segmento de línea entre dos puntos.
   - **`Shape.py`**: Clase base para las figuras geométricas.
   - **`Rectangle.py`**: Implementa la clase `Rectangle` basada en la clase `Shape`.
   - **`Triangle.py`**: Implementa la clase `Triangle` con atributos y métodos comunes para triángulos.
   - **Subcarpetas**:
     - **`RectangleTypes/`**: 
       - Contiene la clase `Square` (cuadrado), una especialización de rectángulos.
     - **`TriangleTypes/`**: 
       - Contiene clases específicas de triángulos: isósceles, escaleno, equilátero y triángulo rectángulo.
---

