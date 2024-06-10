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