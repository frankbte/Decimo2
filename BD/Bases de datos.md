
# Abstracción de datos

## Nivel físico:
- Describe como se almacena los datos en la memoria secundaria
## Nivel Lógico:
* Describe que datos ser almacenados en la base de datos y como se relacionan entre ellos.
## Nivel de vistas
* Describe las parte de la base de datos que es de interés para cierto topo de usuarios.

# Ejemplares y esquemas (diferencia)

### La información en una base de datos cambia a lo largo del tiempo

## Ejemplar de la base de datos
* Colección de información almacenada de la base de datos en un momento particular
## Esquema de la base de datos
* Es el diseño completo de la base de datos
* Esquema físico
* Esquema lógico
* Subesquemas

# Independencia física de los datos
* Los programas de aplicación muestran la independencia física de los datos si no dependen del esquema físico.
* Trabajamos en la capa lógica, el sistema de base de datos decide la manera en la que guarda los datos. 

# Modelo de los datos

## Colección de herramientas conceptuales para describir
* Los datos
* Las relaciones
* Las restricciones
## Categorías
* Modelos lógicos basados en registros
	* Modelo entidad - relación
	* Modelo relacional
* Modelos lógicos basados en objetos
* Modelos físicos


# Modelo entidad-relación

El mundo real que será implementado en el sistema se percibe como un conjunto de entidades de sus relaciones.

**Entidad** 
* Una cosa u objeto del mundo real que es distinguible de otros objetos: alumnos, profesores, salón de clase , etc.
* Las entidades se describen en una base de datos mediante un conjunto de atributos
	* Alumno
	* Profesor
	* Asignatura
**Relaciones**
* Describen una asociación entre entidades
	* Profesor imparte asignatura
	* Alumno toma asignatura


# Interconexión de redes

### El objetivo de la interconexión de redes es dar un servicio de comunicación de datos que involucre diversas redes con diferentes tecnologías de forma transparente para el usuario

### Nos ayudan a superar las limitaciones físicas de los elementos básicos de una red.

## Ventajas

* Coordinación de tareas de diversos grupos de trabajo
* Reducción de cortos
* Aumento de la cobertura geográfica

# Tipos de interconexión de redes

* ## Interconexión de Área Local (RAL)
	* Conecta redes que están geográficamente cerca, como puede ser la interconexión de redes de un mismo edificio o entre edificios, creando una Red de Área Metropolitana (MAN)  
* ## Interconexión de Área Extensa
	* Conecta redes geográficamente dispersas, por ejemplo, redes situadas en diferentes ciudades o países.

## Ventajas
* Fiabilidad 
* Prestaciones (Rendimiento)
* Seguridad
* Geografía (Mas fácil administración)
* Gran variedad de redes


## Lenguajes de base de datos

### Los sistemas de bases de datos se proporcionan
* Lenguaje de definición de datos
* Especifican el esquema 
* Permiten definir: Restricciones de dominio, integridad y autorizaciones

### Lenguaje de manipulación de datos
* Pueden ser procedimentales o declarativos
* Entre sus funciones: Recuperar información, agregar, borrar, actualizar



# Modelo Entidad-Relacion

## Entidad
* ### Una entidad es una cosa u objeto del mundo real que es distinguible de todos los demás objetos
	 * Una entidad tiene un conjunto
	 * Los valores de las propiedades pueden identificar unívocamente a cada objeto
## Conjunto de entidades
* ### Agrupa entidades del mismo tipo que comparten propiedades o atributos 
	* Conjunto de entidades profesor
	* Conjunto de entidades alumnos
* ### Extensión



## Superclaves
### La superclave es un conjunto de uno o vario atributos que, considerados conjuntamente, permiten identificar univocamente  cada una tupla de la relación