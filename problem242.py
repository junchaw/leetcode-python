# https://leetcode.com/problems/valid-anagram/
# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        for c in s:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1
        for c in t:
            if c in m:
                if m[c] > 1:
                    m[c] -= 1
                else:
                    m.pop(c)
            else:
                return False
        return len(m) == 0


def test(c):
    s = Solution()
    result = s.isAnagram(c['s'], c['t'])
    if c['expect']:
        p = ''
    else:
        p = 'not '

    if result == c['expect']:
        print('Passed, "{}" and "{}" is {}anagram'.format(
            c['s'], c['t'], p))
    else:
        print('Failed, "{}" and "{}" is {}anagram'.format(
            c['s'], c['t'], p))


def solve():
    testCases = [
        {
            's': '',
            't': '',
            'expect': True,
        },
        {
            's': '',
            't': 'a',
            'expect': False,
        },
        {
            's': 'anagram',
            't': 'nagaram',
            'expect': True,
        },
        {
            's': 'rat',
            't': 'car',
            'expect': False,
        }
    ]
    for testCase in testCases:
        test(testCase)
