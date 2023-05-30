#Ejercicios de enumerador 
#Aqui solo esta entrando al arreglo por el indice
lista =['a','b','c']
indice=0

for item in lista:
    print(indice,item)
    indice+=1
#Aqui se esta realizando los ejemplos de la funcion de enumerador 
#Ej1
lista =['d','e','f']
 

for index,item in enumerate(lista):
    print(index,item)
       
#Ej2
for index,item in enumerate(range(50,55)):
    print(index,item)

#Ej3
mistuples=list(enumerate(lista))
print(mistuples[1][0])

#Ej4
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    
    print(f'{nombre} se encuentra en el índice {indice}')

#Ej5 lista formada por las tuplas (indice, elemento)
lista_indices=list(enumerate("Python"))

#Ej6
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    if nombre.startswith('M'):
        print(f'{indice}')