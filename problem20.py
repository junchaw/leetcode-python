# Given a string containing just the characters '(', ')', '{', '}',
# '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
#
# Input: "(]"
# Output: false
# Example 4:
#
# Input: "([)]"
# Output: false
# Example 5:
#
# Input: "{[]}"
# Output: true


class Solution:
    def isValid(self, s: str) -> bool:
        m = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c not in m:
                stack.append(c)
            else:
                if len(stack) < 1:
                    return False
                if stack[-1] != m[c]:
                    return False
                stack.pop()
        return len(stack) == 0


class TestCase:
    def __init__(self, s: str, expect: bool):
        self.s = s
        self.expect = expect


def test(c: TestCase):
    s = Solution()
    result = s.isValid(c.s)
    if result == c.expect:
        print("String: {},  expect: {}, passed".format(
            c.s, c.expect))
    else:
        print("String: {}, expect {}, got {}".format(
            c.s, c.expect, result))


def solve():
    testCases = [
        TestCase("", True),
        TestCase("(", False),
        TestCase("()", True),
        TestCase("()]", False),
        TestCase("[()", False),
        TestCase("()()[][]", True),
        TestCase("([{}])", True),
        TestCase("([{]})", False),
    ]
    for testCase in testCases:
        test(testCase)
