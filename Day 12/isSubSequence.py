"""
Problem Statement: Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a
subsequence of "abcde" while "aec" is not).
Example 1:
    Input: s = "abc", t = "ahbgdc"
    Output: true
Example 2:
    Input: s = "axc", t = "ahbgdc"
    Output: false

"""


# Solution:
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:

            if i in t:
                s = s.replace(i, "", 1)
                index = t.find(i)
                t = t.replace(t[0: index + 1], "", 1)

        if s == "":
            return True
        return False


# Main:
if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    result = Solution()
    print(result.isSubsequence(s, t))
