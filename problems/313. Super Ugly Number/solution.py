"""
https://leetcode.com/problems/super-ugly-number/description/

A super ugly number is a positive integer whose prime factors are in the array primes.

Given an integer n and an array of integers primes, return the nth super ugly number.

The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

Example 1:
Input: n = 12, primes = [2,7,13,19]
Output: 32
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 super ugly numbers given primes = [2,7,13,19].

Example 2:
Input: n = 1, primes = [2,3,5]
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are in the array primes = [2,3,5].
 

Constraints:

* 1 <= n <= 105
* 1 <= primes.length <= 100
* 2 <= primes[i] <= 1000
* primes[i] is guaranteed to be a prime number.
* All the values of primes are unique and sorted in ascending order.
"""

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # Keep an array of indexes of the last number the ith
        # prime was used to multiply with
        k = len(primes)
        generated = [0] * n
        memo = [0] * k

        # Last number that we appended
        last = 1

        # Memo of primes "used" to generate the next number. The
        # key will be the index of the number generated, and the
        # value will be an array of indexes of all the numbers
        # "used" to generate that number
        used = {0: set()}

        generated[0] = 1
        for i in range(1, n):
            # Find the lowest multiple of available primes and
            # numbers generated thus far
            m = float("inf")
            used_t = set()
            for j in range(0, k):
                t = primes[j] * generated[memo[j]]
                if t < m:
                    m = t
                    used_t = used[memo[j]].copy()
                    used_t.add(j)
            used[i] = used_t
            for p in used_t:
                memo[p] += 1
            generated[i] = last = m
        
        return last
