//Problem Description:
//Given a string s of roman numerals, convert it to an integer.
//Example 1:
//  Input: s = "III"
//  Output: 3
//Example 2:
//  Input: s = "IV"
//  Output: 4
//Example 3:
//  Input: s = "IX"
//  Output: 9

// Solution:
#include<iostream>
#include<string>
#include<map>
#include<unordered_map>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        int n = 0;
        unordered_map<char, int> dictionary;

        dictionary['I'] = 1;
        dictionary['V'] = 5;
        dictionary['X'] = 10;
        dictionary['L'] = 50;
        dictionary['C'] = 100;
        dictionary['D'] = 500;
        dictionary['M'] = 1000;


        for (int i = 0; i < s.size(); i++){
            int currentChar = s[i];
            if (i == s.size() - 1){
                n += dictionary[currentChar];
                continue;
            }
            int futureChar = s[i + 1];
            if (dictionary[currentChar] < dictionary[futureChar]){
                n -= dictionary[currentChar];
            }
            else {
                n += dictionary[currentChar];
            }
        }
        return n;
    }
};


// Test Cases:
int main(){
    Solution testSolution;
    string s = "MCMXCIV"; // 1994
    cout << testSolution.romanToInt(s) << endl;
    return 0;
}