import math

def log(a, b):

    if b < 0: raise ValueError(f'Math domain error: argument must be greater than zero')

    if a == 1 or a < 0: raise ValueError('Math domain error: base must be greater than zero and base != 1')

    return math.log(b, a)

def ln(b):

    return log(math.e, b)

def lg(b):

    return log(10, b)