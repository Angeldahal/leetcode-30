// Problem Description:
// Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
//
// Do not allocate extra space for another array,
// you must do this by modifying the input array in-place with O(1) extra memory.
//
// Example 1:
//   Given nums = [1,1,2],
//   Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
//   It doesn't matter what you leave beyond the returned length.
//
// Solution:

/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let idx = 1;
    for (let i = 1; i < nums.length; i++){
        if (nums[i] !== nums[i-1]){
            nums[idx] = nums[i];
            idx++;
        }
    }
    return idx;
};

// Test Cases
console.log(removeDuplicates([1,1,2])); // 2
console.log(removeDuplicates([0,0,1,1,1,2,2,3,3,4])); // 5
console.log(removeDuplicates([1,1,1,1,1,1,1,1,1,1])); // 1