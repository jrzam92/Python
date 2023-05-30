from random import * 

aleatorio =randint(1,50)
print(aleatorio)

#numero decimal entre ciertos numeros 
aleatorio=round(uniform(1, 5),1)
print(aleatorio)

#Escoge cualquier valor 
aleatorio=random()
print(aleatorio)
#escoge una opcion de la lista 
colores=['azul','rojo','verde','amarillo']
aleatorio=choice(colores)
print(aleatorio)

#lista que va de 5 en 5 
numeros=list(range(5,50,5))
#Se puede usar  para juegos de naipes 
shuffle(numeros)
print(numeros)