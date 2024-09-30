#crear una clase con alummos con los atributos que usted crea por conveniente 
#luego instancia a 4 alumnos
class alumnos:
    #atributos
    def __init__(self,nombre:str,edad:int,genero:str,dni:int):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.dni=dni

#instanciar
alumno_1=alumnos("marcos",12,"macho",737273732)
print(alumno_1.nombre)
alumno_2=alumnos("ceb",14,"macho",74763633)
print(alumno_2.nombre)
alumno_3=alumnos("computoncio",13,"macho",773727632)
print(alumno_3.nombre)
alumno_4=alumnos("filo",12,"macho",737273732)
print(alumno_4.nombre)