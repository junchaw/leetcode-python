# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given
# nodes in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of itself).”
#
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
#
#
#
#
# Example 1:
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
# of itself according to the LCA definition.
#
#
# Note:
#
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the binary tree.

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from problems.tree import TreeNode, build_tree, in_order


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left:
            if right:
                return root
            return left
        return right






def test(c):
    root = build_tree(c['nodes'])
    nodes = in_order(root)
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
            'nodes': [2, 3, 1],
            'p': 1,
            'q': 3,
            'expect': 2,
        },
        {
            'nodes': [5, 7, 3, 6, 4, 8, 2],
            'p': 6,
            'q': 4,
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
            'p': 6,
            'q': 8,
            'expect': 7,
        },
    ]
    for test_case in test_cases:
        test(test_case)
