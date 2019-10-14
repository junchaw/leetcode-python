# https://leetcode.com/problems/linked-list-cycle/
#
# Given a linked list, determine if it has a cycle in it.
#
# To represent a cycle in the given linked list, we use an integer pos
# which represents the position (0-indexed) in the linked list where tail
# connects to. If pos is -1, then there is no cycle in the linked list.
#
#
#
# Example 1:
#
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to
# the second node.
#
#
# Example 2:
#
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects
# to the first node.
#
#
# Example 3:
#
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
#
#
#
# Follow up:
#
# Can you solve it using O(1) (i.e. constant) memory?
#
# Accepted
# 470,798
# Submissions
# 1,226,385

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import List

from linked_list import ListNode, build_linked_list


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        while head is not None:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False


class TestCase:
    def __init__(self, nums: List[int], loop_at: int, expect: bool):
        self.nums = nums
        self.loop_at = loop_at
        self.expect = expect


def test(c: TestCase):
    s = Solution()
    result = s.hasCycle(build_linked_list(c.nums, c.loop_at))
    if result == c.expect:
        print("Nums: {}, loop at: {}, expect: {}, passed".format(
            c.nums, c.loop_at, c.expect))
    else:
        print("Nums: {}, loop at: {}, expect {}, got {}".format(
            c.nums, c.loop_at, c.expect, result))


def solve():
    testCases = [
        TestCase([], -1, False),
        TestCase([1], -1, False),
        TestCase([1], 0, True),
        TestCase([1, 2], -1, False),
        TestCase([1, 2], 0, True),
        TestCase([1, 2], 1, True),
        TestCase([1, 2, 3, 4], -1, False),
        TestCase([1, 2, 3, 4], 0, True),
        TestCase([1, 2, 3, 4], 3, True),
    ]
    for testCase in testCases:
        test(testCase)
