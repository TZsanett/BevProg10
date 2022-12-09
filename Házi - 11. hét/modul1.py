def is_prime(n): # """ Decide whether a number is prime or not. """

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False