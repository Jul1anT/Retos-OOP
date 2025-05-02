def es_primo(n):
	if n < 2:
		return None
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return None
	return n

try:
	nums = input("Digite el arreglo de números enteros (separandolos por ','): ")
	nums = [int(num) for num in nums.split(',')]
	primos = []
	for i in range(len(nums)):
		primo = es_primo(nums[i])
		if primo is not None:		# Añade el número a la lista de primos si es primo
			primos.append(primo)
	print(f"Los números primos son: {primos}\n")

except ValueError:
	print("Por favor, ingrese solo números enteros separados por comas.")
except Exception as e:
	print(f"Ocurrió un error: {e}\n")