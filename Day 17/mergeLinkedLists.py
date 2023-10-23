"""
Problem Description:
    Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
Example:
    Input: l1 = [1,2,4], l2 = [1,3,4]
    Output: [1,1,2,3,4,4]
    Input: l1 = [], l2 = []
    Output: []
    Input: l1 = [], l2 = [0]
    Output: [0]
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        final = result_node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                result_node.next = list1
                list1, result_node = list1.next, list1
            else:
                result_node.next = list2
                list2, result_node = list2.next, list2

        if list1 or list2:
            result_node.next = list1 if list1 else list2

        return final.next


# Test Cases:
if __name__ == "__main__":
    solution = Solution()

    # Initializing the nodes
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(4)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(1)
    node5 = ListNode(3)
    node6 = ListNode(4)
    node4.next = node5
    node5.next = node6

    result = solution.mergeTwoLists(node1, node4)
    print(result.val, result.next.val, result.next.next.val, result.next.next.next.val, result.next.next.next.next.val, result.next.next.next.next.next.val)
