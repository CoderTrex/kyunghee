def factorial(number):
    if number == 0 or number == 1:
        return 1
    return int(number * factorial(number-1))
