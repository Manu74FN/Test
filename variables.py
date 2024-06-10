#Tipos de datos numericos
entero = 1

print(type(entero/2))

decimales = 6.6
print(type(decimales))

#Tipo de datos strign

cadena = "cadena de texto"
print(type(cadena))

cadena_evaluable = f"el numero entero es {entero}"
print(cadena_evaluable)
print(f"el numero entero es {entero}")

verdad = True

condicion = entero == decimales
print(condicion)

#Listas

lista = [cadena, entero, decimales, cadena_evaluable, verdad, [1,2]]
print(type(lista))

for i in lista:
    print(f"el valor de \"{i}\" tiene el tipo {type(i)}")
    


