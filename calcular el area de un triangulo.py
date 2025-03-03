def calcular_area_triangulo(base: float, altura: float) -> float:
    """Calcula el área de un triángulo dado su base y altura."""
    return (base * altura) / 2

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

area = calcular_area_triangulo(base, altura)
print(f"La base del triangulo es de {base} y la altura {altura} entonces el area es: {area}" )