
#definimos la clase juego
class Juego:

    def __init__(self, initial_state = None):
        if initial_state:
            self.state = initial_state
        else:
            self.state = [[1,2,3,4],
                             [5,6,7,8],
                             [9,10,11,12],
                             [13,14,15,16]]
            
    def imprimir(self):
        #Imprime le estado del juego 
        for row in self.state:
            print("\t".join(map(str, row)))
        print("\n")
    
    def acciones_legales(self):
        #Funcion que devuelve una lista de acciones legales
        actions = []
        for i in range(4):
            actions.append(("derecha", i))
            actions.append(("izquierda", i))
        for j in range(4):
            actions.append(("arriba", j))
            actions.append(("abajo", j))
        return actions

def main():
    #Ejemplo de uso
    puzzle = Juego()
    print("Estado inicial:")
    puzzle.imprimir()
    print("Acciones legales:")
    print(puzzle.acciones_legales())

if __name__ == "__main__":
    main()