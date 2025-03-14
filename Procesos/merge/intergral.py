from mpi4py import MPI
import sys

def BLOCK_LOW(id, p, n):
    return id * n // p

def BLOCK_HIGH(id, p, n):
    return (id + 1) * n // p - 1

def BLOCK_SIZE(id, p, n):
    return BLOCK_HIGH(id, p, n) - BLOCK_LOW(id, p, n) + 1

def calcular_integral(a, b, n, rank, size):
    dx = (b - a) / n
    low = BLOCK_LOW(rank, size, n)  # Índice de inicio
    high = BLOCK_HIGH(rank, size, n)  # Índice de fin
    local_n = BLOCK_SIZE(rank, size, n)  # Tamaño del bloque para este proceso

    local_a = a + low * dx  # Punto inicial del proceso
    local_integral = 0.0

    x = local_a
    for _ in range(local_n):
        valor_fx = x * x  # Función a integrar (x^2)
        local_integral += valor_fx * dx
        x += dx

    return local_integral

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        if len(sys.argv) != 4:
            print("Uso: mpirun -np <num_procesos> python script.py <a> <b> <n>")
            sys.exit(1)

        a = float(sys.argv[1])
        b = float(sys.argv[2])
        n = int(sys.argv[3])
        t1 = MPI.Wtime()

        print(f"Calcula la integral en el intervalo [{a}, {b}] con {n} subintervalos usando {size} procesos")

    else:
        a, b, n = None, None, None

    # Broadcast de los valores a todos los procesos
    a = comm.bcast(a, root=0)
    b = comm.bcast(b, root=0)
    n = comm.bcast(n, root=0)

    # Cada proceso calcula su parte
    integral_local = calcular_integral(a, b, n, rank, size)
    t2 = MPI.Wtime() - t1
    # Reducir los valores parciales en el proceso maestro
    integral_total = comm.reduce(integral_local, op=MPI.SUM, root=0)

    # Solo el proceso maestro imprime los resultados
    if rank == 0:
        print(f"{size}, {integral_total}, {t2}")