def celsius_to_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

# Solicitar al usuario un valor en Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius}°C es igual a {fahrenheit:.2f}°F")