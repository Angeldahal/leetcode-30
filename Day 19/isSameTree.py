"""
Problem Description:
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.
    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
Example:
    Input: p = [1,2,3], q = [1,2,3]
    Output: true
    Input: p = [1,2], q = [1,null,2]
    Output: false
    Input: p = [1,2,1], q = [1,1,2]
    Output: false

"""
from typing import Optional


# Solution:
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p == q
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))))
    print(solution.isSameTree(TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2))))
    print(solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(1)), TreeNode(1, TreeNode(1), TreeNode(2))))
