from typing import Optional


# Problem Description:
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Example :
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Using the Fast and Slow method to find the middle of the linked list
# Fast pointer moves two steps at a time while slow pointer moves one step at a time
# When the fast pointer reaches the end of the linked list, the slow pointer will be at the middle of the linked list
# Time Complexity: O(n)
# Space Complexity: O(1)
#https://www.tutorialspoint.com/python-program-to-get-the-middle-element-of-a-linked-list-in-a-single-iteration#:~:text=To%20find%20the%20middle%20element,index%20of%20the%20middle%20element.
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow


# Using the Solution
listNode = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution = Solution()
print(solution.middleNode(listNode).val)
