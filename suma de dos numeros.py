def sumar_numeros(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b

# Solicitar al usuario dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

resultado = sumar_numeros(num1, num2)
print(f"La suma de {num1} y {num2} es: {resultado}")
