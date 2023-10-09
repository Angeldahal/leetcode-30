# Problem Description:
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# Example:
# Input: nums1 = [1,2,3,0,0,0], m = 3
#        nums2 = [2,5,6],       n = 3
# Output: [1,2,2,3,5,6]
# Note:
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n)
# to hold additional elements from nums2.
#
# Solution:
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:

    # Solution 1: Merge and Sort
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for j in range(n):
            nums1[m + j] = nums2[j]
        nums1.sort()

    # Solution 2: Two Pointers / Start from the end
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    solution.merge(nums1, 3, [2, 5, 6], 3)
    print(nums1)
    nums1 = [1, 2, 3, 0, 0, 0]
    solution.merge2(nums1, 3, [2, 5, 6], 3)
    print(nums1)
