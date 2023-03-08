
#Se puede imprimir con ->'<- y con ->"<- 
print('I said "hocus pocus" to the wizard.')
#Usando comillas dobles 
print("I said \"hocus pocus\" to the wizard.")
#Usando 3 comillas dobles se puede quitar
#el error de en medio de las dobles comillas
print("""I said "hocus pocus" to the wizard.""")
#Concatenate strings
print("I love"+" Python!")
#variables y enteros dentro de un string
algo="high "+str(5)
print(algo)
#Se puede multiplicar las palaras que uno requiera 
a='eek! '*5
print(a)

my_string = 'fugu-sashi'
print (my_string)
print (my_string.upper())
print (my_string.capitalize())
print (my_string.title())
print (my_string[::-2])
print (my_string[::-1])
print (my_string[1::3])
print ( my_string[::2])
print ( my_string[5:])
print(my_string[:4])
print(my_string[5:10])
print(my_string[2:4])
print(my_string[-1])
print(my_string[len(my_string)-1])
print( len(my_string))
print(my_string[0])
print( my_string[3])
print(my_string[0])
#Listas
my_list=[]
my_list.append('chopsticks')
my_list.append('soy sauce')
my_list.append('wasabi')
my_list.append('fugu')
my_list.append('sake')
my_list.append('apple pie')
print(my_list)
my_list[1]='dark soy sauce'
print(my_list)
del my_list[-1]
print(my_list)
my_list[2]
print(my_list)
my_list[-1]
print(my_list)
my_list[:2]
print(my_list)
my_list[2:]
print(my_list)
#Se crea lista nueva 
my_list2 = ['ramen', 'shiitake mushrooms']
print(my_list2)
#Se agrega lista 2 a mi lista 
my_list += my_list2
print(my_list)
#Ordena la lista
my_list.sort()
print(my_list)
#Remueve un elemento de la lista
my_list.pop(0)
print(my_list)
#Area de tuplas
my_tuple=('555', 'EATFUGU')
print(my_tuple)
my_tuple[0]
print(my_tuple)
my_tuple[1]
print(my_tuple)
area_code, number = my_tuple
print(area_code)
print(number) 
print(list(my_tuple))
#Area de diccionario
my_dictionary={'ramen': 5.0, 'fugu': 100.0}
print(my_dictionary)
print(my_dictionary['ramen'])
print(my_dictionary['fugu'])
my_dictionary['chopsticks']=7.50
my_dictionary['sake']=19.95
print(my_dictionary['chopsticks'])
print(my_dictionary['sake'])
print(my_dictionary)
#Area de ciclo for
for count in range(1,6):
    print(count)
    
print(range(1,6))

#Ejercicio pratico
#Realizando compras de productos
shopping=['ipad','xbox','ps5','switch','pc','smartwatch','phone']
price={'ipad':15280.5,'xbox':8542.23,'ps5':16504.95,'switch':9452.45,'pc':55000,'smartwatch':7551.32,'phone':23245.65}
total=0.00

for product in shopping:
    total+=price[product]
print('El total de la compra fue:'+str(total),'que tenga excelente dia!!!')

score = 100
health = 60
damage = 50
fugu = 'tasty'
print('(score != 100) ->',str(score != 100))
print('(health - damage > 0) ->'+str(health - damage > 0))
print ("""'(fugu == 'tasty') ->'""",str(fugu == 'tasty'))
