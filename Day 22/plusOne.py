"""
Problem Description:
    Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
    The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
    You may assume the integer does not contain any leading zero, except the number 0 itself.

Example:
    Input: [1,2,3]
    Output: [1,2,4]

    Input: [4,3,2,1]
    Output: [4,3,2,2]

    Input: [9]
    Output: [1,0]
"""
from typing import List


# Solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        num = str(num + 1)
        nums = []
        for i in num:
            nums.append(int(i))
        return nums


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([1, 2, 3]))
    print(solution.plusOne([4, 3, 2, 1]))
    print(solution.plusOne([9]))
    print(solution.plusOne([0]))
    print(solution.plusOne([9, 9]))