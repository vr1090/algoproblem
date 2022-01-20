class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n < 2:
            return 0
        
        primes = [True] * n
        primes[0] = False
        primes[1] = False
        
        for check in range(2, ceil(sqrt(n))):
            if(primes[check]):
                for k in range(check*check, n, check):
                    primes[k]= False
        
        return sum(primes)
        