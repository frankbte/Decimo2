from mpi4py import MPI
import sys
from sortValues import BLOCK_LOW, BLOCK_HIGH, BLOCK_SIZE
from numFunctions import get_primes, get_gaps

def main():
    #Inicializamos MPI
    t1 = MPI.Wtime()
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    root = 0

    #Leemos argumento de entrada
    if rank == root:
        if len(sys.argv) != 2:
            print("Uso: mpiexec -n <num_procesos> python3 script_twins.py <n>")
            sys.exit(1)
        n = int(sys.argv[1])
    else:
        n = None

    #Le pasamos n a todos los procesos
    n = comm.bcast(n, root=root)

    #Definimos los rangos
    inicio = BLOCK_LOW(rank, size, n) + 1
    fin = BLOCK_HIGH(rank, size, n) + 1

    #Asignamos el rango de numeros para cada proceso
    local_numbers = [i for i in range(inicio, fin + 1)]

    #Calculamos los primos
    local_primes = get_primes(local_numbers)

    #Cuenta de primos gemelos
    local_twin_primes_num = 0

    #Si el proceso es raiz y tiene primos
    if rank == root and local_primes:
        comm.send(local_primes[-1], dest=rank + 1, tag=11) #Enviamos el ultimo primo al siguiente procesador
    elif rank != root:
        ultimo = comm.recv(source=rank - 1, tag=11)  #Recivimos el ultimo primo y lo guardamos
        local_primes.insert(0, ultimo)   #Lo insertamos al incio de la lista
        #Si no estamos en el ultimo proceso, mandamos el ultimo primo al siguiente procesador
        if rank != size - 1 and local_primes:
            comm.send(local_primes[-1], dest=rank + 1, tag=11)

    if local_primes:
        local_twin_primes_num = get_gaps(local_primes) #Calculamos la cantidad de primos gemelos

    global_twin_primes_num = comm.reduce(local_twin_primes_num, op=MPI.SUM, root=root)


    t2 = MPI.Wtime()
    tiempo_final = t2 -t1

    if rank == root:
        print(f"{size}, {global_twin_primes_num}, {tiempo_final}")

if __name__ == "__main__":
    main()
