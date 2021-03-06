'''
104. Maximum Depth of Binary Tree
Easy

https://leetcode.com/problems/maximum-depth-of-binary-tree/
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        nleft = self.maxDepth(root.left)
        nright = self.maxDepth(root.right)

        return nleft + 1 if nleft > nright else nright + 1


