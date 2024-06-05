#crear un lista de los primeros 20 numeros primos haciendo uso de comprension
numeros_primos=[num for num in range(2,100) if all(num%i !=0 for i in range(2, int(num ** 0.5)+1))]
primeros_20=numeros_primos[:20]
print(primeros_20)