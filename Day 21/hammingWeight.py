"""
Problem Description:
    Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Example:
    Input: 00000000000000000000000000001011
    Output: 3
    Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        n = str(n)
        count = 0
        for i in n:
            if i == "1":
                count += 1
        return count


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.hammingWeight(11))
    print(solution.hammingWeight(128))
    print(solution.hammingWeight(4294967293))
    print(solution.hammingWeight(4294967295))
