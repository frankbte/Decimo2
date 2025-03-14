from mpi4py import MPI
from sortValues import quicksort, read_array, mezcla
import sys
import numpy as np
import math

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    root = 0

    if len(sys.argv) != 2:
        if rank == root:
            print("Usage: python script.py file1.txt")
        sys.exit(1)

    arg = sys.argv[1]
    t1 = MPI.Wtime()

    if rank == root:
        # Obtener los chunks y la longitud total del arreglo
        chunks, arr_lenght = read_array(sys.argv[1], size)

        # Verificar que la cantidad de chunks es igual a size
        if len(chunks) != size:
            print(f"Error: Se generaron {len(chunks)} chunks en lugar de {size}")
            sys.exit(1)
    else: 
        chunks = None

    # Distribuir los datos a cada proceso
    recvbuf = comm.scatter(chunks, root=0)

    # Cada proceso ordena su lista localmente
    ordered_nums = quicksort(recvbuf)

    for i in range(math.ceil(size / 2)):
        # Impares envían, pares reciben
        if rank % 2 == 1:
            comm.send(ordered_nums, dest=rank-1, tag=11)
            ordered_nums = comm.recv(source=rank-1, tag=12)
        if rank % 2 == 0 and rank != size-1:
            recieved_list = comm.recv(source=rank+1, tag=11)
            ordered_nums = mezcla(ordered_nums, recieved_list)
            away = ordered_nums[len(ordered_nums)//2:]
            ordered_nums = ordered_nums[:len(ordered_nums)//2]
            comm.send(away, dest=rank+1, tag=12)

        # Pares envían, impares reciben
        if rank != root and rank % 2 == 0:
            comm.send(ordered_nums, dest=rank-1, tag=13)
            ordered_nums = comm.recv(source=rank-1, tag=14)
        if rank % 2 == 1 and rank != size-1:
            recieved_list = comm.recv(source=rank+1, tag=13)
            ordered_nums = mezcla(ordered_nums, recieved_list)
            away = ordered_nums[len(ordered_nums)//2:]
            ordered_nums = ordered_nums[:len(ordered_nums)//2]
            comm.send(away, dest=rank+1, tag=14)

    t2 = MPI.Wtime() - t1
    all_lists = comm.gather(ordered_nums, root=root)

    if rank == root:
        final = [item for sublist in all_lists for item in sublist]
        ind = int(all(final[i] <= final[i+1] for i in range(len(final) - 1)))
        print(f"{size}, {ind}, {t2}")

if __name__ == "__main__":
    main()
