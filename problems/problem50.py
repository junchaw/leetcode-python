# https://leetcode.com/problems/powx-n/
#
# Implement pow(x, n), which calculates x raised to the power n (xn).
#
# Example 1:
#
# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:
#
# Input: 2.10000, 3
# Output: 9.26100
# Example 3:
#
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
# Note:
#
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−231, 231 − 1]


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        elif n == 0:
            return 1
        elif n == 1:
            return x
        if n & 1:
            return x * self.myPow(x * x, n >> 1)
        return self.myPow(x * x, n >> 1)


def test(x, n, expect):
    s = Solution()
    result = s.myPow(x, n)
    if result == expect:
        print("Passed, x: {}, n: {}, expected: {}".format(x, n, expect))
    else:
        print("Failed, x: {}, n: {}, expected: {}, got: {}".format(
            x, n, expect, result))


def solve():
    test_cases = [
        [2, -2, 0.25],
        [2, -1, 0.5],
        [2, 0, 1],
        [2, 1, 2],
        [2, 2, 4],
        [2, 3, 8],
        [2, 10, 1024],
        [3, 2, 9]
    ]
    for test_case in test_cases:
        test(test_case[0], test_case[1], test_case[2])
