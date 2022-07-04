"""
Problem:
    Given the root of a binary tree, invert the tree, and return its root.
v1:
    -- if the root is None, just return
    -- recurse through each side of the tree
    -- for each node, swap the left and the right
    -- return the root after the swap

"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        
        left: TreeNode = self.invertTree(root.left)
        right: TreeNode = self.invertTree(root.right)
        root.right = left
        root.left = right

        return root

"""
Results:
Runtime: 53 ms, faster than 33.97% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 13.9 MB, less than 56.41% of Python3 online submissions for Invert Binary Tree
"""