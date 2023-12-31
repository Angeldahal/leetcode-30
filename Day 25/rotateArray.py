"""
Problem Description:
    Given an array, rotate the array to the right by k steps, where k is
    non-negative.

    Example 1:
        Input: [1,2,3,4,5,6,7] and k = 3
        Output: [5,6,7,1,2,3,4]
        Explanation:
            rotate 1 steps to the right: [7,1,2,3,4,5,6]
            rotate 2 steps to the right: [6,7,1,2,3,4,5]
            rotate 3 steps to the right: [5,6,7,1,2,3,4]

    Example 2:
        Input: [-1,-100,3,99] and k = 2
        Output: [3,99,-1,-100]
        Explanation:
            rotate 1 steps to the right: [99,-1,-100,3]
            rotate 2 steps to the right: [3,99,-1,-100]

"""
# Solution:
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k >= len(nums):
            k = k % len(nums)
        if len(nums) == 1 or k == 0:
            return

        nums[:k], nums[k:] = nums[-k:], nums[:-k]


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    solution.rotate(nums, 3)
    print(nums)
    nums = [-1, -100, 3, 99]
    solution.rotate(nums, 2)
    print(nums)