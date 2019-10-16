# https://leetcode.com/problems/sliding-window-maximum/
#
# Given an array nums, there is a sliding window of size k which is moving
# from the very left of the array to the very right. You can only see the k
# numbers in the window. Each time the sliding window moves right by one
# position. Return the max sliding window.
#
# Example:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Note:
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty
# array.
#
# Follow up:
# Could you solve it in linear time?
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = []
        for i, n in enumerate(nums):
            if window and window[0] <= i - k:
                window.pop(0)
            while window and nums[window[-1]] < n:
                window.pop()
            window.append(i)
            if i >= k - 1:
                result.append(nums[window[0]])
        return result


def test(c):
    s = Solution()
    result = s.maxSlidingWindow(c['nums'], c['k'])
    if result == c['expect']:
        print('Passed, nums: {}, k: {}, expect: {}'.format(
            c['nums'], c['k'], c['expect']))
    else:
        print('Failed, nums: {}, k: {}, expect: {}, got: {}'.format(
            c['nums'], c['k'], c['expect'], result))


def solve():
    test_cases = [
        {
            'nums': [],
            'k': 3,
            'expect': [],
        },
        {
            'nums': [1, 3, 2],
            'k': 1,
            'expect': [1, 3, 2],
        },
        {
            'nums': [1, 3, 2],
            'k': 2,
            'expect': [3, 3],
        },
        {
            'nums': [1, 3, 2],
            'k': 3,
            'expect': [3],
        },
        {
            'nums': [1, 3, -1, -3, 5, 3, 6, 7],
            'k': 3,
            'expect': [3, 3, 5, 5, 6, 7],
        },
    ]
    for test_case in test_cases:
        test(test_case)
