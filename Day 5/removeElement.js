// Problem Description:
// Given an array nums and a value val, remove all instances of that value in-place and return the new length.
// Example:
// Input: nums = [3,2,2,3], val = 3
// Output: 2, nums = [2,2]
// Note:
// Do not allocate extra space for another array, you must do this by modifying the input array in-place
// with O(1) extra memory.
// The order of elements can be changed. It doesn't matter what you leave beyond the new length.
//
// Solution:
/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let idx = 0;
    for (let i = 0; i < nums.length; i++){
        if (nums[i] !== val){
            nums[idx] = nums[i];
            idx++;
        }
    }
    return idx;
};

// Testcase:
console.log(removeElement([3,2,2,3], 3));
console.log(removeElement([0,1,2,2,3,0,4,2], 2));