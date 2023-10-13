# Problem Description:
# Given a string s, find the length of the last word.
# A word is a maximal substring consisting of non-space characters only.
# Example 1:
#   Input: s = "Hello World"
#   Output: 5
# Example 2:
#   Input: s = " "
#   Output: 0

# Solution:

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for char in s[::-1]:
            if char == " ":
                if length != 0:
                    return length
            else:
                length += 1
        return length

    def lengthOfLastWord2(self, s: str) -> int:
        return len(s.rstrip().split(" ")[-1])


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLastWord("Hello World"))
    print(solution.lengthOfLastWord(" "))
    print(solution.lengthOfLastWord2("Hello World"))
    print(solution.lengthOfLastWord2(" "))