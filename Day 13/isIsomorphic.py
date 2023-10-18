# Problem Description:
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character
# while preserving the order of characters. No two characters may map to
# the same character but a character may map to itself.
#
# Example 1:
# Input: s = "egg", t = "add"
# Output: true
#
# Example 2:
# Input: s = "foo", t = "bar"
# Output: false
#
# Example 3:
# Input: s = "paper", t = "title"
# Output: true
#
# Solution:
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dictionary = {}

        for i in range(len(s)):
            if s[i] not in dictionary:
                dictionary[s[i]] = t[i]
            else:
                if dictionary[s[i]] != t[i]:
                    return False

        values_set = set()

        for key, value in dictionary.items():
            if value in values_set:
                return False
            else:
                values_set.add(value)

        return True


# TestCases:
if __name__ == "__main__":
    test_cases = [
        ("egg", "add"),
        ("foo", "bar"),
        ("paper", "title")
    ]
    solution = Solution()
    for s, t in test_cases:
        print(solution.isIsomorphic(s, t))
