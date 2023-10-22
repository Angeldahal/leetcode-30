"""
Problem Description:
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges,
and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:
    "a->b" if a != b
    "a" if a == b

Example 1:
    Input: nums = [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]
    Explanation: The ranges are:
        [0,2] --> "0->2"
        [4,5] --> "4->5"
        [7,7] --> "7"

Example 2:
    Input: nums = [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]
    Explanation: The ranges are:
        [0,0] --> "0"
        [2,4] --> "2->4"
        [6,6] --> "6"
        [8,9] --> "8->9"

"""
from typing import List


# Solution:
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        ans = []
        temp = ""
        i = 0

        while True:
            j = i
            while j + 1 < n and nums[j + 1] == nums[j] + 1:
                j += 1

            if j > i:
                temp = f"{nums[i]}->{nums[j]}"
            else:
                temp = str(nums[i])

            ans.append(temp)
            temp = ""
            i = j + 1
            if i >= n:
                break

        return ans


# TestCases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.summaryRanges([0, 1, 2, 4, 5, 7]))
    print(solution.summaryRanges([0, 2, 3, 4, 6, 8, 9]))
    print(solution.summaryRanges([]))
    print(solution.summaryRanges([-1]))
    print(solution.summaryRanges([0]))
    print(solution.summaryRanges([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(solution.summaryRanges([0, 1, 2, 3, 4, 5, 6, 7, 8, 10]))
    print(solution.summaryRanges([0, 1, 2, 3, 4, 5, 6, 7, 9, 10]))
    print(solution.summaryRanges([0, 1, 2, 3, 4, 5, 6, 8, 9, 10]))
    print(solution.summaryRanges([0, 1, 2, 3, 4, 5, 7, 8, 9, 10]))
    print(solution.summaryRanges([0, 1, 2, 3, 4, 6, 7, 8, 9, 10]))
    print(solution.summaryRanges([0, 1, 2, 3, 5, 6, 7, 8, 9, 10]))
    print(solution.summaryRanges([0, 1, 2, 4, 5, 6, 7, 8, 9, 10]))
    print(solution.summaryRanges([0, 1, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(solution.summaryRanges([0, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(solution.summaryRanges([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(solution.summaryRanges([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]))
