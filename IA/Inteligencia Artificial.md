# ¿ Que es la inteligencia artificial?

Es el desarrollo de **agentes racionales**, que al interactuar con un entorno **maximice** la **esperanza** de una **utilidad** futura.

**Nota: Racional implica exploración, aprendizaje y autonomía. Racional no significa exitoso ni perfecto**

## Como modelo un entorno?

* Inventario de conceptos
* Variables de estado
* Espacio de estado
* Estado
* Percepciones
* Acciones y acciones legales

![[Pasted image 20250130083413.png]]

Tipos de agentes incluyen: humanos, robots, softbots, termostatos

La función de agente mapea usando desde percepciones históricas hasta acciones:
$$
f = P^* → A
$$
![[Pasted image 20250130083825.png]]![[Pasted image 20250130083847.png]]


# Generalización 

![[Pasted image 20250130084022.png]]

¿ Cual es la funcion que mejor describe el comportamiento de los puntos?

* Contrario a lo que uno puede pensar, la naranja es una mala opcion, ya que es demasiado precisa y su comportamiento es anormal, lo que la hace dificil de creer.
* La recta roja es demasiado simple, a pesar de que parece pasar por la mediana de los puntos, es dificil creer que su comportamiento lineal explique de manera logica el comportamiento de los puntos.
* La recta verde es la mejor aproximación, ya que generaliza de manera correcta los puntos, no es demasiado simple pero no es demasiado complicada como para no ser creíble.

![[Pasted image 20250130085008.png]]


# Arboles de decisión


# Regresión lineal

## Que es la regresion lineal?

La **regresión lineal** es un método estadístico y de aprendizaje automático utilizado para modelar la relación entre una variable dependiente (_Y_) y una o más variables independientes (_X_). Se basa en la idea de ajustar una línea recta a un conjunto de datos de tal manera que minimice la diferencia entre los valores predichos y los valores reales.


![[Pasted image 20250226192520.png]]




![[Pasted image 20250226193549.png]]

## Cual es el proposito de la regresion lineal?
El objetivo es encontrar los coeficientes $$ b_{0}, b_{1} $$que minimicen la suma de los errores (ε\varepsilonε). Se hace mediante el método de **mínimos cuadrados ordinarios (OLS)** o técnicas más avanzadas como el **descenso de gradiente** en Machine Learning.


# Clasificación lineal

# Que es?

La **clasificación lineal** es un método en **aprendizaje automático** que se usa para **separar datos en distintas clases** usando una frontera de decisión que es una **línea recta** (en 2D), un **plano** (en 3D) o un **hiperplano** (en dimensiones mayores).

Este tipo de clasificación es útil cuando los datos son **linealmente separables**, es decir, se pueden dividir con una línea recta o un plano sin errores significativos.

![[Pasted image 20250226222050.png]]


### **Modelos de clasificación lineal más comunes**

1. **Regresión logística** 
    - Usa la función sigmoide para clasificar datos en dos clases (0 o 1).
2. **Máquinas de soporte vectorial (SVM)** 
    - Encuentran la **mejor línea de separación** maximizando la distancia entre clases.
3. **Perceptrón** 
    - Es el modelo más simple de una red neuronal, basado en sumas ponderadas de las entradas.

---


## Se explicarán estos temas mas adelante...



# Búsquedas (Search)

## Que es un problema de búsqueda?

- **Problemas de Búsqueda**: Un problema de búsqueda se define por un **espacio de estados**, un **modelo de transición**, un **estado inicial**, una **prueba de objetivo** y una **función de costo del camino**. El objetivo es encontrar una **secuencia de acciones** (un plan) que transforme el estado inicial en un estado objetivo.
    
    - **Espacio de Estados**: Representa todos los posibles estados del problema.
    - **Modelo de Transición**: Describe cómo las acciones cambian el estado actual. La función `Successors(s)` define las acciones posibles desde un estado `s` y sus resultados.
    - **Función de Costo**: Asigna un costo numérico a cada acción, reflejando el "gasto" de usar esa acción.

![[Pasted image 20250226224233.png]]


## Cual será nuestro enfoque para resolver el problema?
## Que es lo que queremos optimizar?

### Ejemplo sencillo que ilustra este problema
![[Pasted image 20250226223927.png]]


- **Tipos de Problemas**: Los problemas de búsqueda pueden clasificarse según la información disponible y la naturaleza del entorno:
    
    - **Totalmente Observable, Determinista**: El agente conoce completamente el estado y el resultado de cada acción.
    - **No Observable (Sensorless o Conformante)**: El agente no tiene información sobre el estado inicial y debe razonar sobre todas las posibilidades.
    - **Parcialmente Observable/No Determinista (Contingencia)**: El agente tiene información limitada y las acciones pueden tener resultados inciertos.
    - **Espacio de Estados Desconocido (Exploración)**: El agente debe aprender sobre el espacio de estados a medida que lo explora.

# Algoritmos de Búsqueda:
- 
    - **Búsqueda en Árbol (Tree Search)**: Explora el espacio de estados construyendo un árbol de búsqueda, donde los nodos representan caminos posibles.
        
        - **Frontier (Fringe)**: Es el conjunto de nodos que están pendientes de expansión.
        - **Expansión**: Generar los sucesores de un nodo.
        - **Estrategia de Exploración**: El método utilizado para seleccionar qué nodo expandir a continuación.
    - **Búsqueda en Profundidad (DFS)**: Expande el nodo más profundo en la frontera. Utiliza una pila LIFO (Last In, First Out).
        
    - **Búsqueda en Anchura (BFS)**: Expande el nodo menos profundo en la frontera. Utiliza una cola FIFO (First In, First Out). BFS encuentra el camino más corto en términos de número de transiciones, pero no necesariamente el de menor costo.
        
    - **Búsqueda de Costo Uniforme (UCS)**: Expande el nodo con el costo de ruta más bajo. Es completo y óptimo, pero puede ser ineficiente porque explora en todas las direcciones.
        
    - **A***: Una búsqueda informada que combina el costo del camino recorrido hasta el momento (`g(n)`) con una estimación heurística del costo restante hasta el objetivo (`h(n)`).
        
        - **f(n) = g(n) + h(n)**
        - **Heurística Admisible**: Una heurística que nunca sobreestima el costo real para alcanzar el objetivo más cercano. Usualmente, se obtienen resolviendo versiones _relajadas_ del problema original.
        - **Condiciones de Terminación**: A* debe detenerse cuando se extrae un nodo objetivo de la cola de prioridad, no cuando se encola.
    
- **Grafos de Espacio de Estados vs. Árboles de Búsqueda**:
    
    - **Grafos de Espacio de Estados**: Los nodos representan estados del problema.
    - **Árboles de Búsqueda**: Los nodos representan caminos (secuencias de acciones) que conducen a esos estados. El mismo estado del problema puede aparecer múltiples veces en el árbol de búsqueda, a través de diferentes caminos.



# Game Trees: Adversarial Search

![[Pasted image 20250226224828.png]]

- **Juegos Adversarios**: Involucran múltiples agentes con objetivos conflictivos.
    
    - **Juegos de Suma Cero**: La utilidad total de todos los jugadores es constante. Un jugador intenta maximizar su utilidad, mientras que el otro intenta minimizarla.
	![[Pasted image 20250226224858.png]]
    - **Información Perfecta**: Todos los jugadores tienen acceso completo al estado del juego.
- **Minimax**: Un algoritmo recursivo para juegos deterministas de suma cero.
![[Pasted image 20250226224945.png]]
    
- **Valor Minimax**: Representa el mejor resultado que un jugador puede lograr asumiendo que el oponente juega óptimamente.
    - **Implementación**: Las funciones `max-value` y `min-value` alternan recursivamente para calcular el valor minimax de cada nodo en el árbol del juego.
    - **Complejidad**: La complejidad temporal es O(b^m) y la complejidad espacial es O(bm), donde 'b' es el factor de ramificación y 'm' es la profundidad del árbol.
![[Pasted image 20250226225024.png]]
- **Poda Alfa-Beta**: Una optimización del algoritmo Minimax que reduce el número de nodos que deben ser evaluados.
    
    - **Alfa (α)**: El valor de la mejor opción (la más alta) encontrada hasta ahora en cualquier punto de elección a lo largo del camino para el jugador MAX.
    - **Beta (β)**: El valor de la mejor opción (la más baja) encontrada hasta ahora en cualquier punto de elección a lo largo del camino para el jugador MIN.
    - **Poda**: Si en un nodo MIN, el valor `v` se vuelve menor o igual a `α`, entonces el jugador MAX no elegirá ese nodo, y podemos podar las ramas restantes. De forma simétrica, si en un nodo MAX, el valor `v` se vuelve mayor o igual a `β`, podemos podar.
    - **Complejidad**: Con un ordenamiento ideal de los nodos, la complejidad temporal se reduce a O(b^(m/2)).
- **Funciones de Evaluación**: En juegos complejos, es imposible buscar hasta los nodos terminales. Las funciones de evaluación estiman la utilidad de un estado no terminal.
    
    - **Función Lineal Ponderada**: Una función de evaluación común es una suma ponderada de características del estado.
    - `E.g. f1(s) = (num white queens – num black queens)`
    - **Profundidad**: Cuanto más profunda es la búsqueda, menos importa la calidad de la función de evaluación.

# Machine Learning: Feature Templates

- **Extracción de Características**: El proceso de transformar datos brutos en un conjunto de características que pueden ser utilizadas por un modelo de aprendizaje automático. La calidad de las características afecta directamente el rendimiento del modelo.
    
- **Plantillas de Características**: Una forma de **organizar y generalizar la extracción de características**.
    
    - **Definición**: Un grupo de características que se computan de manera similar. En lugar de definir características individuales, se define un _patrón_ para generar múltiples características.
- **Implementación**:
    
    - **Vectores Dispersos**: Cuando la mayoría de las características tienen valor cero, es más eficiente usar representaciones dispersas.
        - **Arrays**: Adecuados para características densas, donde la mayoría de los valores son distintos de cero.
        - **Diccionarios**: Adecuados para características dispersas, donde la mayoría de los valores son cero.
- **Ejemplo**: Para determinar si una cadena es una dirección de correo electrónico válida:
    
    - **Características Individuales**: `length>10`, `fracOfAlpha`, `contains @`, `endsWith com`, `endsWith org`.
    - **Plantilla de Característica**: "Los últimos tres caracteres son iguales a...". Esto generaría características como `endsWith aaa`, `endsWith aab`, ..., `endsWith com`, ..., `endsWith zzz`.