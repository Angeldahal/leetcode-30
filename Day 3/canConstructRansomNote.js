// Problem Description:
// Given an arbitrary ransom note string and another string containing letters from all the magazines,
// write a function that will return true if the ransom note can be constructed from the magazines;
// otherwise, it will return false.
// Each letter in the magazine string can only be used once in your ransom note.
// Note:
// You may assume that both strings contain only lowercase letters.
// Examples:
// canConstruct("a", "b") -> false
// canConstruct("aa", "ab") -> false
// canConstruct("aa", "aab") -> true

/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
const canConstruct = function(ransomNote, magazine) {
    let canConstruct = true;
    for (const element of ransomNote){

        if (!(magazine.includes(element))){
            canConstruct = false;
            return canConstruct;
        }
        else {
            magazine = magazine.replace(element, "");
        }
    }
    return canConstruct;
};

// Using the Solution

console.log(canConstruct("a", "b")); // false
console.log(canConstruct("ab", "aab")); // true