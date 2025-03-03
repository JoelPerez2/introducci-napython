import random

def numero_aleatorio():
    print("Esta vez se genero el siguiente número")
    num = random.randint(1, 100)
    print(f"Número generado: {num}")

numero_aleatorio()