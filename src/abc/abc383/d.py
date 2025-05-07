def sieve_of_eratosthenes(n):
    prime_flags = [True] * (n + 1)
    
    prime_flags[0] = prime_flags[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if prime_flags[i]:
            for j in range(i*i, n+1, i):
                prime_flags[j] = False
    
    primes = [i for i in range(2, n+1) if prime_flags[i]]
    
    return primes

def main():
    n = int(input())
    primes = sieve_of_eratosthenes(10**6)
    ans = 0
    for i in range(len(primes)):
        if primes[i]**8 <= n:
            ans += 1
        else:
            break
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            if primes[i]**2 * primes[j]**2 <= n:
                ans += 1
            else:
                break
    print(ans)
    
if __name__ == '__main__':
    main()