//Problem Description:
//Given a string s, find the length of the last word.
//A word is a maximal substring consisting of non-space characters only.
//Example 1:
//  Input: s = "Hello World"
//  Output: 5
//Example 2:
//  Input: s = " "
//  Output: 0

// Solution:

#include<iostream>
#include<string>
using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        int n = s.length();
        int count = 0;
        int ans = 0;

        // Count trailing spaces
        for (int i = n - 1; i >= 0; i--) {
            if (s[i] == ' ') {
                count++;
            } else {
                break;
            }
        }

        // Count the length of the last word
        for (int i = n - 1 - count; i >= 0; i--) {
            if (s[i] != ' ') {
                ans++;
            } else {
                break;
            }
        }

        return ans;
    }
};

int main() {
    Solution sol;
    string s = "Hello World";
    cout << sol.lengthOfLastWord(s) << endl;
    return 0;
}
