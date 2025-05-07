import bisect

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, limit + 1, start):
                sieve[multiple] = False

    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return primes

def generate_400_numbers(limit):
    primes = sieve_of_eratosthenes(int(limit ** 0.5) + 1)
    numbers = set()
    
    for i in range(len(primes)):
        p1 = primes[i]
        p1_squared = p1 * p1
        num_p1 = p1_squared
        while num_p1 <= limit:
            for j in range(i + 1, len(primes)):
                p2 = primes[j]
                p2_squared = p2 * p2
                num = num_p1 * p2_squared
                if num > limit:
                    break
                while num <= limit:
                    numbers.add(num)
                    num *= p2_squared
            num_p1 *= p1_squared
    
    return sorted(numbers)

def main():
    numbers = generate_400_numbers(10**12)
    q = int(input())
    for _ in range(q):
        query = int(input())
        pos = bisect.bisect_right(numbers, query) - 1
        print(numbers[pos])

if __name__ == '__main__':
    main()