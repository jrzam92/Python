"""
Práctica Operadores de Comparación 1
Crea dos variables (num1 y  num2) con los valores 36 y 17 respectivamente. 
Verifica si num1 es mayor o igual que num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool
"""
print("Ejercicio 1")
print("==================")
num1=36 
num2=17
mi_bool=num1>=num2
print(f"num1>=num2 ->{mi_bool}")

print("==================")

"""
Práctica Operadores de Comparación 2
Crea dos variables (num1 y  num2):

Dentro de num1, almacena el resultado de la operación raíz cuadrada de 25

Dentro de num2, almacena el número 5.

Verifica si num1 es igual a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool.
"""
print("Ejercicio 2")
print("==================")

num1=25**.5 #Raiz cuadrada
num2=5
mi_bool=num1==num2
print(f"num1==num2 ->{mi_bool}")

print("==================")


"""
Crea dos variables (num1 y  num2):

Dentro de num1, almacena el resultado de la operación 64 x 3

Dentro de num2, almacena el resultado de la operación 24 x 8

Verifica si num1 es diferente a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool.
"""
print("Ejercicio 3")
print("==================")
num1=64*3
num2=24*8
mi_bool=num1!=num2
print(f"num1!=num2 ->{mi_bool}")

print("==================")
print("Ejercicio 4")
print("==================")
mi_bool=4<5<6
print(f"{mi_bool}")
print("==================")
#OPERADORES LOGICOS 
print("Ejercicio 5")
print("==================")
mi_bool=(4<5) and (5== 2+3)
print(f"{mi_bool}")
print("==================")

print("Ejercicio 6")
print("==================")
mi_bool=(55==55) and ('perro'== 'perro')
print(f"(55==55) and ('perro'== 'perro') {mi_bool}")
print("==================")
print("Ejercicio 7")
print("==================")
mi_bool=(10==10) or (3== 3)
print(f"(10==10) or (3== 3) {mi_bool}")
print("==================")
print("Ejercicio 8")
print("==================")
mi_bool=(1==10) or (3== 2)
print(f"(1==10) or (3== 2) {mi_bool}")
print("==================")
print("Ejercicio 9")
print("==================")
texto="esta frase es breve"
mi_bool=(('frase'in texto )or ('python' in texto))
print(f"('frase'in texto )or ('python' in texto) {mi_bool}")
print("==================")
print("Ejercicio 10")
print("==================")
mi_bool=not ("a"=="a")
print(f"not (\"a\"==\"a\") {mi_bool}")
print("==================")
print("Ejercicio 10")
print("==================")
mi_bool=not ("a"!="a")
print(f"not (\"a\"!=\"a\") {mi_bool}")
print("==================")

"""
Práctica Operadores Lógicos 1
Crea tres variables (num1 ,  num2 y num3):

Dentro de num1, almacena el valor 36

Dentro de num2, almacena el resultado de la operación 72/2

Dentro de num3, almacena el valor 48

Verifica si num1 es mayor que num2, y menor que num3. Almacena el resultado de dicha comparación en una variable llamada mi_bool.
"""
print("Ejercicio 11.1")
print("==================")
num1=36
num2=72/2
num3=48
mi_bool=(num1>num2) and (num1<num3)
print(f"(num1>num2) and (num1<num3) -> {mi_bool}")#false
print("==================")
print("Ejercicio 11.2")
print("==================")
num1=36
num2=72/2
num3=48
mi_bool=(num1>num2) or (num1<num3)
print(f"(num1>num2) and (num1<num3) -> {mi_bool}")#true

"""

Práctica Operadores Lógicos 3
Verifica si las palabras almacenadas en las siguientes variables:

palabra1 = "éxito", y

palabra2 = "tecnología"

no se encuentran en la frase a continuación, y almacena el resultado de esta comprobación (un booleano) en una variable llamada mi_bool:

"Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"

Elon Musk
"""
print("Ejercicio 11.3")
print("==================")
frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool=not ((palabra1 in frase) and (palabra2 in frase ))
print(f"(palabra1 in frase) and (palabra2 in frase ) -> {mi_bool}")
print("==================")