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
    if len(primesList) < 2:
        return 0, {}, 0  # No hay gaps si hay menos de 2 primos

    local_twin_primes_num = 0
    max_diff = 0
    max_local_gaps = {}  # Inicializamos el diccionario para los gaps locales

    for i in range(1, len(primesList)):
        diff = primesList[i] - primesList[i - 1]
        if diff > max_diff:
            max_diff = diff  # Actualizamos el máximo gap
            max_local_gaps = {diff: (primesList[i - 1], primesList[i])}  # Guardamos los números relacionados con el gap máximo
        if diff == 2:
            local_twin_primes_num += 1

    return local_twin_primes_num, max_local_gaps, max_diff  # Devolvemos el máximo gap correctamente
