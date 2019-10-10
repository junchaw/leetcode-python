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


def test(nums: List[int], target: int, expect: List[int]):
    s = Solution()
    result = s.twoSum(nums, target)
    assert result == expect, "Expect {}, got {}".format(expect, result)
    print("Passed, nums: {}, target: {}, expect: {}".format(
        nums, target, expect))


if __name__ == '__main__':
    test([2, 7, 11, 15], 9, [0, 1])
    test([2, 7, 11, 15], 22, [1, 3])
    test([0, 4, 3, 0], 0, [0, 3])
    test([-1, -2, -3, -4, -5], -8, [2, 4])
