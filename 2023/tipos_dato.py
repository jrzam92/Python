#Variables
#Espacio de memoria que se guarda cierto contenido

# str("Hola") #textos
# int(123) #numeros enteros
# float(150.213) #numeros decimales
# list("mario","luigi","toad","sonic","tales","yoshi") #lista de elementos
# dict({"color":"rojo","color":"azul"}) #diccionario
# tuple("lun","martes","mier","juev","view") #tuplas
# set({'a','b','c'}) #elemento seteable
# bool(true) #booleano

#TIPOS DE STRINGS 

nombre =str("Raul")
edad=int(10)
print("Persona: "+nombre + "  Edad: " + str(edad))
nombre =str("Jose")
edad=int(30)
print("Persona: "+nombre + "  Edad: " + str(edad))

# SE COMENTA SOLO PARA QUE EN CONSOLA NO APAREZCA EL INPUT

# nombre =input(str("Cual es tu nombre: "))
# edad=(input(str("Cual es tu edad: ")))
# print("Persona: "+nombre + "  Edad: " + str(edad))

#RECOMENDACIONES

# Tiene que ser legible facil de leer 
# Esto para poder validar para si mismo que quiere decir 
# Te haces el favor a ti y a otros para leer el codigo o lo que trataste de hacer ahi 
# Regla quitar los caracteres como acentos o 'ñ' ya que solo es buena practica 
# Dentro de las variables no es nada practico poner palabras clave 

#TIPOS DE NUMERO ENTERO Y DECIMAL 

numero_entero=int(10)
numero_decimal=float(12.36)

total=numero_decimal+numero_entero
print("La suma de un numero entero \""+str(numero_entero)+"\"  con un numero decimal \""+str(numero_decimal)+"\" tiene un total de : \""+str(total)+"\"")

#CONVERSIONES 

#Implicitas y Explicitas

num1=29
num2=30.6
#Imprimiendo el numero de dato
print("Validacion de tipo numero entero y  decimal")
print(type(num1))#=>int
print(type(num2))#=>float
total=num1+num2#=>float
print(str("Total de num1 y num2 es: ")+str(float(num1) + int(num2)))
#Imprimiendo el numero de dato en total 
print(type(total))
print("=======")
print("=======")
print("Validicacion de num2")
print(num2)
print(type(num2))
#Se realiza la convercion
print("=======")
print("===Conversion de num2 a int ===")
num2=int(num2)
print(num2)
print(type(num2))
print("=======")
print("=======")
# print("Conversion edad de int a string")

# edad=input("Dime tu edad ")
# print(type(edad))
# edad=int(edad)
# type_edad=type(edad)
# print(type_edad)
# new_edad=1+edad
# print("Tu nueva edad va a ser "+ str(new_edad))
# print("=======")
# print("=======")

#FORMATO DE CADENAS 
nombre_carro="Beat"
modelo_carro=2018
marca_carro="Chevrolet"
tipo_carro="Deportivo"
placa_carro="L14-ASE"
print("Formato largo: .format")
print("Mi auto es \"{}\" la marca es \"{}\" del año \"{}\" con un tipo \"{}\" con una placa  \"{}\" ".format(nombre_carro,marca_carro,modelo_carro,tipo_carro,placa_carro))
print("Formato corto: f\"<contenido>\"")
print(f"Mi auto es \"{nombre_carro}\" la marca es \"{marca_carro}\" del año \"{modelo_carro}\" con un tipo \"{tipo_carro}\" con una placa  \"{placa_carro}\" ")

#OPERADORES MATEMATICOS
x=6
y=2
z=7

print(f"{x} mas {y} es igual a {x+y}")
print(f"{x} menos {y} es igual a {x-y}")
print(f"{x} por {y} es igual a {x*y}")
print(f"{x} dividido {y} es igual a {x/y}")

#Division al piso
print(f"{z} dividido al piso de {y} es igual {z//y}")

#modulo -> es el sobrante de la division : se usa mucho para sacar numeros pares e impares 
print(f"{z} modulo de {y} es igual a {z%y}")

#Potencia de un numero
print(f"{x} elevado a la {y} es igual a {x**y}")
print(f"{x} elevado a la {3} es igual a {x**3}")

#Raiz cuadrada
print(f"La raiz cuadrada de {x} es {x**0.5} ")

########
#Redondeo
a=float(257.23)/float(78.21)
b=round(a)
print("primera operacion")
print(f"El redondeo de : {a} es {b}")
a=float(450.23)/float(258.364)
print(type(b))
b=round(a,2)
print("segunda operacion")
print(f"El redondeo de : {a} es {b}")
print(type(b))

