"""
Problem Description:
    Given an integer array nums, return an array answer such that answer[i]
    is equal to the product of all the elements of nums except nums[i].

    The algorithm should run in O(n) time and should not consist division operation.

    Example 1:
        Input: nums = [1, 2, 3, 4]
        Output: [24, 12, 8, 6]

    Example 2:
        Input: nums= [-1, 1, 0, -3, 3]
        Output: [0, 0, 9, 0, 0]
"""
# Solution:

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod = 1
        postfix_prod = 1
        result = [0] * n

        for i in range(n):
            result[i] = prefix_prod
            prefix_prod *= nums[i]

        for i in range(n-1, -1, -1):
            result[i] *= postfix_prod
            postfix_prod *= nums[i]

        return result


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1, 2, 3, 4]))
    print(solution.productExceptSelf([-1, 1, 0, -3, 3]))
    print(solution.productExceptSelf([0, 1, 3, 5, 7, 9, 10, 20]))