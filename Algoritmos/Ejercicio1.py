def fibonacci_recursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def fibonacci_iterativo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b

numero = 10
valor_fibonacci_recursivo = fibonacci_recursivo(numero)
print(f"El valor de Fibonacci para {numero} (recursivo) es: {valor_fibonacci_recursivo}")

valor_fibonacci_iterativo = fibonacci_iterativo(numero)
print(f"El valor de Fibonacci para {numero} (iterativo) es: {valor_fibonacci_iterativo}")
