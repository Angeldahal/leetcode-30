// Problem Description:
// Given a string s, find the length of the last word.
// A word is a maximal substring consisting of non-space characters only.
// Example 1:
//   Input: s = "Hello World"
//   Output: 5
// Example 2:
//   Input: s = " "
//   Output: 0

//Solution:
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {

    s = s.replace(/\s+/g, ' ').trim().split(' ')
    lastWord = s[s.length - 1]
    return lastWord.length

};

// Test Cases
console.log(lengthOfLastWord("Hello World")); // 5
console.log(lengthOfLastWord(" ")); // 0
console.log(lengthOfLastWord("a ")); // 1
