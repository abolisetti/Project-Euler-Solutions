def sumPrimes(n):
    ans, sieve = 0, [True] * n
    for p in range(2, n):
        if sieve[p]:
            ans += p
            for i in range(p*p, n, p):
                sieve[i] = False
    return ans

print(sumPrimes(2000000))
