"""
 TODO crear una primera funcion que calcule el precio de un viaje
     que tenga como parámetros la distancia, el precio de la gasolina
     y el consumo del coche. 
     Si no se le pasa el precio de la gasolina se le pasa por defecto 1.3€/l """


def calcular_precio_viaje(distancia, consumo, precio_gasolina = 1.3 ):
    """
    distancia: Distancia que se va a recorrer en KM
    consumo: Consumo del coche en l/100km
    precio_gasolina: Precio de la gasolina en €/l por defecto 1.3€/l

    return un numero que indica el precio del viaje
    """
    precio_viaje = (consumo * precio_gasolina * (distancia/100))
    print(f"El precio del viaje es de {precio_viaje:.2f} €")
    return round(precio_viaje,2)

if __name__ == "__main__" :
      ok = False

      # TODO Crear un validador con un decorador (@), o se puede usar una libreria para tipar,
      # para dentro de un par de clases
      while  not ok:
            try:
                  distancia = float(input("Introduce la distancia en kilometros que hay a tu destino: "))
                  ok = True
            except:
                  print("La distancia debe ser un número")

      ok =  False
      while not ok:
            try:
                  consumo = float(input("Introduce el consumo de tu coche: "))
                  ok = True
            except:
                  print("El consumo debe ser una cifra")
            
      ok = False
      while not ok:
            pregunta = input("¿Sabes el precio de la gasolina? S/N ")
            if pregunta == "S" or pregunta == "s":
                  precio_gasolina = float(input("Introduce el precio de la gasolina: "))
                  print(calcular_precio_viaje(distancia, consumo, precio_gasolina))
                  ok =True
            elif pregunta == "N" or pregunta == "n":
                  print(calcular_precio_viaje(distancia, consumo))
                  ok = True
            else:
                  print("Debes pulsar S ó N")