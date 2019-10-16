# https://leetcode.com/problems/kth-largest-element-in-a-stream/
#
# Design a class to find the kth largest element in a stream. Note that
# it is the kth largest element in the sorted order, not the kth distinct
# element.
#
# Your KthLargest class will have a constructor which accepts an integer k
# and an integer array nums, which contains initial elements from the stream.
# For each call to the method KthLargest.add, return the element representing
# the kth largest element in the stream.
#
# Example:
#
# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   // returns 4
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8
# Note:
# You may assume that nums' length ≥ k-1 and k ≥ 1.

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]


def test(c):
    k = KthLargest(c['k'], c['initial'])
    passed = True
    for add in c['add']:
        n = add[0]
        expect = add[1]
        result = k.add(n)
        if result == expect:
            print('  Passed, added: {}, expect: {}'.format(n, expect))
        else:
            passed = False
            print('  Added: {}, expect: {}, got: {}'.format(n, expect, result))
    if passed:
        tmpl = 'Initial: {}, k: {}, Passed.'
    else:
        tmpl = 'Initial: {}, k: {}, Failed.'
    print(tmpl.format(c['initial'], c['k']), '\n')


def solve():
    testCases = [
        {
            'initial': [1],
            'k': 1,
            'add': [
                [1, 1],
                [2, 2],
            ]
        },
        {
            'initial': [1, 2, 3],
            'k': 2,
            'add': [
                [4, 3],
                [5, 4],
                [1, 4],
            ],
        },
    ]
    for testCase in testCases:
        test(testCase)
