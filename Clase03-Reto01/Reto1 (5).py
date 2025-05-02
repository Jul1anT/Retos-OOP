# Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los
#  mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]

def mismos_caracteres(lista):
  resultado = []
  for palabra in lista:
    for otra_palabra in lista:
      if palabra != otra_palabra and sorted(palabra) == sorted(otra_palabra):
        resultado.append(palabra)
        break
  return resultado

try:
  lista_strings = input("Digite el arreglo de strings (separandolos por ','): ")
  strings = [str(s) for s in lista_strings.split(',')]
  print(f"Los elementos con los mismos caracteres son: {mismos_caracteres(strings)}\n")
except Exception as e:
  print(f"Ha ocurrido un error: {e}")

print()