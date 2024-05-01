**Título: Manipulación de Cadenas de Caracteres en Python**

**I. Creación de Cadenas:**
   - Las cadenas de caracteres (str) se crean utilizando comillas simples (''), comillas dobles ("") o triple comillas (''' o """).

**Ejemplo:**
```python
cadena1 = 'Hola mundo'
cadena2 = "¡Hola, mundo!"
cadena3 = '''¡Hola, mundo!'''

print(cadena1)  # Hola mundo
print(cadena2)  # ¡Hola, mundo!
print(cadena3)  # ¡Hola, mundo!
```

**II. Indexación y Segmentación:**
   - Se puede acceder a caracteres individuales en una cadena utilizando índices.
   - La segmentación permite acceder a subcadenas utilizando rangos de índices.

**Ejemplo:**
```python
cadena = "Python"

print(cadena[0])     # P
print(cadena[2:5])   # tho
print(cadena[-1])    # n
```

**III. Métodos Útiles:**
   - Python ofrece una variedad de métodos integrados para manipular cadenas, como ```lower()```, ```upper()```, ```strip()```, ```split()```, ```join()```, entre otros.

**Ejemplo:**
```python
texto = "    Hola, mundo!    "

print(texto.strip())       # "Hola, mundo!"
print(texto.lower())       # "    hola, mundo!    "
print(texto.split(','))    # ['    Hola', ' mundo!    ']
```

**IV. Formateo de Cadenas:**
   - Se puede formatear cadenas utilizando el método ```.format()``` o utilizando f-strings (a partir de Python 3.6).

**Ejemplo:**
```python
nombre = "Juan"
edad = 30

print("Hola, me llamo {} y tengo {} años.".format(nombre, edad))  # Hola, me llamo Juan y tengo 30 años.
print(f"Hola, me llamo {nombre} y tengo {edad} años.")            # Hola, me llamo Juan y tengo 30 años.
```

**V. Inmutabilidad:**
   - Las cadenas de caracteres son inmutables, lo que significa que no se pueden modificar después de su creación.

Las cadenas de caracteres en Python (str) son secuencias de caracteres Unicode y se pueden manipular de diversas formas, incluyendo indexación, segmentación y el uso de métodos integrados.













