def factorial(n):
    if n == 1:
        return n

    return n * factorial(n-1)

n = int(input("enter number: "))

print(factorial(n))