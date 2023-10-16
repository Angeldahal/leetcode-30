// Problem Description:
// Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
// Note: For the purpose of this problem, we define empty string as valid palindrome.
// Example 1:
// Input: s = "A man, a plan, a canal: Panama"
// Output: true
// Explanation: "amanaplanacanalpanama" is a palindrome.
//
// Solution:
/**
 * @param {string} s
 * @return {boolean}
 */
const isPalindrome = function(s) {
    s = s.toLowerCase();
    s = s.replace(/[^a-zA-Z0-9]/g, '');

    const str_length = s.length
    const loop_range = str_length % 2 === 0 ? str_length / 2: (str_length - 1) / 2;

    for (let i = 0; i <= loop_range; i++){
        if (s[i] !== s[str_length - i - 1]){
            return false;
        }
    }
    return true;
};

// Testcase:
const test_string = "A man, a plan, a canal: Panama";
console.log(isPalindrome(test_string));