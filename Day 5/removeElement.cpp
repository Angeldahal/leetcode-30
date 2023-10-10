// Problem Description:
// Given an array nums and a value val, remove all instances of that value in-place and return the new length.
// Example:
// Input: nums = [3,2,2,3], val = 3
// Output: 2, nums = [2,2]
// Note:
// Do not allocate extra space for another array, you must do this by modifying the input array in-place
// with O(1) extra memory.
// The order of elements can be changed. It doesn't matter what you leave beyond the new length.
//
// Solution:
#include<iostream>
#include<vector>
#include<assert.h>
using namespace std;
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int idx = 0;
        for (int i = 0; i < nums.size(); i++){
            if (nums[i] != val){
                nums[idx] = nums[i];
                idx++;
            }
        }
        return idx;
    }
};

// Testcases:
int main(){
    Solution solution;
    vector<int> nums = {3,2,2,3};
    cout << solution.removeElement(nums, 3) << endl;
    vector<int> nums2 = {0,1,2,2,3,0,4,2};
    cout << solution.removeElement(nums2, 2) << endl;
    return 0;
}