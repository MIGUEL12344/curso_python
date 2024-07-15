def funcion_es_mayor(lista:list):
    """funcion para saber si una persona es menor de edad"""
    mayor=lista[0]
    for n in lista:
        if n>mayor:
            mayor=n
    return mayor