"""
Problem Description:
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that
nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:
    Input: nums = [1,2,3,1], k = 3
    Output: true

Example 2:
    Input: nums = [1,0,1,1], k = 1
    Output: true

Example 3:
    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false
"""
from typing import List


# Solution:
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictionary = {}

        for i, n in enumerate(nums):
            if n in dictionary and abs(i - dictionary[n]) <= k:
                return True
            else:
                dictionary[n] = i

        return False


# TestCases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))
    print(solution.containsNearbyDuplicate([1, 0, 1, 1], 1))
    print(solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
