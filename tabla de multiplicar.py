def tabla_multiplicar(numero: int):
    """Genera la tabla de multiplicar de un número del 1 al 10."""
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número: "))

tabla_multiplicar(numero)