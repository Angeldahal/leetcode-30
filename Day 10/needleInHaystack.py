# Problem Description:
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#
# Solution:
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

    def strStr2(self, haystack: str, needle: str) -> int:
        m = len(needle)
        length = 0
        i = 1
        lps = [0] * m

        while i < m:
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length == 0:
                    lps[i] = 0
                    i += 1
                else:
                    length = lps[length - 1]

        n = len(haystack)
        j = 0
        i = 0

        while j < n:
            if haystack[j] == needle[i]:
                i += 1
                j += 1
                if i == m:
                    return j - m
            elif haystack[j] != needle[i]:
                if i == 0:
                    j += 1
                else:
                    i = lps[i - 1]

        return -1


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.strStr("hello", "ll"))
    print(solution.strStr("aaaaa", "bba"))
    print(solution.strStr2("hello", "ll"))
    print(solution.strStr2("aaaaa", "bba"))

