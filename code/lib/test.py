from num_theory import decomposePositiveInt, isPrime
from num_theory import primesLessThanN


primes = primesLessThanN(100)
for p in primes:
    print("{} ~ {} is prime: {}".format(p, 2**p - 1, isPrime(2**p-1)))

print(ord('龙'))
print(ord(chr(0x9F99)))

for i in range(1, 8):
    x = 2**(2**i) -1
    print(x)