# https://leetcode.com/problems/linked-list-cycle-ii/
#
# Given a linked list, return the node where the cycle begins.
# If there is no cycle, return null.
#
# To represent a cycle in the given linked list, we use an integer pos
# which represents the position (0-indexed) in the linked list where tail
# connects to. If pos is -1, then there is no cycle in the linked list.
#
# Note: Do not modify the linked list.
#
#
#
# Example 1:
#
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects
# to the second node.
#
#
# Example 2:
#
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects
# to the first node.
#
#
# Example 3:
#
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.
#
#
#
#
# Follow-up:
# Can you solve it without using extra space?
#
# Accepted
# 245,528
# Submissions
# 727,134

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import List

from problems.linked_list import ListNode, build_linked_list


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        seen = set()
        while head is not None:
            if head in seen:
                return head
            seen.add(head)
            head = head.next


class TestCase:
    def __init__(self, nums: List[int], loop_at: int, expect: int):
        self.nums = nums
        self.loop_at = loop_at
        self.expect = expect


def test(c: TestCase):
    s = Solution()
    result = s.detectCycle(build_linked_list(c.nums, c.loop_at))
    if result:
        resultVal = result.val
    else:
        resultVal = 0
    if resultVal == c.expect:
        print("Nums: {}, loop at: {}, expect: {}, passed".format(
            c.nums, c.loop_at, c.expect))
    else:
        print("Nums: {}, loop at: {}, expect {}, got {}".format(
            c.nums, c.loop_at, c.expect, resultVal))


def solve():
    testCases = [
        TestCase([], -1, False),
        TestCase([1], -1, 0),
        TestCase([1], 0, 1),
        TestCase([1, 2], -1, 0),
        TestCase([1, 2], 0, 1),
        TestCase([1, 2], 1, 2),
        TestCase([1, 2, 3, 4], -1, 0),
        TestCase([1, 2, 3, 4], 0, 1),
        TestCase([1, 2, 3, 4], 3, 4),
    ]
    for testCase in testCases:
        test(testCase)
