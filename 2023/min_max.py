#Ejercicio para saber que numero es menor y cual es mayor 
menor=min(58,96,72,64,35)
mayor=max(58,96,72,64,35)
print(menor)
print(mayor)
#Ejercicio para saber que numero es menor y cual es mayor 
lista =[58,96,72,64,35]
print(f'El menor es {min(lista)} y el mayor es {max(lista)}')
#Ejercicio de lista para saber que nombre es minimo y cual es maximo 
nombres=['juan','carlos','alicia','pablo']
print(min(nombres))
print(max(nombres))
#Ejercicios con string para un solo nombre
nombre="Carlos"
print(min(nombre.lower()))
#Ejemplo de diccionario con minimos 
dic={'c1':45,'c2':11}

print(dic.values())

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo=max(lista_numeros)

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

rango=max(lista_numeros)-min(lista_numeros)

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima=min(diccionario_edades.values())
ultimo_nombre=max(diccionario_edades)