
def sumar(datos):
       suma = 0
       for x in datos:
              suma += x

       return suma
def restar(datos):
       resta = 0
       for x in datos:
              if resta == 0:
                     resta = x
              else:
                     resta -= x

       return resta

def multiplicacion(datos):
       multi = 0
       for x in datos:
              if multi == 0:
                     multi = x
              else:
                     multi *= x

       return multi


def division(datos):
       dividir = 0
       for x in datos:
              if dividir == 0:
                     dividir = x
              else:
                     dividir /= x

       return dividir

print ('BIENVENIDOS A LA CALCULADORA'
       '\nPODRA REALIZAR SOLO 4 TIPOS DE OPERACION\n'
       '------------------------------------------\n'
       'Elija un de las siguientes operaqciones a realizar\n'
       'A) Suma\n'
       'B) Resta\n'
       'C) Multiplicacion\n'
       'D) Divición\n'
       '---------------------------------------------------\n'
       'Escoge un opción escribiendo una de las letras')

opcion=input(">")

print('indique la cantidad de numeros para efectuar la operación')

cantim = int(input('> '))

if cantim >= 2:
       if opcion == 'A':
              x=0
              dato = []
              while x < cantim:

                     datos = int(input("INGRESE EL "+ str(x + 1)+ " NUMERO PARA SUMAR---> "))
                     dato.append(datos)
                     x += 1

              operaciosuma = sumar(dato)
              print("LA SUMA ES = " , str(operaciosuma))
       elif opcion == 'B':
              x=0
              dato = []
              while x < cantim:
                     datos = int(input("INGRESE EL "+ str(x + 1)+ " NUMERO PARA RESTAR --------> "))
                     dato.append(datos)
                     x +=1
              operacioresta = restar(dato)
              print("LA RESTA ES = ", str(operacioresta))

       elif opcion == 'C':
              x=0
              dato = []
              while  x< cantim:
                     datos = int(input("INGRESE EL "+ str(x + 1)+"NUMERO PARA MULTIPLICAR -------->"))
                     dato.append(datos)
                     x +=1
              operacionmulti = multiplicacion(dato)
              print("LA MULTIPLICACION ES = ", str(operacionmulti))
       elif opcion == 'D':
              x = 0
              dato = []
              while x < cantim:
                     datos = int(input("INGRESE EL " + str(x + 1) + "NUMERO PARA DIVIDIR -------->"))
                     dato.append(datos)
                     x += 1
              operaciondivi = division(dato)
              print("LA DIVISION ES = ", str(operaciondivi))






