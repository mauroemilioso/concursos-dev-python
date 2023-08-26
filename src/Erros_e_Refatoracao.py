
# Probleminhas gerados pelo ChatGPT: https://chat.openai.com/share/45c8995c-b5e4-4560-ab5a-b198c7b9bbe4

#falhas na identação 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
result = factorial(5)
print("Factorial of 5:", result) 


# identação do último print incorrta
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i])
    print("Next number")

#Mesmo problema de falta do :
x = 5
if x > 2:
    print("x is greater than 2")
else:
    print("x is not greater than 2")

# estava faltando o : no fim do DEF
def calculate_average(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return avg

numbers = [10, 15, 20, 25]
result = calculate_average(numbers)
print("The average is:", result)