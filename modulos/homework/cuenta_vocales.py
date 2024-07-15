def funcion_cuenta_vocales(text:str):
    """funcion para contar la cantidad de vocales a que aparecen en un texto"""
    text_minusculas:str=text.lower()
    cantidad_vocales=0
    for n in text_minusculas:
        if n== "a":
            cantidad_vocales+=1
    return cantidad_vocales