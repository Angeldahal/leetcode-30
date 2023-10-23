"""
Problem Description:
    Given a linked list, determine if it has a cycle in it.
    To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to.
    If pos is -1, then there is no cycle in the linked list.
Example:
    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list, where tail connects to the second node.
    Input: head = [1,2], pos = 0
    Output: true
    Explanation: There is a cycle in the linked list, where tail connects to the first node.
    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle in the linked list.

"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


# Test Cases:
if __name__ == "__main__":
    solution = Solution()

    # Initializing the nodes
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    print(solution.hasCycle(node1))

    # Another Test Node
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node2.next = node1

    print(solution.hasCycle(node1))

    # Negative Test Case
    node1 = ListNode(1)
    print(solution.hasCycle(node1))
