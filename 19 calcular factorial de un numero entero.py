print ("Este programa calcula el factorial de un numero entero")

def calcular (x):
    if x >= 0:
        f = 1
        for i in range(1,x+1):
            f = f * i
            return f
        else:
            return 0
        
        n = int(input("Escriba un numero: "))
        print(f"El factorial del numero {n} es: {calcular(n)}")
