from typing import List


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def build_linked_list(nums: List[int]) -> ListNode:
    p = ListNode(0)
    hook = p
    for n in nums:
        node = ListNode(n)
        p.next = node
        p = node
    return hook.next
