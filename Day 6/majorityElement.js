// Problem Description:
// Given a non-empty array of integers, return the majority element.
// The majority element is the element that appears more than ⌊n/2⌋ times.
// You may assume that the array is non-empty and the majority element always exist in the array.
// Example:
// Input: [3,2,3]
// Output: 3
// Input: [2,2,1,1,1,2,2]
// Output: 2

// Solution:
/**
 * @param {number[]} nums
 * @return {number}
 */
// Using the Boyer-Moore Voting Algorithm
const majorityElement = function (nums) {
    let count = 0;
    let candidate = 0;

    nums.forEach(function (num) {
        if (count === 0) {
            candidate = num;
        }

        if (num === candidate) {
            count += 1;
        } else {
            count -= 1;
        }
    });

    return candidate;
};

// Using the object data structure
const majorityElement2 = function (nums) {
    let obj = {};
    let max = 0;
    let maxNum = nums[0];

    for (let i = 0; i < nums.length; i++) {
        let num = nums[i];
        obj[num] = obj[num] + 1 || 1;
        if (obj[num] > max) {
            max = obj[num];
            maxNum = num;
        }
    }

    return maxNum;
}

// Test Cases
console.log(majorityElement([3, 2, 3])); // 3
console.log(majorityElement([2, 2, 1, 1, 1, 2, 2])); // 2
console.log(majorityElement([1])); // 1
console.log(majorityElement2([1, 2, 3, 4, 5, 6, 7, 8, 9, 1])); // 1
console.log(majorityElement2([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1])); // 1