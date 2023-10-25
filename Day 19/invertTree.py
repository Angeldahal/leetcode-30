"""
Problem Description:
    Given the root of a binary tree, invert the tree, and return its root.
Example:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]
    Input: root = [2,1,3]
    Output: [2,3,1]
    Input: root = []
    Output: []
"""
# Solution:
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left
        return root


# Test Cases:
if __name__ == "__main__":
    solution = Solution()
    print(solution.invertTree(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))))
    print(solution.invertTree(TreeNode(2, TreeNode(1), TreeNode(3))))
    print(solution.invertTree(None))

