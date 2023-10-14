// Problem Description:
// Write a function to find the longest common prefix string amongst an array of strings.
// If there is no common prefix, return an empty string "".
//
// Example 1:
// Input: strs = ["flower","flow","flight"]
// Output: "fl"
//
// Example 2:
// Input: strs = ["dog","racecar","car"]
// Output: ""

// Solution : Sort the array of strings and compare the first and last string.

#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string longestPrefix = "";

        sort(strs.begin(), strs.end());
        int n = strs.size();

        string first = strs[0], last = strs[n - 1];

        for (int i = 0; i < min(first.size(), last.size()); i++){
            if (first[i] != last[i]){
                return longestPrefix;
            }
            longestPrefix += first[i];
        }
        return longestPrefix;
    }
};

int main(){
    vector<string> strs = {"flower", "flow", "flight"};
    Solution s;
    cout << s.longestCommonPrefix(strs) << endl;
    return 0;
}