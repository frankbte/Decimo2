from mpi4py import MPI
import sys

def BLOCK_LOW(id, p, n):
    return (id * n) // p

def BLOCK_HIGH(id, p, n):
    return BLOCK_LOW(id + 1, p, n) - 1

def get_primes(numbers):
    primes = []
    for num in numbers:
        if num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes

def main():
    t1 = MPI.Wtime()
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    root = 0

    if rank == root:
        if len(sys.argv) != 2:
            print("Uso: mpiexec -n <num_procesos> python3 script.py <n>")
            sys.exit(1)

    n = int(sys.argv[1])

    inicio = BLOCK_LOW(rank, size, n) + 1
    fin = BLOCK_HIGH(rank, size, n) + 1

    local_numbers = [i for i in range(inicio, fin + 1)]
    local_primes = get_primes(local_numbers)

    total_primes = comm.reduce(len(local_primes), op=MPI.SUM, root=root)

    if rank == root:
        tiempo = MPI.Wtime() - t1
        print(f"{size:3},{total_primes},{tiempo:12.10f}")

        # Guardar los resultados en un archivo
        with open("resultados.txt", "a") as f:
            f.write(f"{size},{total_primes},{tiempo:.10f}\n")

if __name__ == "__main__":
    main()

