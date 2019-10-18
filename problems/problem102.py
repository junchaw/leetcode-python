# https://leetcode.com/problems/binary-tree-level-order-traversal/
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

from typing import List

from problems.tree import TreeNode, build_tree


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        curr, nex = [root], []
        while curr:
            result.append([])
            while curr:
                node = curr.pop(0)
                if node:
                    if node.val is not None:
                        result[-1].append(node.val)
                    if node.left:
                        nex.append(node.left)
                    if node.right:
                        nex.append(node.right)
            if not result[-1]:
                result.pop()
            curr, nex = nex, []
        return result


def test(nums: List[int], expect: List[List[int]]):
    s = Solution()
    result = s.levelOrder(build_tree(nums))
    if result == expect:
        print("Passed, nums: {}, expected: {}".format(nums, expect))
    else:
        print("Failed, nums: {}, expected: {}, got: {}".format(
            nums, expect, result))


def solve():
    test_cases = [
        [[], []],
        [[1, None, 3], [[1], [3]]],
        [[1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]]]
    ]
    for test_case in test_cases:
        test(test_case[0], test_case[1])
