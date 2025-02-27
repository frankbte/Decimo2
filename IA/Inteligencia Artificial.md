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


