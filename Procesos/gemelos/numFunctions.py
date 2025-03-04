def es_primo(n):
    if n == 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_primes(primesList):
    local_primes = []
    for number in primesList:
        if es_primo(number):
            local_primes.append(number)
    return local_primes

def get_gaps(primesList):
    if len(primesList) == 0:
        return 0

    twinPrimesCount = 0

    for i in range(len(primesList)):
        diff = primesList[i] - primesList[i - 1]
        if diff == 2:
            twinPrimesCount += 1
    return twinPrimesCount
