#TODO explicar que son los formatted strings
#TODO explicar todos los ¿¿¿condicionales??? operadores 
#TODO explicar que son las Tuplas y los diccionarios
#TODO crear una primera funcion que calcule el precio de un viaje
#     que tenga como parámetros la distancia, el precio de la gasolina
#     y el consumo del coche. Si no se le pasa el precio de la gasolina se le pasa por defecto 1.3€/l

#TODO explicar que son los formatted strings

#Los formatted strings permiten incluir expresiones dentro de una cadena de texto

nombre, apellido = "Pepito", "Pérez"
edad = 43
nota = 7.5842

#Con el operador % te aseguras pasar el valor formateado. 
# %s para cadenas de texto
# %d para enteros
# %f para números decimales
# %.número de dígitosf para números decimales con presisión fija

print("Mi nombre es %s %s y tengo %d años. Tengo una nota de %f que redondeando es %.2f" 
      %(nombre, apellido, edad, nota, nota))


#Usando str.format

print("Mi nombre es {} {} y tengo {} años. Tengo una nota de {} que redondeando es {:.2f}" 
      .format(nombre, apellido, edad, nota, nota))


#Con f-String

print(f"Mi nombre es {nombre} {apellido} y tengo {edad} años. Tengo una nota de {nota} que redondeando es {nota:.2f}") 


#TODO explicar todos los ¿¿¿condicionales??? operadores


#Operadores aritméticos + - * / % ** //

print(2+2)   # +  es el operador de suma
print(4-2)   # -  es el operador de resta
print(5*2)   # *  es el operador de multiplicación
print(10/3)  # /  es el operador de división
print(10%3)  # %  es el operador de módulo. Devuelve el resto de la división
print(2**3)  # ** es el operador de exponentes
print(10//3) # // es el operador Floor division. Nos da la parte entera del cociente de la división

print("Hola " + "Mundo") #El operador + tambien sirve para concatenar cadenas de strings


#Operadores de asignación

x = 5   # = es el operador de asignación. Aquí le asigna el valor 5 a la variable x 
x += 3  # += es lo mismo que x = x + 3
x -= 3  # += es lo mismo que x = x - 3
x *= 3  # += es lo mismo que x = x * 3
x /= 3  # += es lo mismo que x = x / 3
x %= 3  # += es lo mismo que x = x % 3
x //= 3 # += es lo mismo que x = x // 3
x **= 3 # += es lo mismo que x = x ** 3


#Operadores de comparación. Devuelven True o False

print(5 > 3)  # > es el operador de mayor que
print(5 < 3)  # < es el operador de menor que
print(5 == 3) # == es el operador de igual que
print(5 != 3) # != es el operador de no igual que
print(5 >= 3) # >= es el operador de mayor o igual que
print(5 <= 3) # <= es el operador de menor o igual que

print(1 is 1)     # devuelve True al ser 1 igual que 1
print(1 is not 2) # devuelve True al no ser 1 igual que 2

print("P" in "Pepe")     # devulve True al estar P en Pepe
print("p" not in "Pepe") # devuelve False ya que evalua si p no está en Pepe

#Operadores lógicos

print(3 > 2 and 7 > 5) #and devuelve True si las dos comparaciones son ciertas
print(2 > 3 or 7 > 5)  #or devuelve True si alguna de las comparaciones son ciertas
print(not 3 > 2)       #not devuelve lo contrario del resultado de la comparación


#TODO explicar que son las Tuplas y los diccionarios

# Las Tuplas son un conjunto de diferentes tipos de datos ordenados
# y que una vez creada no se puede modificar. Son inmutables.

mi_tupla = tuple() #Se puede definir usando su constructor
mi_tupla_dos = ("Pepe", 8, -5)  #Tambien se puede definir con los parentesis
print(type(mi_tupla_dos))

# Los Diccionarios es un conjunto de datos que se almacenan en pares clave:valor. Es Mutable

diccionario = dict() #Se puede definir usando su constructor
diccionario_dos = {"Nombre":"Pepe", "Apellido":"Pérez", "Edad":35}
print(diccionario_dos)