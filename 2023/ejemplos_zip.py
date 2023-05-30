nombres=['juan','pablo','ana']
edades=[25,42,33]
ciudades=['mexico','madrid','barcelona']
#El zip funciona para generar tuplas 
combinada=zip(nombres,edades,ciudades)
lista=list(combinada)
print(lista)
print('===============')
print('===============')
print('===============')
for nombre,edad,ciudad in lista:
    print(f"{nombre} tiene {edad} anios y vive en {ciudad}")
print('===============')
print('===============')
print('===============')
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

lista=list(zip(capitales,paises))

for capital,pais in lista:
    print(f'La capital de {pais} es {capital}')
print('===============')
print('===============')
print('===============')
marcas =['nintendo','sony','microsoft']
productos =['switch','ps5','xbox s']
mi_zip=list(zip(marcas,productos))
for marca,producto in mi_zip:
    print(f"La marca es {marca} y vende: {producto}")

print('===============')
print('===============')
print('===============')
#El patron a usar el zip es que los combina el cual esto hace que dependiendo del orden este va a funcionar de diferente manera 
espanol = ['uno','dos','tres','cuatro','cinco']
portugues = ['um','dois','três','quatro','cinco']
ingles = ['one','two','three','four','five']
 

numeros=list(zip(espanol,portugues,ingles))
for i in numeros:
    print(i)
