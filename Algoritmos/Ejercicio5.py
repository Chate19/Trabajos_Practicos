def romano_a_decimal(romano):
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    valor_anterior = 0

    for letra in reversed(romano):
        valor_actual = valores[letra]
        if valor_actual < valor_anterior:
            total -= valor_actual
        else:
            total += valor_actual
        valor_anterior = valor_actual

    return total

numero_romano_ingresado = input("Ingrese un número romano: ")

resultado = romano_a_decimal(numero_romano_ingresado)

print("El número romano {numero_romano_ingresado} en decimal es: {resultado}")