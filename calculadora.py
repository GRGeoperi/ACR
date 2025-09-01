def resta (a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

#suma 
def suma(a, b):
    return a + b

def division(a, b):
    if b == 0:
        return "Error: División por cero no está permitida."
    return a / b

if __name__ == "__main__":
    print(f"División: 10/2 = {division(10, 2)}")
    print(f"Suma: 5 + 3 = {suma(5, 3)}")
    print(f"Resta: 10 - 5 = {resta(10, 5)}")
    print(f"Multiplicación: 4 * 6 = {multiplicacion(4, 6)}")

