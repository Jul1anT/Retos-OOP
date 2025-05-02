# Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, 
# según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado 
# para la operación. entrada: (1,2,"+"), salida (3).

def operaciones_basicas():
	operacion = input(
		"Digite el caracter de la operación que desea realizar (+, -, *, /): "
	)
	num1 = int(input("Digite el primer número: "))
	num2 = int(input("Digite el segundo número: "))
	if operacion == '+':
		return num1 + num2
	elif operacion == '-':
		return num1 - num2
	elif operacion == '*':
		return num1 * num2
	elif operacion == '/':
		if num2 != 0:
			return num1 / num2
		else:
			return "Error: División por cero"
	else:
		return "Operación no válida"

result = operaciones_basicas()
print(f"El resultado es: {result}")
