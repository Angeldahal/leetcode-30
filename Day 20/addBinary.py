"""
Problem Description:
    Given two binary strings a and b, return their sum as a binary string.
Example:
    Input: a = "11", b = "1"
    Output: "100"
    Input: a = "1010", b = "1011"
    Output: "10101"
"""


# Solution:
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        result = ""
        carry = 0

        for i in range(max_len - 1, -1, -1):
            r = carry
            r += 1 if a[i] == "1" else 0
            r += 1 if b[i] == "1" else 0
            result = ("1" if r % 2 == 1 else "0") + result

            carry = 0 if r < 2 else 1

        if carry != 0:
            result = "1" + result

        return result


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.addBinary("11", "1"))
    print(solution.addBinary("1010", "1011"))
    print(solution.addBinary("0", "0"))
    print(solution.addBinary("1111", "1111"))
    print(solution.addBinary("1111", "1110"))
    print(solution.addBinary("1110", "1111"))
    print(solution.addBinary("1110", "1110"))
    print(solution.addBinary("1111", "1110"))
    print(solution.addBinary("1110", "1111"))
    print(solution.addBinary("1110", "1110"))
