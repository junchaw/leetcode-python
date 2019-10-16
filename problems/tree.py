from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_tree(nums: List[int]):
    if not nums:
        return None

    nums = nums.copy()

    root = TreeNode(nums.pop(0))

    cap = 2
    parents = [root]
    t = []
    while nums:
        for i in range(cap):
            if not nums:
                break
            n = TreeNode(nums.pop(0))
            t.append(n)
            if i % 2 == 0:
                parents[i // 2].left = n
            else:
                parents[i // 2].right = n
            cap *= 2
        parents = t

    return root


# in_order returns list of tree nodes
def in_order(root: TreeNode) -> List[TreeNode]:
    if not root:
        return []

    return in_order(root.left) + [root] + in_order(root.right)
