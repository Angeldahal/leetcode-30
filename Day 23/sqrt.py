"""
Problem Description:
    Given a non-negative integer x, compute and return the square root of x.
    Since the return type is an integer, the decimal digits are truncated, and
    only the integer part of the result is returned.

Notes:
    - You may not use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Constraints:
    - 0 <= x <= 2^31 - 1

Examples:
    - Example 1:
        Input: x = 4
        Output: 2
    - Example 2:
        Input: x = 8
        Output: 2
        Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
"""
import math


# Solution:
class Solution:
    def mySqrt(self, x: int) -> int:
        number = x / 2
        temp = 0

        if x == 1:
            return 1

        while math.floor(temp) != math.floor(number):
            temp = number
            number = (x/temp + temp) / 2

        return math.floor(number)

    def mySqrt2(self, x: int) -> int:
        n = 1
        while n * n <= x:
            n += 1
        return n - 1


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.mySqrt(4))
    print(solution.mySqrt(8))
    print(solution.mySqrt(1))
    print(solution.mySqrt(0))
    print(solution.mySqrt(2))
    print(solution.mySqrt(3))
    print(solution.mySqrt(5))
    print(solution.mySqrt(6))
