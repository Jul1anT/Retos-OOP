# Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función 
# debe recibir una lista de enteros y retornar solo aquellos que sean primos.

def es_primo(n):
	if n < 2:
		return None
	for i in range(2,int(n**0.5)+1):
		if (n%i==0):
			return None
	return n

try:
	nums = input("Digite el arreglo de números enteros (separandolos por ','): ")
	nums = [int(num) for num in nums.split(',')]
except ValueError:
	print("Error: Asegúrese de ingresar solo números enteros separados por comas.")


primos = []
for i in range(len(nums)):
	primos.append(es_primo(nums[i]))
print(f"Los números primos son: {primos}")