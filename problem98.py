# https://leetcode.com/problems/validate-binary-search-tree/
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the
# node's key.
# The right subtree of a node contains only nodes with keys greater than
# the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
# Example 1:
#
#     2
#    / \
#   1   3
#
# Input: [2,1,3]
# Output: true
# Example 2:
#
#     5
#    / \
#   1   4
#      / \
#     3   6
#
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_tree(nums: List[int]):
    if not nums:
        return None

    nums = nums.copy()

    root = TreeNode(nums.pop(0))

    cap = 2
    parents = [root]
    t = []
    while nums:
        for i in range(cap):
            if not nums:
                break
            n = TreeNode(nums.pop(0))
            t.append(n)
            if i % 2 == 0:
                parents[i // 2].left = n
            else:
                parents[i // 2].right = n
            cap *= 2
        parents = t

    return root


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, prev = [], None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev is not None and root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True


def test(c):
    s = Solution()
    result = s.isValidBST(build_tree(c['nodes']))
    if c['expect']:
        p = ''
    else:
        p = 'not '
    if result == c['expect']:
        print("Passed, nodes: {} is {}BST".format(c['nodes'], p))
    else:
        print("Failed, nodes: {} is {}BST".format(c['nodes'], p))


def solve():
    test_cases = [
        {
            'nodes': [1, 1],
            'expect': False,
        },
        {
            'nodes': [2, 1, 3],
            'expect': True,
        },
        {
            'nodes': [2, 3, 1],
            'expect': False,
        },
        {
            'nodes': [5, 3, 7, 2, 4, 6, 8],
            'expect': True,
        },
        {
            'nodes': [5, 4, 7, 2, 6, 8, 9],
            'expect': False,
        },
        {
            'nodes': [5, 3, 7, 2, 4, 6, 8, 1],
            'expect': True,
        },
    ]
    for test_case in test_cases:
        test(test_case)
