#if condicion:
    # accion
#elif condcion:
    # accion
#else

print('======================')
print("1. Ejercicio")
if 10 > 9:
    print('Es correcto...')

print('======================')
print("2. Ejercicio")
if 5== 3:
    print('Son iguales')
else:
    print('No es correcto')

print('======================')
print("3. Ejercicio")

mascota='perro'
if mascota =='perro':
  print('Tienes un perro')
elif mascota =='gato':
  print('Tienes un gato')
elif mascota =='pez':
  print('Tienes un pez')
else:
  print('No se que animal tienes')

print('======================')
print("4. Ejercicio")

edad=16
calificacion=9
if edad < 18:
        print('Eres menor de edad')
        if calificacion>=7:
          print('Aprobado')
        else:
          print('No Aprobado')
else:
    print('Eres adulto')

print('======================')
print("5. Ejercicio")
num1 = input("Ingresa un número:")
num2 = input("Ingresa otro número:")
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
elif num1 == num2:
    print(f"{num1} y {num2} son iguales")

print('======================')
print("6. Ejercicio")

edad = 16
tiene_licencia = False
if edad > 18:
    print("Puedes conducir")
elif edad ==16:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
else:
    print("No puedes conducir. Necesitas contar con una licencia")

print('======================')
print("7. Ejercicio")
habla_ingles = True
sabe_python = False

if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif habla_ingles==False and sabe_python==False:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif habla_ingles==False and sabe_python==True:
    print("Para postularte, necesitas tener conocimientos de inglés")
elif habla_ingles==True and sabe_python==False:
    print("Para postularte, necesitas saber programar en Python")