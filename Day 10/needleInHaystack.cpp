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
#include<iostream>
#include<string>
using namespace std;
class Solution {
public:
    int strStr(string haystack, string needle)
    {
        int index = haystack.find(needle);
        return (index != -1) ? index : -1;
    }
};

//Test cases:
int main(){
    Solution solution;
    string haystack = "hello";
    string needle = "ll";
    cout << solution.strStr(haystack, needle) << endl;
    return 0;
}