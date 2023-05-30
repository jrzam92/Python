monedas=5
print("Ejemplo1 =============")
while monedas>0:
    print(f"Tengo {monedas} monedas")
    monedas-=1
else:print("No tengo mas dinero")


print("Ejemplo2 =============")
resp='s'
while resp=='s':
    resp=input("Quieres salir?(s/n)")
    if resp=='n':
        print("Gracias vuelve pronto!!!")
        break
# else:
#     print('Gracias')


nombre = input("Tu nombre:")
for letra in nombre:
    print(letra)


numero = 10
while numero>=0:
    print(f"{numero}")
    numero-=1


    