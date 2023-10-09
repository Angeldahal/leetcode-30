// Problem Description:
// Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
// Example:
// Input: nums1 = [1,2,3,0,0,0], m = 3
//        nums2 = [2,5,6],       n = 3
// Output: [1,2,2,3,5,6]
// Note:
// The number of elements initialized in nums1 and nums2 are m and n respectively.
// You may assume that nums1 has enough space (size that is greater or equal to m + n)
// to hold additional elements from nums2.
//
// Solution:
// Time Complexity: O(n)
// Space Complexity: O(1)

/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
const merge = function(nums1, m, nums2, n) {
    let i = m - 1;
    let j = n - 1;
    let k = m + n - 1;

    while (j >= 0){
        if (i >= 0 && nums1[i] >= nums2[j]){
            nums1[k] = nums1[i];
            i -= 1;
        }
        else {
            nums1[k] = nums2[j];
            j -= 1;
        }
        k -= 1;
    }
};

// Test Cases
const test1 = [1,2,3,0,0,0];
const test2 = [2,5,6];
merge(test1, 3, test2, 3);
console.log(test1); // [1,2,2,3,5,6]