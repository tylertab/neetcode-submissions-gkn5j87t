class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [False] * (n)
        print(n)

        count = 0
        for i in range(2, len(sieve)):
            if sieve[i] == False: 
                count += 1
                
                for j in range(i * i , n, i):
                    sieve[j] = True

        return count
