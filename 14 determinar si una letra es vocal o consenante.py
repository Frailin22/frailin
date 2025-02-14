print ("Este programa determina si una letra es vocal o consonante")
c = input("Escriba una letra: ")
vocales = ["a","e","i","o","u","A","E","I","O","U"]
if c in vocales:
    print("Es una vocal")
else:
    print("Es una consonante")