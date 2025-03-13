import sys
import random

def main():
    if len(sys.argv) != 3:
        print("Uso: python script.py <nombre_archivo> <cantidad_datos>")
        return
    
    nombre_archivo = sys.argv[1]
    try:
        n = int(sys.argv[2])
    except ValueError:
        print("El segundo argumento debe ser un número entero.")
        return
    
    with open(nombre_archivo, "w") as fp:
        fp.write(f"{n}\n")
        for _ in range(n):
            fp.write(f"{random.randint(1, 100)}\n")  # Valores en el rango [1,100]

if __name__ == "__main__":
    main()
