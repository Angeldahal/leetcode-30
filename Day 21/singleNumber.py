"""
Problem Description:
    Given a non-empty array of integers, every element appears twice except for one. Find that single one.

    Example:
        Input: [2,2,1]
        Output: 1

        Input: [4,1,2,1,2]
        Output: 4

        Input: [1,1,2,2,3,3,4,5,5,6,6]
        Output: 4
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        if len(nums) == 1:
            return nums[0]

        for i in range(0, len(nums) - 2, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]

        return nums[-1]


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNumber([2, 2, 1]))
    print(solution.singleNumber([4, 1, 2, 1, 2]))
    print(solution.singleNumber([1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]))
    print(solution.singleNumber([1]))