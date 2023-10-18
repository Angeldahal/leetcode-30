// Problem Description:
// Given two strings s and t, determine if they are isomorphic.
//
// Two strings are isomorphic if the characters in s can be replaced to get t.
//
// All occurrences of a character must be replaced with another character
// while preserving the order of characters. No two characters may map to
// the same character but a character may map to itself.
//
// Example 1:
// Input: s = "egg", t = "add"
// Output: true
//
// Example 2:
// Input: s = "foo", t = "bar"
// Output: false
//
// Example 3:
// Input: s = "paper", t = "title"
// Output: true
//
// Solution:
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
const isIsomorphic = function (s, t) {
    if (s.length !== t.length) {
        return false;
    }

    let dictionary = {};

    for (let i = 0; i < s.length; i++) {
        if (s[i] in dictionary) {
            if (dictionary[s[i]] !== t[i]) {
                return false;
            }
        } else {
            dictionary[s[i]] = t[i];
        }
    }
    console.log(dictionary);

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


// Test Cases:
console.log(isIsomorphic("egg", "add")); // true
console.log(isIsomorphic("foo", "bar")); // false
console.log(isIsomorphic("paper", "title")); // true
console.log(isIsomorphic("ab", "aa")); // false
