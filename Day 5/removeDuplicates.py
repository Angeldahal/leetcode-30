# Problem Description:
# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array,
# you must do this by modifying the input array in-place with O(1) extra memory.
#
# Example 1:
#   Given nums = [1,1,2],
#   Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
#   It doesn't matter what you leave beyond the returned length.
#
# Solution:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[idx] = nums[i]
                idx += 1
        return idx


# TestCases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates([1, 1, 2]))
    print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(solution.removeDuplicates([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    print(solution.removeDuplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
