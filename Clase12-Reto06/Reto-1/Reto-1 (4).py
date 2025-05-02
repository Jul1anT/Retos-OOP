def suma_mayor(lista):
	if len(lista) < 2:
		return None  # No hay suficientes elementos para comparar

	Suma = lista[0] + lista[1]
	for i in range(1, len(lista) - 1):
		suma = lista[i] + lista[i + 1]
		if suma > Suma:
			Suma = suma
	return Suma

try:
	lista = input("Digite el arreglo de números enteros (separandolos por ','): ")
	nums = [int(num) for num in lista.split(',')]
	print(f"La mayor suma entre dos elementos consecutivos es: {suma_mayor(nums)}")
except ValueError:
	print("Error: Asegúrese de ingresar solo números enteros separados por comas.")
except Exception as e:
	print(f"Ha ocurrido un error: {e}")  # Captura cualquier otro error y lo muestra
