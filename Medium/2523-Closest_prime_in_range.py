# DQ 6 Mar 2025
# Use Sieve of Eratosthenes

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [True] * (right+1)
        sieve[0] = sieve[1] = False

        for (i, isprime) in enumerate(sieve):
            if isprime:
                for n in range(i*i, right+1, i):
                    sieve[n] = False

        primes = [i for i in range(left, right+1) if sieve[i]]
        if len(primes) < 2:
            return [-1, -1]

        ans = float("inf")
        for i in range(len(primes)-1):
            if primes[i+1] - primes[i] <= ans:
                idx = i
                ans = primes[i+1] - primes[i]
                if ans <= 2:
                    break
        return [primes[idx], primes[idx+1]]
