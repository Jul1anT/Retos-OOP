# Calculadora 
def operaciones_basicas():
    try:
        operacion = input("Digite el caracter de la operación que desea realizar (+, -, *, /): ").strip()
        
        num1 = float(input("Digite el primer número: "))
        num2 = float(input("Digite el segundo número: "))

        if operacion == '+':
            return num1 + num2
        elif operacion == '-':
            return num1 - num2
        elif operacion == '*':
            return num1 * num2
        elif operacion == '/':
            return num1 / num2  
        else:
            return "Error: Operación no válida"
    
    except ValueError:
        return "Error: Entrada no válida, ingrese números."
    except ZeroDivisionError:
        return "Error: División por cero"

result = operaciones_basicas()
print(f"El resultado es: {result}\n")
