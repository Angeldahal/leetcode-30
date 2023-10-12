# Problem Description:
# Given a string s of roman numerals, convert it to an integer.
# Example 1:
#   Input: s = "III"
#   Output: 3
# Example 2:
#   Input: s = "IV"
#   Output: 4
# Example 3:
#   Input: s = "IX"
#   Output: 9

# Solution:
class Solution:
    def romanToInt(self, s: str) -> int:
        n = 0
        dictionary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for idx, char in enumerate(s):
            if idx == len(s) - 1:
                n = n + dictionary[char]
                continue
            if dictionary[char] < dictionary[s[idx + 1]]:
                n = n - dictionary[char]
            else:
                n = n + dictionary[char]

        return n


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("III"))
    print(solution.romanToInt("IV"))
    print(solution.romanToInt("IX"))