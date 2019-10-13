# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:
#
# A linked list can be reversed either iteratively or recursively.
# Could you implement both?
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr is not None:
            curr.next, prev, curr = prev, curr, curr.next
        return prev


def build_linked_list(nums: List[int]) -> ListNode:
    p = ListNode(0)
    hook = p
    for n in nums:
        node = ListNode(n)
        p.next = node
        p = node
    return hook.next


def linked_list_to_list(head: ListNode) -> List[int]:
    p = head
    l = []
    while p is not None:
        l.append(p.val)
        p = p.next
    return l


class TestCase:
    def __init__(self, nums: List[int], expect: List[int]):
        self.nums = nums
        self.expect = expect


def test(c: TestCase):
    s = Solution()
    result = s.reverseList(build_linked_list(c.nums))
    resultList = linked_list_to_list(result)
    if resultList == c.expect:
        print("Passed, nums: {},  expect: {}".format(c.nums, c.expect))
    else:
        print("Expect {}, got {}".format(c.expect, resultList))


def solve():
    testCases = [
        TestCase([1], [1]),
        TestCase([1, 2], [2, 1]),
        TestCase([1, 2, 3], [3, 2, 1]),
    ]
    for testCase in testCases:
        test(testCase)
