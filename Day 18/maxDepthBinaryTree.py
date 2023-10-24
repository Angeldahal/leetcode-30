"""
Problem Description:
    Given the root of a binary tree, return its maximum depth.
    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Example:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3
    Input: root = [1,null,2]
    Output: 2
    Input: root = []
    Output: 0
    Input: root = [0]
    Output: 1
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_depth_left = self.maxDepth(root.left)
        max_depth_right = self.maxDepth(root.right)
        return max(max_depth_left, max_depth_right) + 1


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
    print(solution.maxDepth(TreeNode(1, None, TreeNode(2))))
    print(solution.maxDepth(None))
    print(solution.maxDepth(TreeNode(0)))