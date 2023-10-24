"""
Problem Description:
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    Input: nums = [3,3], target = 6
    Output: [0,1]

"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            num = target - nums[i]
            if num in nums[i + 1:]:
                result.append(i)
                result.append(nums.index(num, i + 1))
                return result


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([3, 2, 4], 6))
    print(solution.twoSum([3, 3], 6))
