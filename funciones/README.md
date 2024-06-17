# FUNCIONES
## CONCEPTO
matematicamente una funcion es una operacion que toma uno o mas valores llamados `argumentos` y produce un valor denominado `resultado`
> [!NOTE]
> todos los lenguajes de programacion tiene funciones incorporadas (`funciones internas`), y funciones creadas por el usuario (`funciones externas`)
En programacion una funcion es un subprograma, es una estructura que nos permite agrupar codigo y sus principales objetivos son:
- `NO REPETIR` fragmentos de codigo
- `REUTILIZAR` el codigo en distintos escenarios
## ESTRUCTURA DE UNA FUNCION
Una funcion viene `definida` por un `nombre`, sus `parametros` y su valor de `retorno`.
una ves creadea la funcion podremos solicitar su ejecucion `invocando` la funcion por su `nombre`.
## DEFINIR UNA FUNCION EN PYTHON
Para definir funciiones en python primero utilizaremos la palabra reservada `def` seguida por el `nombre` de la funcion. A continuacion especificaremos los `parametros` con `()` si es una funcion sin parametros, `(a)` si es una funcion con parametros, si se tuviera mas de un parametros iran separados por `,`, finalizaremos la linea con `:`, en la siguiente linea sin olvidar el identado, comenzara el `cuerpo` de la funcion (micro programa) que puede contener 1 o mas sentencias, finalmente debera `retornar` un resultado con la palabra reservada `return`.
> [!TIP]
> como retorno tambien se puede utilizar la `funcion interna`, `print()`, para depuracion de codigo no es recomendable usarlo en produccion.

> [!TIP]
> `print()` dentro de una una funcion es una herramienta que se utiliza para depurar o comprobar que la funcion se ejecute de manera correcta.
**ejemplo:** 
```python
def saluda():
    saludo="hola chivo"
    saludo_dos="como estas"
    return f"{saludo}, {saludo_dos}"
print(saludo())
```
## Invocar una funcion 
Para invocar, (o lllamar, ejecutar) una funcion solo tendremos que escribir el `nombre` de la funcion seguido por parentesis.
```python
def saludo():
    print("hola")
#invocando la funcion
saludo()
```
## Retornar un valor
Las funciones pueden retornar (o devolver) un valor.
```python
def uno():
    return 1
uno()
```
>[!WARNING]
No confundir `print()` con `return`, el valor retornado por `return` nos permite usarlo fuera de su contexto, y `print()` solo mostrara el literal por terminal.
**ejemplo**
*en el archivo `lecture.py`
## Retornando multiples valores
El secreto es hacerlo mediante un tipo de dato estructurado
```python
def tupla():
    return 2,3,4
tupla()
#retorna (2,3,4)
def lista():
    return ["hola",45]
lista()
#retorna ["hola",45]
def dicc():
    return {"nombre":"jose","edad":45}
dicc()
#retorna {"nombre":"jose","edad":45} 
```
## parametros y argumentos
si una funcion no dispusiera de valores de entrada estaria limitada en su actuacion.
es por ello que los `parametros` no permiten variar los datos que consume una funcion para obtener distintos resultados
**ejemplo**
*crear una funcion que recibe un valor numerico y devuelve su raiz cuadrada*
```python
def sqrt(valor):
    return valor**(1/2)
# NOTA: en este caso el valor 4 es un argumeto de la funcion
sqrt(4)
```
cuando llamamos a una funcion con `argumentos` los valores dde estos argumentos se copian en los correspondientes`parametros` dentro de la funcion.
```python
def ejem(a,b,c):
    return a+b+c
ejem(4,5,6)
```
### argumentos nominales
en esta aproximacion los argumentos no son copiados en un orden especifico sino que **se asignan por nombre a cada parametro**. ello nos permite evitar el problema de conocer o recordar cual es el orden de los parametros en la definicion de la funcion.
para utilizarlos, basta con realizar una asignacion de cada argumento en la propia llamada a la funcion.
**ejemplo**
```python
def build_cpu(familia,num_core,frecuencia):
    print(f""" 
    la cpu es de la familia {familia}
     con {num_core} cores y con una 
     frecuencia de {frecuencia}
     """)
build_cpu("intel",4,2,7)
#haciendo uso de argumentos nominales
buid_cpu(num_core=4, familia="intel",frecuencia=2.7)
```
### argumentos posicionales
 los argumentos no son copiados en un orden especifico, en este caso debemos conocer o recordar cual es el orden de los parametros
 **ejemplos**
 ```python
 def build_cpu(familia,num_core,frecuencia):
    print(f""" 
    la cpu es de la familia {familia}
     con {num_core} cores y con una 
     frecuencia de {frecuencia}
     """)
#haciendo uso de argumentos posicionales
build_cpu("intel",4,2,7)
 ```
 ### parametros por defecto
es posible especifcar **valores por defecto** e los parametros de una funcion, en el caso de que no se proporcione un valor al argumento en la llamada a la funcion, el parametro correspondiente tomara el valor definido por defecto.
**ejemplo**
```python
def alumnos(nom,app,estado="aprobado"):
alumnos("ruth","castillo")
alumnos("antony","cruzes","desaprobado")
```



### desenpaquetado/empaquetado de argumentos(tarea)
### Empaquetado de Argumentos

#### *args
- Se utiliza para empaquetar una cantidad variable de argumentos posicionales en una tupla.
  
python
def ejemplo_args(*args):
    print(args)

ejemplo_args(1, 2, 3, 'a', 'b')  # Salida: (1, 2, 3, 'a', 'b')


#### **kwargs
- Se utiliza para empaquetar una cantidad variable de argumentos con nombre en un diccionario.
  
python
def ejemplo_kwargs(**kwargs):
    print(kwargs)

ejemplo_kwargs(a=1, b=2, c=3)  # Salida: {'a': 1, 'b': 2, 'c': 3}


### Desempaquetado de Argumentos

#### Desempaquetado de Tuplas/Listas con *
- Permite pasar una secuencia de argumentos a una función como si fueran argumentos posicionales separados.

python
def suma(a, b, c):
    return a + b + c

valores = (1, 2, 3)
print(suma(*valores))  # Salida: 6


#### Desempaquetado de Diccionarios con **
- Permite pasar un diccionario a una función como si fueran argumentos con nombre separados.

python
def mostrar_info(nombre, edad, ciudad):
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

info = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Madrid'}
mostrar_info(**info)  # Salida: Nombre: Juan, Edad: 25, Ciudad: Madrid


### Ejemplos Combinados

#### Empaquetado y Desempaquetado Simultáneo
- Puedes combinar *args y **kwargs en la misma función.

```python
def combinacion(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

combinacion(1, 2, 3, a=4, b=5, c=6)
# Salida:
# args: (1, 2, 3)
# kwargs: {'a': 4, 'b': 5, 'c': 6}

```
#### Usar * para Desempaquetar en Llamadas a Funciones
- Puedes usar el operador * para desempaquetar una lista dentro de una función.

```python
def funcion(a, b, c):
    print(a, b, c)

lista = [1, 2, 3]
funcion(*lista)  # Salida: 1 2 3


#### Usar ** para Desempaquetar en Llamadas a Funciones
- Puedes usar el operador ** para desempaquetar un diccionario dentro de una función.
```
```python
def funcion(a, b, c):
    print(a, b, c)

diccionario = {'a': 1, 'b': 2, 'c': 3}
funcion(**diccionario)  # Salida: 1 2 3
```
 ## funciones internas de python (tarea)

 En Python, existen muchas funciones internas (también conocidas como funciones incorporadas o built-in) que están disponibles automáticamente sin necesidad de importarlas desde un módulo. Estas funciones realizan una variedad de tareas, desde operaciones matemáticas básicas hasta la manipulación de estructuras de datos. Aquí te presento algunas de las funciones internas más comunes y útiles en Python:

1. *Funciones Matemáticas y Numéricas:*
   - abs(x): Devuelve el valor absoluto de un número.
   - round(x, n): Redondea un número x a n decimales.
   - max(iterable, *[, key, default]): Devuelve el valor máximo de un iterable.
   - min(iterable, *[, key, default]): Devuelve el valor mínimo de un iterable.
   - sum(iterable, /, start=0): Suma los elementos de un iterable.

2. *Funciones de Conversión:*
   - int(x, base=10): Convierte un valor a un entero.
   - float(x): Convierte un valor a un número de punto flotante.
   - str(object): Convierte un objeto a una cadena de caracteres.
   - list(iterable): Convierte un iterable a una lista.
   - tuple(iterable): Convierte un iterable a una tupla.
   - dict(): Crea un diccionario.

3. *Funciones de Secuencia y Estructuras de Datos:*
   - len(s): Devuelve la longitud (el número de elementos) de un objeto.
   - sorted(iterable, *, key=None, reverse=False): Devuelve una lista ordenada de los elementos en un iterable.
   - reversed(seq): Devuelve un iterador que invierte el orden de una secuencia.
   - enumerate(iterable, start=0): Devuelve un objeto enumerado.
   - zip(*iterables): Une varios iterables.

4. *Funciones de Entrada/Salida:*
   - print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False): Imprime objetos a la salida estándar.
   - input(prompt): Permite al usuario ingresar datos desde la entrada estándar.

5. *Funciones de Manipulación de Archivos:*
   - open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None): Abre un archivo y devuelve un objeto de archivo.

6. *Funciones de Evaluación y Ejecución:*
   - eval(expression, globals=None, locals=None): Evalúa una expresión.
   - exec(object, globals=None, locals=None): Ejecuta un objeto de código.

7. *Funciones de Comprobación y Atributos:*
   - type(object): Devuelve el tipo del objeto.
   - isinstance(object, classinfo): Comprueba si un objeto es una instancia de una clase o de una tupla de clases.
   - hasattr(object, name): Comprueba si un objeto tiene un atributo con el nombre especificado.
   - getattr(object, name[, default]): Devuelve el valor de un atributo de un objeto.
   - setattr(object, name, value): Establece un atributo de un objeto.