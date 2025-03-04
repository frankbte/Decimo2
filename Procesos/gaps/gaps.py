from mpi4py import MPI
import sys
from sortValues import BLOCK_LOW, BLOCK_HIGH, BLOCK_SIZE
from numFunctions import get_primes, get_gaps

def main():
    t1 = MPI.Wtime()
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    root = 0

    if rank == root:
        if len(sys.argv) != 2:
            print("Uso: mpiexec -n <num_procesos> python3 script_gap.py <n>")
            sys.exit(1)
        n = int(sys.argv[1])
    else:
        n = None

    n = comm.bcast(n, root=root)
    inicio = BLOCK_LOW(rank, size, n) + 1
    fin = BLOCK_HIGH(rank, size, n) + 1
    local_numbers = [i for i in range(inicio, fin + 1)]
    local_primes = get_primes(local_numbers)
    max_diff = 0

    if rank == root and local_primes:
        comm.send(local_primes[-1], dest=rank + 1, tag=11)
    elif rank != root:
        ultimo = comm.recv(source=rank - 1, tag=11)
        local_primes.insert(0, ultimo)
        if rank != size - 1 and local_primes:
            comm.send(local_primes[-1], dest=rank + 1, tag=11)

    if local_primes:
        _, max_local_gaps, max_diff = get_gaps(local_primes)

    max_global_gap = comm.reduce(max_diff, op=MPI.MAX, root=root)


    t2 = MPI.Wtime()
    tiempo_final = t2 -t1

    if rank == root:
        print(f"{size} {max_global_gap} {tiempo_final} s")

if __name__ == "__main__":
    main()
