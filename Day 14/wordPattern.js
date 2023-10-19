// Problem Description:
// Given a pattern and a string str, find if str follows the same pattern.
//
// Here follow means a full match, such that there is a bijection
// between a letter in pattern and a non-empty word in str.
//
// Examples:
//
//     pattern = "abba", str = "dog cat cat dog" should return true.
//     pattern = "abba", str = "dog cat cat fish" should return false.
//     pattern = "aaaa", str = "dog cat cat dog" should return false.
//     pattern = "abba", str = "dog dog dog dog" should return false.
//
// Solution:
/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
const wordPattern = function (pattern, s) {

    s = s.split(" ");

    if (s.length !== pattern.length) {
        return false;
    }

    let dictionary = {};

    for (let i = 0; i < s.length; i++) {
        if (pattern[i] in dictionary) {
            if (dictionary[pattern[i]] !== s[i]) {
                return false;
            }
        } else {
            dictionary[pattern[i]] = s[i];
        }
    }

    let values_arr = [];

    for (const key in dictionary) {
        if (values_arr.includes(dictionary[key])) {
            return false;
        } else {
            values_arr.push(dictionary[key]);
        }
    }

    return true;
};