#nombre de mi clase
class mascota:
#atributos de mi clase
    nombre="leon"
    edad="5 años"
    sexo="macho"
    raza="chiwawa"
#metodos de mi clase
    def ladrar(self):
        print("guau guau")
#instanciar una clase o crear mis objetos
labrador=mascota()
labrador.nombre="body"
print(labrador.nombre)

aleman=mascota()
aleman.nombre="peruano"
print(aleman.nombre)