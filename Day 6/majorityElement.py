# Problem Description:
# Given a non-empty array of integers, return the majority element.
# The majority element is the element that appears more than ⌊n/2⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.
# Example:
# Input: [3,2,3]
# Output: 3
# Input: [2,2,1,1,1,2,2]
# Output: 2

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary = {}

        for i in nums:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1

        return max(dictionary, key=dictionary.get)

    def majorityElement2(self, nums: List[int]) -> int:
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


# Test Cases
if __name__ == "__main__":
    Solution = Solution()
    print(Solution.majorityElement([3, 2, 3]))
    print(Solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))
    print(Solution.majorityElement2([3, 2, 3]))
    print(Solution.majorityElement2([2, 2, 1, 1, 1, 2, 2]))