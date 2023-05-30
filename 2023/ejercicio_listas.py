#En este ejercicio lo que realizara es la separacion de la letra o caracter de la palabra videojuegos 
lista=[item for item in 'videojuegos']
print(lista)

#En este ejercicio se esta realizando un for anidado a una condicion en la que si es menor o mayor ya a poner el valor de no 
lista=[n if n*2<10  else 'no' for n in range(0,21,2) ]
print(lista)

#Ejercicio que realiza la conversacion de pies a metros pasadole una lista de valores y despues realizando 
#la operacion de la conversion en el for imprimiendo asi los valores 
pies=[10,20,30,40,50]
metros=[p*3.281 for p in pies]
print(metros)

#ejercicio para elevar al cuadrado 
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado =[valor**2 for valor in valores]

#ejercicio en donde se puede obtener tanto los pares como los impares 
valores = [1, 2, 3, 4, 5, 6, 9.5] 
valores_pares=[n if n%2==0 else f'{n} es impar' for n in valores]
print(valores_pares)
#Ejercicio donde se encuentran los pares solamente pero fijate que se puede realizar la condicion al final del for 
valores = [1, 2, 3, 4, 5, 6, 9.5] 
valores_pares=[n for n in valores if n%2==0]
print(valores_pares)

#Ejercicio en donde se realiza la conversion de grados farenheit a  grados_celsius 
temperatura_fahrenheit = [32, 212, 275]
grados_celsius=[(grados_fahrenheit-32)*(5/9) for grados_fahrenheit in  temperatura_fahrenheit]