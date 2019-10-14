# https://leetcode.com/problems/reverse-nodes-in-k-group/
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
#
# k is a positive integer and is less than or equal to the length of the
# linked list. If the number of nodes is not a multiple of k then left-out
# nodes in the end should remain as it is.
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself
# may be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import List

from linked_list import ListNode, build_linked_list, linked_list_to_list


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k < 2:
            return head

        h = p = ListNode(0)
        p.next = head

        while True:
            q = p
            for _ in range(k):
                q = q.next
                if q is None:
                    return h.next # no enough nodes

            # another round (q is now the tail of the loop)
            loop_head, loop_tail = p.next, p.next.next
            for _ in range(k - 1):
                p.next, loop_head.next, loop_tail.next, loop_tail = \
                    loop_head.next, loop_tail.next, p.next, loop_tail.next
            p = loop_head

        return h.next


class TestCase:
    def __init__(self, nums: List[int], k: int, expect: List[int]):
        self.nums = nums
        self.k = k
        self.expect = expect


def test(c: TestCase):
    s = Solution()
    result = s.reverseKGroup(build_linked_list(c.nums), c.k)
    resultList = linked_list_to_list(result)
    if resultList == c.expect:
        print("Nums: {}, k: {}, expect: {}, passed".format(
            c.nums, c.k, c.expect))
    else:
        print("Nums: {}, k: {}, expect {}, got {}".format(
            c.nums, c.k, c.expect, resultList))


def solve():
    testCases = [
        TestCase([], 1, []),
        TestCase([1], 1, [1]),
        TestCase([1], 2, [1]),
        TestCase([1, 2], 1, [1, 2]),
        TestCase([1, 2], 2, [2, 1]),
        TestCase([1, 2], 3, [1, 2]),
        TestCase([1, 2, 3, 4], 1, [1, 2, 3, 4]),
        TestCase([1, 2, 3, 4], 2, [2, 1, 4, 3]),
        TestCase([1, 2, 3, 4], 3, [3, 2, 1, 4]),
    ]
    for testCase in testCases:
        test(testCase)
