// Problem Description:
// Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
//
// Do not allocate extra space for another array,
// you must do this by modifying the input array in-place with O(1) extra memory.
//
// Example 1:
//   Given nums = [1,1,2],
//   Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
//   It doesn't matter what you leave beyond the returned length.
//
// Solution:
#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int idx = 1;
        for (int i = 1; i < nums.size(); i++){
            if (nums[i] != nums[i-1]){
                nums[idx] = nums[i];
                idx++;
            }
        }
        return idx;
    }
};

int main(){
    Solution test;
    vector<int> nums = {1,1,2};
    cout << test.removeDuplicates(nums) << endl;
    vector<int> nums2 = {1, 2, 3, 3, 4, 4, 5};
    cout << test.removeDuplicates(nums2) << endl;
    return 0;
}