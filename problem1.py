# Given an array of integers, return indices of the two numbers such that
# they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you
# may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        expect = {}
        for i, n in enumerate(nums):
            if n in expect:
                return [expect[n], i]
            expect[target - n] = i
        raise RuntimeError


class TestCase:
    def __init__(self, nums: List[int], target: int, expect: List[int]):
        self.nums = nums
        self.target = target
        self.expect = expect


def test(c: TestCase):
    s = Solution()
    result = s.twoSum(c.nums, c.target)
    assert result == c.expect, "Expect {}, got {}".format(c.expect, result)
    print("Passed, nums: {}, target: {}, expect: {}".format(
        c.nums, c.target, c.expect))


if __name__ == '__main__':
    testCases = [
        TestCase([2, 7, 11, 15], 9, [0, 1]),
        TestCase([2, 7, 11, 15], 22, [1, 3]),
        TestCase([0, 4, 3, 0], 0, [0, 3]),
        TestCase([-1, -2, -3, -4, -5], -8, [2, 4]),
    ]
    for testCase in testCases:
        test(testCase)
