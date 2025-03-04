def BLOCK_LOW(id, p, n):
    return id * n // p

def BLOCK_HIGH(id, p, n):
    return (id + 1) * n // p - 1

def BLOCK_SIZE(id, p, n):
    return BLOCK_HIGH(id, p, n) - BLOCK_LOW(id, p, n) + 1
