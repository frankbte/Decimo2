import sys
from sortValues import BLOCK_LOW, BLOCK_HIGH, BLOCK_SIZE
from numFunctions import get_primes, get_gaps
import time

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 script_gap.py <n>")
        sys.exit(1)

    t1 = time.time()
    n = int(sys.argv[1])
    size = 1  # En secuencial, solo hay un "proceso"
    rank = 0

    inicio = BLOCK_LOW(rank, size, n) + 1
    fin = BLOCK_HIGH(rank, size, n) + 1
    numbers = list(range(inicio, fin + 1))

    # Obtener los primos
    primes = get_primes(numbers)

    # Calcular los gaps
    max_diff = 0
    if primes:
	_, _, max_diff = get_gaps(primes)

    t2 = time.time()
    tfinal = t2 - t1
    print(f"Max gap: {max_diff}, {tfinal}")

if __name__ == "__main__":
    main()

