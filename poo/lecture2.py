class personaje:
    #atributos
    def __init__(self,nombre,edad,usuario,bando,raza):
        self.nombre=nombre
        self.edad=edad
        self.usuario=usuario
        self.bando=bando
        self.raza=raza
    def mostrar_personaje(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "usuario": self.usuario,
            "bando": self.bando,
            "raza":self.raza,
        }
luffy=personaje("luffy",18,"gomu gomu no mi","pirata","humano")
print(luffy.mostrar_personaje())
coby=personaje("coby",15,"no","sword","humano")
print(coby.bando)
king=personaje("king",40,"zoan mitologica","pirata","lunaria")