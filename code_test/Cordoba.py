import random
import string

# Palabras a buscar (ejemplo, puedes cambiarlas)
PALABRAS = ["PYTHON", "CODIGO", "JUEGO", "MATRIZ", "LETRAS"]

def instrucciones():
    print("Bienvenid@ a la sopa de letras de Darth Pyths")
    print("Instrucciones:")
    print("1. Selecciona la dificultad (10x10, 20x20, 30x30).")
    print("2. Encuentra las palabras escribiendo sus coordenadas inicial y final (ej. A1 A5).")
    print("3. Las palabras pueden estar en horizontal, vertical o diagonal.")
    print("4. Las palabras encontradas se resaltarán en la sopa de letras.\n")

def crear_matriz(tamanio):
    return [[' ' for _ in range(tamanio)] for _ in range(tamanio)]

def insertar_palabra(matriz, palabra):
    """ Intenta colocar una palabra en una posición aleatoria válida """
    tamanio = len(matriz)
    direccion = random.choice(["H", "V", "D"])  # Horizontal, Vertical, Diagonal
    colocada = False

    while not colocada:
        fila = random.randint(0, tamanio - 1)
        col = random.randint(0, tamanio - 1)

        if direccion == "H" and col + len(palabra) <= tamanio:
            if all(matriz[fila][col + i] == ' ' for i in range(len(palabra))):
                for i, letra in enumerate(palabra):
                    matriz[fila][col + i] = letra
                colocada = True

        elif direccion == "V" and fila + len(palabra) <= tamanio:
            if all(matriz[fila + i][col] == ' ' for i in range(len(palabra))):
                for i, letra in enumerate(palabra):
                    matriz[fila + i][col] = letra
                colocada = True

        elif direccion == "D" and fila + len(palabra) <= tamanio and col + len(palabra) <= tamanio:
            if all(matriz[fila + i][col + i] == ' ' for i in range(len(palabra))):
                for i, letra in enumerate(palabra):
                    matriz[fila + i][col + i] = letra
                colocada = True

def rellenar_matriz(matriz):
    """ Llena los espacios vacíos con letras aleatorias """
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == ' ':
                matriz[i][j] = random.choice(string.ascii_uppercase)

def imprimir_matriz(matriz, resaltadas=None):
    """ Imprime la matriz resaltando palabras encontradas """
    if resaltadas is None:
        resaltadas = set()
    
    print('')
    letras = "abcdefghijklmnopqrstuvwxyz"
    print("   " + " ".join(str(i+1) for i in range(len(matriz)))) # Encabezado de columnas
    print('') 

    for i, fila in enumerate(matriz):
        fila_str = []
        for j, letra in enumerate(fila):
            if (i, j) in resaltadas:
                fila_str.append(f"\033[92m{letra}\033[0m")  # Verde para resaltado
            else:
                fila_str.append(letra)
        print(letras[i] + "  " + " ".join(fila_str))

def coordenada_a_indices(coord):
    """ Convierte una coordenada (ej. A1) a índices de matriz """
    try:
        letra, numero = coord[0].upper(), int(coord[1:]) - 1
        fila = ord(letra) - ord('A')
        return fila, numero
    except (ValueError, IndexError):
        return None

def verificar_palabra(matriz, inicio, fin):
    """ Verifica si la palabra seleccionada está en la lista """
    i1, j1 = inicio
    i2, j2 = fin

    palabra_seleccionada = ""
    
    if i1 == i2:  # Horizontal
        paso = 1 if j1 < j2 else -1
        palabra_seleccionada = "".join(matriz[i1][j] for j in range(j1, j2 + paso, paso))

    elif j1 == j2:  # Vertical
        paso = 1 if i1 < i2 else -1
        palabra_seleccionada = "".join(matriz[i][j1] for i in range(i1, i2 + paso, paso))

    elif abs(i2 - i1) == abs(j2 - j1):  # Diagonal
        paso_fila = 1 if i1 < i2 else -1
        paso_col = 1 if j1 < j2 else -1
        palabra_seleccionada = "".join(matriz[i][j] for i, j in zip(range(i1, i2 + paso_fila, paso_fila),
                                                                     range(j1, j2 + paso_col, paso_col)))

    return palabra_seleccionada if palabra_seleccionada in PALABRAS else None

def jugar(matriz):
    """ Permite al usuario interactuar con la sopa de letras """
    palabras_encontradas = set()

    while len(palabras_encontradas) < len(PALABRAS):
        imprimir_matriz(matriz, palabras_encontradas)
        print("\nPalabras a encontrar:", ", ".join(PALABRAS))
        
        entrada = input("\nIngresa coordenadas inicial y final (ej. A1 A5) o 'salir': ").strip()
        if entrada.lower() == "salir":
            break
        
        try:
            c1, c2 = entrada.split()
            inicio = coordenada_a_indices(c1)
            fin = coordenada_a_indices(c2)
            
            if inicio and fin:
                palabra = verificar_palabra(matriz, inicio, fin)
                if palabra:
                    print(f"¡Correcto! Encontraste: {palabra}")
                    palabras_encontradas.update([inicio, fin])
                else:
                    print("Esa no es una palabra válida, intenta de nuevo.")
            else:
                print("Entrada inválida. Usa el formato correcto (ej. A1 A5).")
        except ValueError:
            print("Formato incorrecto. Ingresa dos coordenadas separadas por espacio.")

    print("¡Felicidades! Has encontrado todas las palabras.")

def main():
    instrucciones()
    
    while True:
        try:
            tamanio = int(input("Ingresa tamaño deseado de la sopa (entre 10 y 30): "))
            if 10 <= tamanio <= 30:
                break
            else:
                print("Por favor, ingresa un número entre 10 y 30.")
        except ValueError:
            print("Entrada no válida. Ingresa un número.")
    
    matriz = crear_matriz(tamanio)
    
    for palabra in PALABRAS:
        insertar_palabra(matriz, palabra)

    rellenar_matriz(matriz)
    jugar(matriz)

if __name__ == "__main__":
    main()