// Problem Description:
// Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
// Note: For the purpose of this problem, we define empty string as valid palindrome.
// Example 1:
// Input: s = "A man, a plan, a canal: Panama"
// Output: true
// Explanation: "amanaplanacanalpanama" is a palindrome.
//
// Solution:
#include<iostream>
#include<string>
#include<algorithm>
#include<cctype>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        std::transform(s.begin(), s.end(), s.begin(), ::tolower);
        s.erase(
                std::remove_if(s.begin(), s.end(),
                    [](char c) { return !std::isalnum(c); }
                ),
                s.end()
            );
        int s_length = s.length();
        int loop_range = (s_length % 2 == 0) ? (s_length / 2): ((s_length - 1) / 2);

        for (int i = 0; i < loop_range; i++){
            if (s[i] != s[s_length - i - 1]){
                return false;
            }
        }
        return true;
    }
};

// Test Cases:
int main() {
    Solution sol;
    string str = "A man, a plan, a canal: Panama";
    cout << sol.isPalindrome(str) << endl;
    return 0;
}