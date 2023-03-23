def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Digite um número: "))

pertence = False
i = 0
while fibonacci(i) <= num:
    if fibonacci(i) == num:
        pertence = True
        break
    i += 1

if pertence:
    print(num, "pertence à sequência de Fibonacci")
else:
    print(num, "não pertence à sequência de Fibonacci")