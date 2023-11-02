"""Problem Description:
You are given an array of integer array nums. ou are initially positioned at the array's
first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: The maximum jump length in nums is 2,
    jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what.
    Its maximum jump length is 0, which makes it impossible to reach the last index.

"""
from typing import List


# Solution:
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0

        for i in range(len(nums)):
            if i > reachable:
                return False

            reachable = max(reachable, i + nums[i])
        return True


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.canJump([2, 3, 1, 1, 4]))
    print(solution.canJump([3, 2, 1, 0, 4]))
    print(solution.canJump([0]))
    print(solution.canJump([1, 0, 1, 0]))
    print(solution.canJump([1, 1, 1, 0]))
