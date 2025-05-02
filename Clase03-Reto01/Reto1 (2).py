# Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing 
# para invertir la palabra y verificar que sea igual a la original.

def es_palindromo(palabra):
	longitud = len(palabra)
	for i in range(longitud // 2):
		if palabra[i] != palabra[longitud - i - 1]:
			return False
		return True

palabra = input("Digite la palabra que desea verificar si es palíndromo: ")
result = es_palindromo(palabra)
print(f"Es palindromo: {result}")