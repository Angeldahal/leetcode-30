// Problem Description:
// Given the head of a singly linked list, return the middle node of the linked list.
// If there are two middle nodes, return the second middle node.

// Example :
// Input: head = [1,2,3,4,5]
// Output: [3,4,5]
// Explanation: The middle node of the list is node 3.

/**
 * Definition for singly-linked list.
 **/
 #include<iostream>
 using namespace std;
 struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast != nullptr && fast->next != nullptr){
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
};

// Using the solution
int main(){
    Solution s;
    ListNode* head = new ListNode(1);
    ListNode* temp = head;
    for(int i = 2; i <= 5; i++){
        temp->next = new ListNode(i);
        temp = temp->next;
    }
    ListNode* middle = s.middleNode(head);
    while(middle != nullptr){
        cout << middle->val << " ";
        middle = middle->next;
    }
    cout << endl;
}