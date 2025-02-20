
print("Bienvenidos dinos los precio, gannacia y impuesto")
#escribir leer
precio = input("engrese el precio: ")
precio = float(precio)

ganancia = input("engrese ganancia: ")
precio = float(ganancia)

impuesto = input("engrese impuesto: ")
precio = float(impuesto)


#funcion nombre de l avariable()
def calcularImpuesto(impuesto, precio):
    return impuesto * precio

def calcularGanancia(ganancia, precio):
    return ganancia * precio

def calcularPreciofinal(precio, impueso, ganancia):
    precio1 = calcularGanancia(ganancia, precio) + precio
    impuestVenta = calcularImpuesto(impueso, precio1)
    return precio1 + impuestVenta

print(calcuarPrecioFinal(precio, impuesto, ganancia))




