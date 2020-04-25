"""
========================================
1221. Split a String in Balanced Strings
balancedStringSplit()
========================================

Balanced strings are those who have equal quantity of 'L' and 'R' characters.
Given a balanced string s split it in the maximum amount of balanced strings.
Return the maximum amount of splitted balanced strings.

Example 1:
----------
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Example 2:
----------
Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

Example 3:
----------
Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".

Example 4:
----------
Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'

Constraints:
------------
1 <= s.length <= 1000
s[i] = 'L' or 'R'

"""

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """

        return

if __name__ == "__main__":
    in1, out1 = "RLRRLLRLRL", 4
    in2, out2 = "RLLLLRRRLR", 3
    in3, out3 = "LLLLRRRR", 1
    in4, out4 = "RLRRRLLRLL", 2

    s = Solution()
    a = s.findNumbers(in1)
    b = s.findNumbers(in2)
    c = s.findNumbers(in3)
    d = s.findNumbers(in4)

    print(a)
    print(b)



""" Resources

    https://leetcode.com/problems/split-a-string-in-balanced-strings/

"""
