#!/usr/bin/env python3

# Tribute to HSCTF 2014's 20XX

import random, sys

# Adapted from Wikibooks, because I'm lazy :P
def is_probable_prime(n, k = 100):
    """use Rabin-Miller algorithm to return True (n is probably prime)
       or False (n is definitely composite)"""
    if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
        return [False, False, True, True, False, True][n]
    elif n & 1 == 0:  # should be faster than n % 2
        return False
    else:
        s, d = 0, n - 1
        while d & 1 == 0:
            s, d = s + 1, d >> 1
        for i in range(k):
            a = random.randint(2,n-2)
            x = pow(a, d, n)
            if x != 1 and x + 1 != n:
                for r in range(1, s):
                    x = pow(x, 2, n)
                    if x == 1:
                        return False  # composite for sure
                    elif x == n - 1:
                        a = 0  # so we know loop didn't continue to end
                        break  # could be strong liar, try another a
                if a:
                    return False  # composite if we reached end of this loop
        return True  # probably prime if reached end of outer loop

def probable_prime(size):
    while True:
        p = random.randrange(2**(size-1),2**size)
        if is_probable_prime(p):
            return p

def superincreasing_sequence(n):
    k = []
    for i in range(n):
        k.append(sum(k)+random.randrange(1,1000))
    return k

def merkle_hellman_knapsack(message):
    b = ''.join(format(ord(i),'08b') for i in message)
    ss = superincreasing_sequence(len(b))

    p = probable_prime(128)
    r = random.randrange(1,p)

    k = [(i*r)%p for i in ss]
    c = sum([k[i] for i in range(len(b)) if b[i] == '1'])

    return ((ss, r, p), k, c)

def main():
    message = input("Message: ")
    private, public, cipher = merkle_hellman_knapsack(message)
    print()
    print("Private Key:")
    print("Superincreasing Sequence:", private[0])
    print("Multiplier:", private[1])
    print("Modulus:", private[2])
    print()
    print("Public Key:", public)
    print()
    print("Ciphertext:", cipher)

if __name__ == '__main__':
    main()
