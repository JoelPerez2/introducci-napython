def determinar_signo(num: int) -> str:
    """Determina si un número es positivo, negativo o cero."""
    if num > 0:
        return "Positivo"
    elif num < 0:
        return "Negativo"
    else:
        return "Cero"

num = float(input("Ingrese un número: "))

resultado = determinar_signo(num)
print(f"El número {num} es {resultado}.")