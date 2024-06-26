TODO explicar todos los ¿¿¿condicionales??? operadores


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