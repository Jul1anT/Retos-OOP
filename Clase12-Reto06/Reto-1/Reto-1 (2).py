def es_palindromo(palabra):
    try:
        # Verifica que el argumento sea una cadena de texto
        if not isinstance(palabra, str):
            raise TypeError("El argumento debe ser una cadena de texto.")

        # Recorre la mitad de la palabra y compara caracteres
        longitud = len(palabra)
        for i in range(longitud // 2):
            if palabra[i] != palabra[longitud - i - 1]:
                return False
        return True
    
    except TypeError as e:
        print(f"Error: {e}")
        return False

# Solicita al usuario una palabra para verificar si es un palíndromo
palabra = input("Digite la palabra que desea verificar si es palíndromo: ")
result = es_palindromo(palabra)
print(f"Es palíndromo: {result}\n")
