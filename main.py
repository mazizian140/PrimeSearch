
''' Given an integer n, return the number of prime numbers that are strictly less than n.
'''
def countPrimes(n):
    if n <= 2:
        return 0

    # Step 1: Create a boolean array to track prime numbers
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    # Step 2: Mark non-prime numbers using the Sieve of Eratosthenes
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            # Mark all multiples of i as False
            for multiple in range(i * i, n, i):
                is_prime[multiple] = False

    # Step 3: Count the primes
    return sum(is_prime)


def main():
    # Example input
    n = int(input("Enter the number you want to find the primes less than that: "))

    # Get the number of primes less than n
    result = countPrimes(n)

    # Output the result
    print(f"Number of primes less than {n}: {result}")


if __name__ == "__main__":
    main()

