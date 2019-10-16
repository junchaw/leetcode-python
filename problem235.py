# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of
# two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both
# p and q as descendants (where we allow a node to be a descendant of itself).”
#
# Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
#
#
#
#
# Example 1:
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant
# of itself according to the LCA definition.
#
#
# Note:
#
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the BST.
# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from tree import TreeNode, build_tree, pre_order


class Solution:
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode',
                              q: 'TreeNode') -> 'TreeNode':
        if root.val > p.val:
            if root.val <= q.val:
                return root
            else:
                return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val:
            if root.val >= q.val:
                return root
            else:
                return self.lowestCommonAncestor(root.right, p, q)
        return root

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root


def test(c):
    root = build_tree(c['nodes'])
    nodes = pre_order(root)
    p, q = None, None
    for node in nodes:
        if node.val == c['p']:
            p = node
        if node.val == c['q']:
            q = node
    if not p:
        raise Exception('Node p not exists')
    if not q:
        raise Exception('Node q not exists')

    s = Solution()
    result = s.lowestCommonAncestor(root, p, q)
    if result.val == c['expect']:
        print("Passed, nodes: {}, p: {}, q: {}, expected: {}".format(
            c['nodes'], c['p'], c['q'], c['expect']))
    else:
        print("Failed, nodes: {}, p: {}, q: {}, expected: {}, got: {}".format(
            c['nodes'], c['p'], c['q'], c['expect'], result.val))


def solve():
    test_cases = [
        {
            'nodes': [2, 1],
            'p': 1,
            'q': 2,
            'expect': 2,
        },
        {
            'nodes': [2, 1],
            'p': 2,
            'q': 1,
            'expect': 2,
        },
        {
            'nodes': [2, 1, 3],
            'p': 1,
            'q': 3,
            'expect': 2,
        },
        {
            'nodes': [5, 3, 7, 2, 4, 6, 8],
            'p': 6,
            'q': 8,
            'expect': 7,
        },
        {
            'nodes': [5, 3, 7, 2, 4, 6, 8],
            'p': 2,
            'q': 4,
            'expect': 3,
        },
        {
            'nodes': [5, 3, 7, 2, 4, 6, 8],
            'p': 4,
            'q': 8,
            'expect': 5,
        },
    ]
    for test_case in test_cases:
        test(test_case)
