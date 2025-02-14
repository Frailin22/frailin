print ("Este programa te pide dos numeros y define cual es el mayor")
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
if a == b:
    print("Los numeros son iguales")

else:
    if a > b:
        print("El numero mayor es: " ,a)
    else:
        print("El numero mayor es: " ,b)