import sys
from sortValues import BLOCK_LOW, BLOCK_HIGH, BLOCK_SIZE
from numFunctions import get_primes, get_gaps
import time

def main():
    t1 = time.time()  # Usamos time.time() en lugar de MPI.Wtime()

    # Leemos el argumento de entrada
    if len(sys.argv) != 2:
        print("Uso: python script_twins.py <n>")
        sys.exit(1)

    n = int(sys.argv[1])

    # Definimos los rangos
    inicio = BLOCK_LOW(0, 1, n) + 1  # El rango es de 0 a 1 ya que solo hay un proceso
    fin = BLOCK_HIGH(0, 1, n) + 1

    # Asignamos el rango de números para este único proceso
    local_numbers = [i for i in range(inicio, fin + 1)]

    # Calculamos los primos
    local_primes = get_primes(local_numbers)

    # Cuenta de primos gemelos
    local_twin_primes_num = 0
    if local_primes:
        local_twin_primes_num = get_gaps(local_primes)  # Calculamos la cantidad de primos gemelos

    t2 = time.time()
    tiempo_final = t2 - t1

    print(f"{local_twin_primes_num}, {tiempo_final} ")

if __name__ == "__main__":
    main()
