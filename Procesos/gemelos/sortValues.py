def BLOCK_LOW(id, p, n):
    return id * n // p

def BLOCK_HIGH(id, p, n):
    return (id + 1) * n // p - 1

def BLOCK_SIZE(id, p, n):
    return BLOCK_HIGH(id, p, n) - BLOCK_LOW(id, p, n) + 1

def get_primes(primesList):
    local_primes = []
    for number in primesList:
        if es_primo(number):
            local_primes.append(number)
    return local_primes
