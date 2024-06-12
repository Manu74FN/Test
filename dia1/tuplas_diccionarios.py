#TODO explicar que son las Tuplas y los diccionarios

# Las Tuplas son un conjunto de diferentes tipos de datos ordenados
# y que una vez creada no se puede modificar. Son inmutables.

#Se puede definir usando su constructor
mi_tupla = tuple(["1",2,3]) 

#Tambien se puede definir con los parentesis
mi_tupla_dos = ("Pepe", 8, -5) 

print(type(mi_tupla_dos))

#expandible
mi_tupla = mi_tupla.__add__(tuple("add")) 

print(mi_tupla)


# Los Diccionarios es un conjunto de datos que se almacenan en pares clave:valor. Es Mutable

#Se puede definir usando su constructor
diccionario = dict()

diccionario_dos = {
    "Nombre":"Pepe"
    ,"Apellido":"Pérez"
    ,"Edad":35
}
print(diccionario_dos)

diccionario_final = {
    "[1]" :"paco"
}

print(diccionario_final["[1]"])