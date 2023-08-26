"""
Python
"""
from ast import List
def retornaArrayFibonacci(n):
    fibo = []
    for i in range(0, n+1):
        if i == 0:
            fibo.append(i)
            continue
        if i == 1:
            fibo.append(i)
            continue
        fibo.append(fibo[i-1]+fibo[i-2])
    return fibo

# Fibonacci usando recursão
def fibonacci_recursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Fibonacci usando programação dinâmica (memorização)
def fibonacci_dinamico(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        memo[n] = result
        return result

# Testando os métodos
if __name__ == "__main__":
    n = 10
    print(f"Fibonacci de {n} (recursivo): {fibonacci_recursivo(n)}")
    print(f"Fibonacci de {n} (dinâmico): {fibonacci_dinamico(n)}")
    print(f"Fibonacci de {n} (Mauro): {retornaArrayFibonacci(10)}")
    