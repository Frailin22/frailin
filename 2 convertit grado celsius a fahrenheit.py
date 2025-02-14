#convertir de grado celsius a fahrenheit
# f = (c * 9/5) + 32;


def convertir(c):
    return (c * 9/5) + 32


n = float(input("Ingresa los grados celsius: "))
print(f"La convercion a grados fahraheit es: {convertir(n)}")