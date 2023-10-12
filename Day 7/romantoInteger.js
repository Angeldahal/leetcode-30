// Problem Description:
// Given a string s of roman numerals, convert it to an integer.
// Example 1:
//   Input: s = "III"
//   Output: 3
// Example 2:
//   Input: s = "IV"
//   Output: 4
// Example 3:
//   Input: s = "IX"
//   Output: 9

// Solution:

/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    let n = 0;

    const dictionary = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    for(let i = 0; i < s.length; i++){
        if (i == s.length - 1){
            n += dictionary[s[i]];
            continue;
        }
        if (dictionary[s[i]] < dictionary[s[i + 1]]){
        n -= dictionary[s[i]];
    }
        else {
            n += dictionary[s[i]];
        }
    }
    return n;
};

// Test Cases
console.log(romanToInt("III")); // 3
console.log(romanToInt("IV")); // 4
console.log(romanToInt("IX")); // 9
console.log(romanToInt("LVIII")); // 58