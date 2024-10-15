Algorithm: Sieve of Eratosthenes
Step 1: Create a boolean array is_prime of size n, initialized to True for all elements. The value is_prime[i] will be True if i is a prime number and False otherwise.

Step 2: Mark non-prime numbers. Starting from the smallest prime number 2, mark all of its multiples as non-prime (i.e., False).

For example, mark 4, 6, 8, 10, etc. (multiples of 2) as False.
Then, move to the next number that is still marked True (this will be 3) and repeat the process.
Repeat this process for numbers up to sqrt(n), because larger factors will already have been marked.
Step 3: Count primes. After marking non-prime numbers, count how many True values remain in the is_prime array for numbers less than n.
