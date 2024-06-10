#TODO explicar que son los formatted strings
#TODO explicar todos los condicionales
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

