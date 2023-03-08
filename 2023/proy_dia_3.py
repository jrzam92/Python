#Metodo Index()
#Sirve para conocer cierto indice de un caracter

mi_texto="Hola que hay de nuevo"
res = mi_texto[9]
print(res)
res = mi_texto[-4]
print(res)
mi_texto="Hola que hay de nuevo"
#La busqueda la hace de izquierda a derecha 
#dando asi la primera letra que encuentra 
res=mi_texto.index("o")
print(res)
#La busqueda la hace de  derecha a izquierda  
#dando asi la primera letra que encuentra 
mi_texto="Hola que hay de nuevo"
res = mi_texto.rindex("o")
print(res)
print("=======")
palabra = "ordenador"
res=palabra.index("n")
print(res)
print("=======")
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
res=frase.index("práctica")
print(res)

#Extraccion de caracteres Slice o substring 
print("=======")
texto="ABCDEFGHIJKLMNOPQRSTUVWzYZ"

frag=texto[2]
print(frag)#Se obtiene la letra C

texto="ABCDEFGHIJKLMNOPQRSTUVWzYZ"
frag=texto[2:]
print(frag)#Toma todo desde el indice 2(C) ->CDEFGHIJKLMNOPQRSTUVWzYZ 

texto="ABCDEFGHIJKLMNOPQRSTUVWzYZ"
frag=texto[:5]
print(frag)#Toma los primero 5 indices

texto="ABCDEFGHIJKLMNOPQRSTUVWzYZ"
frag=texto[2:10:3]
print(frag)

texto="ABCDEFGHIJKLMNOPQRSTUVWzYZ"
frag=texto[::3]
print(frag)

#Forma inversa de obtener la cadena 
texto="ABCDEFGHIJKLMNOPQRSTUVWzYZ"
frag=texto[::-1]
print(frag)

frase = "Controlar la complejidad es la esencia de la programación"
frag=frase[0:9]
print(frag)


#Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
frag=frase[8::3]
print(frag)
print("=======")
# Metodos de string 
# upper()-> pasa a mayusculas 
# lower()-> pasar a minusculas 
# split()-> separalo en partes(lista)
# join()-> unir items usando separador
# find()-> encontrar un substring
# replace(old, new) -> replaza un subs

texto="Este es un texto de Jose Raul" 
res=texto 
print(res)
res=texto.upper() 
print(res)
res=texto.lower() 
print(res)
res=texto.split() #Lista o arreglo es su separacion
print(res)
res=texto.split(" ") #Lista o arreglo es su separacion por caracter
print(res)
a="Aprender"
b="python"
c="es"
d="genial"
texto=" "
res=texto.join([a,b,c,d]) 
print(res)
res=res.replace("Aprender","Estudiar") 
print(res)
res=texto.find("a") #
print(res)
print("=======")

# Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
lista_palabras = ["La","legibilidad","cuenta."]
espacio=" "
res=espacio.join(lista_palabras)
print(res)

# Reemplaza en la siguiente frase:
# "Si la implementación es difícil de explicar, puede que sea una mala idea."
# los siguientes pares de palabras:
# "difícil" --> "fácil"
# "mala" --> "buena"
# y muestra en pantalla la frase con ambas palabras modificadas.

frase="Si la implementación es difícil de explicar, puede que sea una mala idea."
res=frase.replace("difícil","fácil").replace("mala","buena")
print(res)

#Propiedades de string pueden ser inmutables 
#Los string pueden concatenarse con un signo +
# o bien se puede obtener una multiplicacion de string 
# Los saltos de linea pueden entrar con tres """

# Ejercicio:
#Cambio de variables 
_xnombre="Carina"
_xnombre="Karina"
n1="Raul"
n2="Jose"

print(n1+" "+n2)
res=n1+" "
print(res*3)

poema="""Mil pequeños peces 
blancos como si
hirviera el color de agua"""
print(poema)
print("Agua existe en poema")
print("agua" in poema)
print("Fuego no existe en poema")
print("Fuego" not in  poema)

word="peces"
res=f"peces existen en poema:{word in poema}"
print(res)

poema="Hola Mundo Python!!!!"
print(len(poema))

# Listas
print("=====================")
print("=======LISTAS=======")
print("=====================")
# Qué significa que un método actúe “en el lugar” (in-place)
    #R:===> Que transforma un obejto sin retornar un resultado
mi_lista=["a","b","c"]
print(type(mi_lista))#Tipo
print(len(mi_lista))#logitud
print(mi_lista[0])#Indice 0
print(mi_lista[0:2]) #indice 0 a 2 caracteres
mi_lista2=["d","e","f"]
mi_lista3=mi_lista+mi_lista2
print(mi_lista3)#concatenacion de listas
#Alteracion de los elementos de la lista

mi_lista3[0]="alpha"
print(mi_lista3)

mi_lista3.append('g') #Se agrega un nuevo elemento
print(mi_lista3)

mi_lista3.pop()#Se elimina el ultimo elemento 

elemento_eliminado=mi_lista3.pop(0)#Se le puede eliminar por el indice 
print(mi_lista3)
print(elemento_eliminado)

lista=['p','a','r','s','c']
lista.sort()#Se tiene que poner fuera para que lo pueda imprimir ordenadamente
print(lista)
lista.reverse()#pone la lista en reversa 
print(lista)
new_list=lista.sort()
print(new_list)#No devuelve nada por lo que sale None en consola
print(type(new_list))

#Diccionarios
#Coleccion de conceptos y sus definiciones [key:value]
# Cuando combiene usar diccionario y : list

# diccionario se usa cuando solo se quiere conocer sin ningun orden 
# una lista es necesaria ordenar para ver sus valores 
# Ejemplo 
mi_dic={'c1':'valor1','c2':'valor2','c3':'valor3'}

print(type(mi_dic))

print(mi_dic)

res=mi_dic['c1']
print(res)

cliente={"nombre":"Juan","apellido":"Fuentes","peso":"75","talla":"175"}

print(f"El cliente: \'{cliente['nombre']} {cliente['apellido']}\' mide: \'{cliente['talla']}\' cm y pesa: \'{cliente['peso']}\' Kg")


diccionario1={'c1':55, 'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
# Imprime del diccionario con la clave 2 en la posicion 1
print(diccionario1['c2'][1])
print(diccionario1['c3']['s2'])

diccionario2={'c1':['a','b','c'],'c2':['d','e','f']}
print(diccionario2['c2'][1].upper())#Debe de tomar la clave 2 la letra 'e' en mayuscula
print(diccionario2['c1'][0].upper().replace('A', 'Hello'))

diccionario3={1:'a',2:'b'}
print(diccionario3)

diccionario3[3]='c'

print(diccionario3)

diccionario3[2]='B'

print(diccionario3)

print(diccionario3.keys())
print(diccionario3.values())
print(diccionario3.items())

mi_dic={ 
'nombre':'Karen',
'apellido':'Jurgens',
'edad':35,
'ocupacion':'Periodista' 
}
# Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.

# Si el valor 300 cambiara en el futuro, el código debería funcionar igual para devolver el valor que se encuentre en esa misma posición. Para ello, deberás hacer referencia a los nombres de las claves y/o índices según corresponda.
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])


mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic['nombre']='Karen'
mi_dic['apellido']='Jurgens'
mi_dic['edad']=36
mi_dic['ocupacion']='Editora'
mi_dic['pais']='Colombia'

#Tuple son inmutables parecidas a las listas
#Limitantes, ocupan menos espacio de memoria 
#Esturcturas que no se deben de modificar --> son a prueba de daños 

mi_tuple=(1,2,3,4)
print(type(mi_tuple))
mi_tuple=1,2,3,4 #sin parentesis
print(type(mi_tuple))

#Puede tener diferentes tipos dentro
#Se puede tomar el indice 
print(mi_tuple[0])

#Al ser inmutable como los string no es posible cambar el valor 

#Si se puede realizar anidaciones 
mi_tuple=(1,2,(10,20),4)
print(mi_tuple[2][0])#Seleccionar el 3er indice el primer valor

#Realizando casting 
mi_tuple=list(mi_tuple)
print(type(mi_tuple))
mi_tuple=tuple(mi_tuple)
print(type(mi_tuple))

#Asignancion de variables para las Tuple
t=(1,2,3)#Tiene que tener las mismas variables para sus correxpondientes valores 
x,y,z=t
print(x,y,z)

#Conociendo la longitud del tuple
t=(1,2,3) 
print(len(t))
print(t.count(0))#regresa el numero de veces de occurrencia dentro de la tupla
print(t.index(1))#Da el valore del indice de la tupla 

#SETS son coleccion de elementos como una lista 
# usando la palabra set pasa dentro de un arreglo  o las {<1,1,1,1>} pasa directo 
#Son inmutables por lo que ojo al respecto 
mi_set=set([1,2,3,4,5,6])
print(type(mi_set))
print(mi_set)

mi_set=(['a','b','c'])
print(mi_set)

mi_set={1,2,3,4}
print(mi_set) 

# print(mi_set[{0}])#'set' object is not subscriptable
mi_set={1,2,3,4,1,2,3,4,1,2,3,4}
print(mi_set) 

#Dentro de los sets no pueden agregarse diccionarios o listas o arreglos internamente

#solo se puede agregar tuplas ya que igual son inmutables 
mi_set={1,2,3,4,(5,6,7,10)} #(5,6,7,10) tupla dentro de set 


print(mi_set)
print(len(mi_set))#Se tiene la longitud del set 

print(2 in mi_set)#El dos se encuentra en el set -> true

#Realizando la union de sets
s1={1,2,3}
s2={4,5,6}
s3=s1.union(s2)
print(s3)

s1={1,2,3}
s1.add(4)#Agregando el 4 
print(s1)

s1.remove(2)#Remueve el elemento deseado 
print(s1)
s1.discard(3)#Descarta el numero
print(s1)
s1.pop()#Elimina aleatoriamente
print(s1) 

s1.clear()
print(s1)

#Booleanos, verdaderos o falsos 

mi_bool=5<4
# > mayor que 
# < menor que
# >=mayor o igual que
# <=menor o igual que 
# == igual que
# != diferente que
#Es necesario poner correctamente las variables 
#Las que se llaman banderas o bien variables de memoria 
#que pueden ayudar a leer mejor lo que se quiere hacer o expresar
#No esta demas hacer una nota de lo que se esta haciendo en el metodo

lista=['ventanas','perros','parques','circos','rutas']
mi_bool='ventas' in lista
print(mi_bool)
mi_bool='pizarrones' not in lista
print(mi_bool)
#Los booleanos son cuestiones logicas para hacer validaciones correctas

var1=True
var2=False
print(type(var1))
print(f'El valor de la varible var 1 es ...{var1}')

isnumero=5>2+3
print(type(isnumero))
print(f'la comparacion de 5>2+3 es : {isnumero}')
isnumero=5==2+3
print(type(isnumero))
print(f'la comparacion de 5==2+3 es : {isnumero}')
isnumero=5>=2+3
print(type(isnumero))
print(f'la comparacion de 5>=2+3 es : {isnumero}')
isnumero=5!=2+3
print(type(isnumero))
print(f'la comparacion de 5!=2+3 es : {isnumero}')
isnumero=bool(5<6) #Casteo directamente 
print(type(isnumero))
print(f'la comparacion de 5<6 es : {isnumero}')


# Verifica si 17834/34 es mayor que 87*56 y muestra el resultado (booleano) en pantalla utilizando print()
a=17834/34
b=87*56
c=bool(a>b)
print(c)
# Verifica si la raíz cuadrada de 25 es igual a 5 y muestra el resultado (booleano) en pantalla utilizando print()
numero=25
raiz=numero**0.5
isRaiz=bool(raiz==5)
print(isRaiz)

palabra='exito'

print(palabra[4])

redes = ['“YouTube”',' “Facebook”', '“Twitter”', '“Whatsapp”']
redes.sort()
print(redes)
