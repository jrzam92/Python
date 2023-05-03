print("===========")
print("Ejercicio 1")
lst_NamesCharacterVideoGames= {'Goku','Vegeta','Sonic','Mario','Zelda','Batman','Yoshi','Pikachu'}

print("Lista de nombres de personajes de videojuegos")
for character_name in lst_NamesCharacterVideoGames:
    print(character_name)
print("===========")
print("Ejercicio 2")
arrayNumber=[1,2,3]

for number in arrayNumber:
    print(number)

print("===========")
print("Ejercicio 3")
listaChars=['a','b','c','d']
print("Index + 1  == letra")
for char in listaChars:
    num_letra=listaChars.index(char)   + 1
    print(f"{num_letra}- Letra {char}")
print("===========")
print("Ejercicio 4")
MarioCharacters={'Mario','Peach','Luigi','Yoshi','Toad'}
for names in MarioCharacters:
    if names.endswith('i'):
        print(names)
    else:
        print(f"Nombres que no terminan en i :{names}")
        
print("===========")
print("Ejercicio 5")
numeros=[1,2,3,4,5]
mi_valor=0
for numero in numeros:
    mi_valor=mi_valor+numero
    print(mi_valor)

print("===========")
print("Ejercicio 6")
palabra ='Super Smash Bros'
for letra in palabra:
    print(letra)
print("===========")
print("Ejercicio 7")
print("=====Valores de 'a'======")
for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
print("=====Valores de 'b'======")
for a,b in [[1,2],[3,4],[5,6]]:
    print(b)
print("====Valores de 'a,b'=======")
for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

print("===========")
print("Ejercicio 8")    
#loop con diccionarios
dictionary={'key1':'Goku','key2':'Vegeta','key3':'Trunks','key4':'Gotenk'}

print("======Diccionario Dragon Ball Character=====")
for a,b in dictionary.items():
    print(a,b)

print("===========")
print("Ejercicio 9") 
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for num in lista_numeros:
    
   
    if(num% 2 == 0):
        suma_pares+=num
        print("Valores pares")
        print(suma_pares)
    elif(num% 2 == 1 ):
        suma_impares+=num
        print("Valores imapres")
        print(suma_impares)