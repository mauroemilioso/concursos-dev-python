from Erros_e_Refatoracao import factorial

class Fatorial:

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    
    if __name__ == '__main__':
        result = factorial(5)
        print("Factorial of 5:", result)
        result = factorial(50)
        print("Factorial of 50:", result)
        result = factorial(250)
        print("Factorial of 250:", result)
        result = factorial(2380)
        print("Factorial of 2380:", result)