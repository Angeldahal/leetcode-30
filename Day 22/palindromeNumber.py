"""
Problem Description:
    Given a integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

Example:
    Input: 121
    Output: true

    Input: -121
    Output: false

    Input: 10
    Output: false
"""

# Solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        loop_range = int(len(x) / 2)

        for i in range(loop_range):
            if x[i] != x[-i - 1]:
                return False

        return True


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(121))
    print(solution.isPalindrome(-121))
    print(solution.isPalindrome(10))
    print(solution.isPalindrome(0))
    print(solution.isPalindrome(1))
    print(solution.isPalindrome(11))
    print(solution.isPalindrome(111))
    print(solution.isPalindrome(1111))