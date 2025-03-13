from mpi4py import MPI
import numpy as np
from sortValues import *
import math

def esta_ordenada(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return False
    return True


def main():

    #Leemos el archivo de datos
    nombre_archivo = "numeros.txt"
    with open(nombre_archivo, "r") as fp:
        n = int(fp.readline())
        lista_completa = np.array([int(x) for x in fp.readlines()]).tolist()

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    root = 0
    t1 = MPI.Wtime()

    # Broadcast para compartir el tamaño de la lista (n) con todos los procesos
    n = comm.bcast(n, root=0)
    #print(f"n={n}")
    # División de la lista en sublistas usando BLOCK_LOW y BLOCK_HIGH
    if rank == 0:
        sublistas = [lista_completa[BLOCK_LOW(i, size, n):BLOCK_HIGH(i, size, n) + 1] for i in range(size)]
    else:
        sublistas = None

    # Scatter para distribuir las sublistas
    lista_local = comm.scatter(sublistas, root=0)
    lista_local = quicksort(lista_local)

    #print(f"Soy el proceso {rank} y mi lista inicial ordenada es: {lista_local}")
    #print(rank, ", Lista local ", lista_local)

    # Número de iteraciones necesarias para garantizar la ordenación global
    for i in range(math.ceil(size/2.0)):
    # Primera fase: procesos impares mandan, procesos pares reciben
        if rank % 2 == 1:
            comm.send(lista_local, dest=rank - 1, tag=0)
            lista_local = comm.recv(source=rank - 1, tag=1)
        if rank % 2 == 0 and rank != size - 1:
            copia_lista = comm.recv(source=rank + 1, tag=0)
            lista_local = mezcla(lista_local, copia_lista)
            lista_fuera = lista_local[len(lista_local) // 2:]
            lista_local = lista_local[:len(lista_local) // 2]
            comm.send(lista_fuera, dest=rank + 1, tag=1)

        comm.Barrier()  # Sincronizacin

            # Segunda fase: procesos pares mandan, procesos impares reciben
        if rank != root and rank % 2 == 0:
            comm.send(lista_local, dest=rank - 1, tag=2)
            lista_local = comm.recv(source=rank - 1, tag=3)
        if rank % 2 == 1 and rank != size - 1:
            copia_lista = comm.recv(source=rank + 1, tag=2)
            lista_local = mezcla(lista_local, copia_lista)
            lista_fuera = lista_local[len(lista_local) // 2:]
            lista_local = lista_local[:len(lista_local) // 2]
            comm.send(lista_fuera, dest=rank + 1, tag=3)

        comm.Barrier()  # Sincronizacin

    #print(f"{i}, {rank},  Lista local:  {lista_local}")

    t2 = MPI.Wtime() - t1
    # Recolectar resultados finales
    lista_final = comm.gather(lista_local, root=root)

    if rank == root:
        lista_final = sum(lista_final, [])
        ordenada = esta_ordenada(lista_final)
        print(f"{size}, {ordenada}, {t2}")
        #lista_final = quicksort(lista_final)

if __name__ == "__main__":
    main()