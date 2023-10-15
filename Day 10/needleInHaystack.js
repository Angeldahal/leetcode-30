// Problem Description:
// Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
//
// Example 1:
// Input: haystack = "hello", needle = "ll"
// Output: 2
//
// Example 2:
// Input: haystack = "aaaaa", needle = "bba"
// Output: -1
//
// Solution:

/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
const strStr = function(haystack, needle) {
    if (haystack.includes(needle)){
        return haystack.indexOf(needle);
    }
    else {
        return -1;
    }
};

// TestCases:
console.log(strStr("hello", "ll")); // 2
console.log(strStr("aaaaa", "bba")); // -1
console.log(strStr("aaaaa", "a")); // 0