"""
Problem Description:
    Reverse bits of a given 32 bits unsigned integer.
    Example:
        Input: 00000010100101000001111010011100
        Output: 00111001011110000010100101000000
        Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596,
        so return 964176192 which its binary representation is 00111001011110000010100101000000.
"""
# Solution:
class Solution:
    def reverseBits(self, n: int) -> int:
        return self.reverse(n, 0, 0)

    def reverse(self, n, rev_n, bit):
        return rev_n << (32 - bit) if n < 1 else self.reverse(n >> 1, rev_n << 1 | (n & 1), bit + 1)


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseBits(43261596))
    print(solution.reverseBits(4294967293))
    print(solution.reverseBits(0))
    print(solution.reverseBits(1))
    print(solution.reverseBits(2147483648))
    print(solution.reverseBits(2147483649))