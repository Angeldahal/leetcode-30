// Problem Description:
// Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
// Example:
// Input: nums1 = [1,2,3,0,0,0], m = 3
//        nums2 = [2,5,6],       n = 3
// Output: [1,2,2,3,5,6]
// Note:
// The number of elements initialized in nums1 and nums2 are m and n respectively.
// You may assume that nums1 has enough space (size that is greater or equal to m + n)
// to hold additional elements from nums2.


// Solution:
#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m -1;
        int j = n - 1;
        int k = m + n - 1;

        while (j>=0){
            if (i >= 0 && nums1[i] >= nums2[j]){
                nums1[k] = nums1[i];
                i--;
            }
            else {
                nums1[k] = nums2[j];
                j--;
            }
            k--;
        }
    }
};

int main(){
    Solution solution;
    vector<int> nums1 = {1,2,3,0,0,0};
    vector<int> nums2 = {2,5,6};
    solution.merge(nums1, 3, nums2, 3);
    for (int i = 0; i < nums1.size(); i++){
        cout << nums1[i] << " ";
    }
    cout << endl;
    return 0;
}