def suma(a, b):
    return a + b

if __name__ == "__main__":
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    resultado = suma(num1, num2)
    print(f"La suma de {num1} y {num2} es: {resultado}")