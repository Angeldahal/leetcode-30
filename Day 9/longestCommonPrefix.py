# Problem Description:
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
from typing import List


# Solution:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestPrefix = ""

        strs = sorted(strs)

        first = strs[0]
        last = strs[-1]

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return longestPrefix

            longestPrefix += first[i]

        return longestPrefix


# Test Cases:

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
    print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
