def is_prime(n):
    """Returns True if n is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def primepartition(m):
    """Returns True if m can be partitioned as primes, False otherwise."""
    if m <= 0:
        return False
    for i in range(2, m):
        if is_prime(i) and is_prime(m-i):
            return True
    return False
print(primepartition(7))
print(primepartition(185))
print(primepartition(3432))