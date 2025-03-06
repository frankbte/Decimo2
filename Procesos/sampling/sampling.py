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
    n = comm.bcast(n, root=root)
    
    # División de la lista en sublistas usando BLOCK_LOW y BLOCK_HIGH
    if rank == root:
        # Crear una lista de sublistas para scatter
        sublistas = [lista_completa[BLOCK_LOW(i, size, n):BLOCK_HIGH(i, size, n) + 1] for i in range(size)]
    else:
        sublistas = None

    # Scatter para distribuir las sublistas
    lista_local = comm.scatter(sublistas, root=root)
    lista_local = quicksort(lista_local)


    print(f"Proceso: {rank}, lista: {lista_local}")

    # Paso 3
    # n = numero de muestras
    # size = numero de procesos
    # 

    num_muestras  = size
    muestras = []

    if len(lista_local) >= num_muestras:
        for i in range(num_muestras):
            muestras.append(lista_local[math.floor(i*n/size**2)])
    else:
        # Si la lista es más pequeña que el número de procesos, tomamos todos los valores
        muestras = lista_local

    print(f"Proceso: {rank}, muestras: {muestras}")

    muestras_recolectadas = comm.gather(muestras, root=root)

    #paso 4
    if rank == root:
        # Aplanar la lista para tener una sola lista de muestras
        muestras_recolectadas = [item for sublist in muestras_recolectadas for item in sublist]
        muestras_ord = quicksort(muestras_recolectadas)
        print(f"Muestras ordenadas: {muestras_ord}")
        pivotes  = [muestras_ord[i * size + (size // 2)- 1] for i in range(1, size)]
        print(f"Pivotes: {pivotes}")
    else:
        pivotes = None
            
    pivotes = comm.bcast(pivotes, root=root)

    #paso 5
    particiones = [[] for _ in range(size)]  # Inicializar listas vacías para cada partición

    for num in lista_local:
        for i, pivote in enumerate(pivotes):
            if num <= pivote:
                particiones[i].append(num)
                break
        else:
            # Si el número es mayor que todos los pivotes, va a la última partición
            particiones[-1].append(num)

    print(f"Proceso: {rank}, particiones: {particiones}")


if __name__ == "__main__":
    main()