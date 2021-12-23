
def factorial(n):
    
    if not isinstance(n, int):
        raise ValueError('Argument exception: must be int')

    if n < 0:
        raise ValueError('Math domain error')

    if n == 1 or n == 0: return 1

    else: return n * factorial(n-1)
