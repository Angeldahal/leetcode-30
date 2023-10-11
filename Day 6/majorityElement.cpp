// Problem Description:
// Given a non-empty array of integers, return the majority element.
// The majority element is the element that appears more than ⌊n/2⌋ times.
// You may assume that the array is non-empty and the majority element always exist in the array.
// Example:
// Input: [3,2,3]
// Output: 3
// Input: [2,2,1,1,1,2,2]
// Output: 2

// Solution:
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    // Using the Boyer-Moore Voting Algorithm
    int majorityElement(vector<int>& nums) {
        int count = 0;
        int candidate = 0;

        for (int num: nums){
            if (count == 0){
                candidate = num;
            }
            if (candidate == num){
                count += 1;
            }
            else {
                count -= 1;
            }
        }
        return candidate;
    }
    // Using the Hashmap
    int majorityElement2(vector<int>& nums) {
        unordered_map<int, int> counts;
        int majority = 0;
        int majority_count = 0;

        for (int num: nums){
            counts[num] += 1;
            if (counts[num] > majority_count){
                majority = num;
                majority_count = counts[num];
            }
        }
        return majority;
    }

        int majorityElement3(vector<int>& nums) {
        unordered_map <int, int> hashmap;

        for (int num: nums){
            if (hashmap.find(num) != hashmap.end()){
                hashmap[num]++;
            }
            else {
                hashmap[num] = 1;
            }
        }
        auto pr = std::max_element(hashmap.begin(), hashmap.end(), [](const auto &x, const auto &y) {
                    return x.second < y.second;
                });
        return pr -> first;
    }
};

// TestCases:
int main(){
    Solution solution;
    vector<int> nums1{3,2,3};
    vector<int> nums2{2,2,1,1,1,2,2};
    cout << solution.majorityElement(nums1) << endl;
    cout << solution.majorityElement(nums2) << endl;
    cout << solution.majorityElement2(nums1) << endl;
    cout << solution.majorityElement2(nums2) << endl;
    cout << solution.majorityElement3(nums1) << endl;
    cout << solution.majorityElement3(nums2) << endl;
    return 0;
}