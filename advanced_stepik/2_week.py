from itertools import takewhile
from math import factorial

def is_prime(n):
    if (factorial(n-1)+1) % n == 0:
        return True

def primes():
    x = 2
    while True:
        if is_prime(x):
            yield x
            x+=1
        else:
            x+=1

if __name__ == '__main__':
    print(list(takewhile(lambda x : x <= 31, primes())))