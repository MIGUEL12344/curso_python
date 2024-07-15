def funcion_es_menor (lista:list):
    """funcion para saber si una persona es menor de edad"""
    menor=lista[0]
    for n in lista:
        if n<menor:
            menor=n
    return menor