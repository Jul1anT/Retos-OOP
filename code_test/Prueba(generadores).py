def contador(n):
    while n > 0:
        yield n
        n -= 1

num = int(input("Digite el contador: "))
gen = contador(num)  # Crear el generador

while True:
    x = int(input("1. para ver el contador, 2. para salir: "))
    if x == 1:
        try:
            print(next(gen))  # Obtener el siguiente valor
        except StopIteration:
            print("El contador ha terminado.")
            break  # Salir si ya no hay más valores        
    else:
        break
