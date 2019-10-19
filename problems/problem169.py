# https://leetcode.com/problems/majority-element/
#
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example 1:
#
# Input: [3,2,3]
# Output: 3
# Example 2:
#
# Input: [2,2,1,1,1,2,2]
# Output: 2

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        maj = 0
        counter = 0
        for n in nums:
            if n in m:
                m[n] += 1
            else:
                m[n] = 1
            if m[n] > counter:
                maj = n
                counter = m[n]
        return maj


def test(nums: List[int], expect: int):
    s = Solution()
    result = s.majorityElement(nums)
    if result == expect:
        print('Passed, nums: {}, expected: {}'.format(nums, expect))
    else:
        print('Failed, nums: {}, expected: {}, got: {}'.format(
            nums, expect, result))


def solve():
    test_cases = [
        [[1], 1],
        [[1, 1, 2], 1],
        [[1, 2, 1, 2, 1, 2, 1, 2, 1], 1],
        [[1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3], 2],
    ]
    for test_case in test_cases:
        test(test_case[0], test_case[1])
