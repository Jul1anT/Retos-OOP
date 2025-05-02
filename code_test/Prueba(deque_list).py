from collections import deque
import time

# Prueba con lista
lista = list(range(10**5))
start = time.time()
for _ in range(10000):
    lista.pop(0)  # O(n) -> Lento
end = time.time()
print(f"Tiempo con list.pop(0): {end - start:.5f} segundos")

# Prueba con deque
dq = deque(range(10**5))
start = time.time()
for _ in range(10000):
    dq.popleft()  # O(1) -> Rápido
end = time.time()
print(f"Tiempo con deque.popleft(): {end - start:.5f} segundos")
