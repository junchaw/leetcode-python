from typing import List


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def build_linked_list(nums: List, loop_at: int = -1) -> ListNode:
    hook = p = ListNode(0)

    if len(nums) < 1:
        return hook.next  # None

    if loop_at == -1:  # no loop
        for n in nums:
            node = ListNode(n)
            p.next = node
            p = node
    else:
        loop_record = None
        for i, n in enumerate(nums):
            node = ListNode(n)
            if i == loop_at:
                loop_record = node
            p.next = node
            p = node
        if loop_record:
            p.next = loop_record

    return hook.next


def linked_list_to_list(head: ListNode) -> List:
    l = []
    seen = set()
    while head is not None:
        if head in seen:
            l.append("Cycled, tail connects to <{}>".format(head.val))
            return l
        seen.add(head)
        l.append(head.val)
        head = head.next
    return l
