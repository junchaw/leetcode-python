# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself
# may be changed.
#
#
#
# Example:
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        new_head = p = ListNode(0)
        p.next = head
        while p.next is not None and p.next.next is not None:
            a, b = p.next, p.next.next
            p.next, a.next, b.next, p = b, b.next, a, a
        return new_head.next


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
    result = s.swapPairs(build_linked_list(c.nums))
    resultList = linked_list_to_list(result)
    if resultList == c.expect:
        print("Nums: {}, expect: {}, passed".format(c.nums, c.expect))
    else:
        print("Nums: {}, expect {}, got {}".format(c.nums,
                                                   c.expect, resultList))


if __name__ == '__main__':
    testCases = [
        TestCase([], []),
        TestCase([1], [1]),
        TestCase([1, 2], [2, 1]),
        TestCase([1, 2, 3], [2, 1, 3]),
        TestCase([1, 2, 3, 4], [2, 1, 4, 3]),
    ]
    for testCase in testCases:
        test(testCase)
