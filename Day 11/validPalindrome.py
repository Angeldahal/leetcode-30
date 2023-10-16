# Problem Description:
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
# Solution:
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        str_length = len(s)
        loop_range = str_length / 2 if str_length % 2 == 0 else (str_length - 1) / 2
        loop_range = int(loop_range)

        for i in range(loop_range):
            if s[i] != s[-i - 1]:
                return False

        return True


# TestCases:
if __name__ == "__main__":
    solution = Solution()
    test_s = "A man, a plan, a canal: Panama"
    print(solution.isPalindrome(test_s))

