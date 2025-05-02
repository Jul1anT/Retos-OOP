# Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos 
# consecutivos.

def suma_mayor(lista):
  if len(lista) < 2:
    return None  # No hay suficientes elementos para comparar

  Suma = lista[0] + lista[1]
  for i in range(1, len(lista) - 1):
    suma = lista[i] + lista[i + 1]
    if suma > Suma:
      Suma = suma
      return Suma

lista = input("Digite el arreglo de números enteros (separandolos por ','): ")
nums = [int(num) for num in lista.split(',')]
print(f"La mayor suma entre dos elementos consecutivos es: {suma_mayor(nums)}")
