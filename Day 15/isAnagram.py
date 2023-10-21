"""
Problem Description:
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    Example 1:
        Input: s = "anagram", t = "nagaram"
        Output: true
    Example 2:
        Input: s = "rat", t = "car"
        Output: false
"""
# Solution:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in t:
                return False
            else:
                t = t.replace(s[i], "", 1)

        return True


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram"))
    print(solution.isAnagram("rat", "car"))
    print(solution.isAnagram("a", "ab"))
    print(solution.isAnagram("ab", "a"))