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
#include<iostream>
#include<unordered_map>
#include<unordered_set>
#include<cassert>
#include<string>
using namespace std;
class Solution {
public:
    bool isIsomorphic(std::string s, std::string t) {
        if (s.length() != t.length()) {
            return false;
        }

        std::unordered_map<char, char> dictionary;
        std::unordered_set<char> values_set;

        for (int i = 0; i < s.length(); i++) {
            if (dictionary.find(s[i]) == dictionary.end()) {
                dictionary[s[i]] = t[i];
            } else {
                if (dictionary[s[i]] != t[i]) {
                    return false;
                }
            }
        }

        for (const auto& entry : dictionary) {
            char value = entry.second;
            if (values_set.find(value) != values_set.end()) {
                return false;
            } else {
                values_set.insert(value);
            }
        }

        return true;
    }
};

// Test cases:
int main(){
    Solution solution;
    assert(solution.isIsomorphic("egg", "add") == true);
    assert(solution.isIsomorphic("foo", "bar") == false);
    assert(solution.isIsomorphic("paper", "title") == true);
    assert(solution.isIsomorphic("ab", "aa") == false);
    assert(solution.isIsomorphic("ab", "ca") == true);
    return 0;
}