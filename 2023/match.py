#Condicional if
serie="N-02"
# if serie=="N-01":
#     print("Samsung")
# if serie=="N-02":
#     print("Nokia")
# if serie=="N-03":
#     print("Motorola")
# else:
#     print("No existe ese producto")

'''Forma de realizar un switch en python'''
match serie:
    case "N-01":
        print("Samsung")
    case  "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe ese producto")
cliente={
    'nombre':'Raul',
    'edad':30,
    'ocupacion':'developer'
}

pelicula={
    'titulo':'Matrix',
    'ficha_tecnica':
        {
            'protogonista':'Keanu Reeves',
            'director':'Lana y Lilly Wachowski'
        }
    }

elementos=[cliente,pelicula,'libro']

for e in elementos:
    match e:
        case {
            'nombre':nombre,
            'edad':edad,
            'ocupacion':ocupacion
        }:
            print("Es un cliente")
            print(f"Nombre del cliente es {nombre} edad : {edad} y su  ocupacion es {ocupacion}")
        case {
            'titulo':titulo,
            'ficha_tecnica':
        {
            'protogonista':protagonista,
            'director':director
        }
        }:
            print("Es una pelicula")
            print(f"Titulo de la pelicula {titulo}, el protagonista es {protagonista}, el director es : {director}")
        case _:
            print("No se que es esto ... ")

