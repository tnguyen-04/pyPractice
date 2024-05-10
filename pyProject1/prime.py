
def prime_checker(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    i = 3
    sqrt_n = int(number ** 0.5)
    while i <= sqrt_n:
        if number % i == 0:
            return False
        i += 2
    return True
inputt = int(input('nhap'))
print(prime_checker(inputt))

       