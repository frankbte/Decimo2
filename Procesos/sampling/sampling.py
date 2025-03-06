import sys 
import numpy as np
from mpi4py import MPI
from sortValues import *
import math 

def main():
    #Leemos el archivo de datos
    nombre_archivo = "numeros.txt"
    with open(nombre_archivo, "r") as fp:
        n = int(fp.readline())
        lista_completa = np.array([int(x) for x in fp.readlines()]).tolist()

    #Inicializamos MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    root = 0

    #if rank == root:
    #    print(f"Lista original: {lista_completa}")

    #Mandampos el numero de elementos a todos los procesos
    n = comm.bcast(n, root=0)
    
    # División de la lista en sublistas usando BLOCK_LOW y BLOCK_HIGH
    if rank == 0:
        # Crear una lista de sublistas para scatter
        sublistas = [lista_completa[BLOCK_LOW(i, size, n):BLOCK_HIGH(i, size, n) + 1] for i in range(size)]
    else:
        sublistas = None

    # Scatter para distribuir las sublistas
    lista_local = comm.scatter(sublistas, root=0)
    lista_local = quicksort(lista_local)


    print(f"Proceso: {rank}, lista: {lista_local}")

    # Paso 3

    num_muestras  = size
    muestras = []

    if len(lista_local) >= num_muestras:
        for i in range(num_muestras):
            muestras.append(lista_local[math.floor(i*n/size**2)])
    else:
        # Si la lista es más pequeña que el número de procesos, tomamos todos los valores
        muestras = lista_local

    print(f"Proceso: {rank}, muestras: {muestras}")

    muestras_recolectadas = comm.gather(muestras, root=0)

    if rank == 0:
         # Aplanar la lista para tener una sola lista de muestras
        muestras_recolectadas = [item for sublist in muestras_recolectadas for item in sublist]
        muestas_ord = quicksort(muestras_recolectadas)
        print(f"Muestras ordenadas: {muestas_ord}")
        pivotes  = [muestas_ord[i *size +(size // 2) - 1]]
        print(f"Pivotes: {pivotes}")
        
if __name__ == "__main__":
    main()