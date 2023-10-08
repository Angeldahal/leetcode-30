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
#include<iostream>
#include<unordered_map>
#include<string>
using namespace std;

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map <char, int> dictionary;

        for (char c: magazine){
            if (dictionary.find(c) == dictionary.end()){
                dictionary[c] = 1;
            }
            else {
                dictionary[c]++;
            }
        }

        for (char c: ransomNote){
            if (dictionary.find(c) != dictionary.end() && dictionary[c] > 0){
                dictionary[c]--;
            }
            else {
                return false;
            }
        }
        return true;
    }
};

// Using the Solution
int main(){
    Solution s;
    cout << s.canConstruct("a", "b") << endl; // false
    cout << s.canConstruct("aa", "ab") << endl; // false
    cout << s.canConstruct("aa", "aab") << endl; // true
    return 0;
}



