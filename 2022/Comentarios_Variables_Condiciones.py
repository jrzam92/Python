#Comentario sencillo 
"""
Tutorial de GD script lenguaje parecido a python
"""

#Variables
_valorA=10;
_string="Hello World"
#Imprimir en consola
print("Hola Mundo!!!")
print(_valorA)
print(_string)
#####=========Nuevo ejercicio==========############
edad=20
#Validar la mayoria de edad y dejar pasasr en caso de ser mayor a 18, de lo contrario, no dejar pasar 
if edad>=18:	
    print("Es mayor de edad "+str(edad))

else:
    print("No puede pasar porque tiene "+str(edad)+" y es menor de edad")
_name="Raul"
print("Tu nombre es: "+ str(_name))
_name=True
print("Tu nombre es: "+ str(_name))
"""
Criterios:
1. Si la edad es menir a 18 => Eres adolescente
2. Si la edad es mayor a 18 a 34-> Eres chavo ruco
3. Si la edad es menor a 50 y mayor a 35 -> eres Adulto Joven
4. Si la edad es menor a 60 y mayor a 50 -> eres Adulto Responsable
5 Si la edad es mayor a 75 -> eres anciano
"""
_age=28

if _age < 18  :
    print("Eres adolescente")
elif _age >=18 and _age < 35:
     print("Eres chavo")
elif _age >=35 and _age < 50:
    print("Eres chavo ruco")
elif _age >=50 and _age < 75:
    print("Eres Adulto")  	
else :   
   	print("Eres Anciano")  
    