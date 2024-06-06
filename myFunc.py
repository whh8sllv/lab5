def isPrime(n):
    if n == 1:
        return '1 is not a prime or composite number'
    elif n < 1:
        return 'only a natural number can be prime'
    else:
        for i in range(2, n):
            if n % i == 0:
                return f'composite'
    return f'prime'

def factorial(n):
    if not type(n) is int:
        return 'Type Error'
    elif n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)