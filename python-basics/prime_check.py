"""Check whether a number is prime.

Optimisation levels (from Day 01 notes):
  L-I   : range(1, n+1)       -> count all divisors
  L-II  : range(2, n)
  L-III : range(2, n//2 + 1)
  L-IV  : range(2, sqrt(n)+1) -> O(sqrt n)
"""

# Level I: count divisors, prime if exactly 2
n = int(input())
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("prime")
else:
    print("not a prime")


# Level IV: only check up to sqrt(n)
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
