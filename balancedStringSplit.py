"""
==================================================================
1221. Split a String in Balanced Strings
balancedStringSplit()
<https://leetcode.com/problems/split-a-string-in-balanced-strings/>
===================================================================

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

        count = {
            'L': 0,
            'R': 0,
            'n': 0
        }

        for i in s:
            count[i] += 1

            if count['L'] == count['R']:
                count['n'] += 1

        return count['n']

    def balancedStringSplit_attempt1(self, s):
        """
        :type s: str
        :rtype: int

        Runtime: 16 ms, faster than 83.84% of Python online submissions for Split a String in Balanced Strings.
        Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for Split a String in Balanced Strings.
        """
        l = 0   # number of L's
        r = 0   # number of R's
        n = 0   # number of substrings

        for i in s:
            if i == 'L':
                l += 1
            else:
                r += 1

            if l == r:
                n += 1
                l = 0
                r = 0
        
        return n


if __name__ == "__main__":
    in1, out1 = "RLRRLLRLRL", 4
    in2, out2 = "RLLLLRRRLR", 3
    in3, out3 = "LLLLRRRR", 1
    in4, out4 = "RLRRRLLRLL", 2

    s = Solution()
    a = s.balancedStringSplit(in1)
    b = s.balancedStringSplit(in2)
    c = s.balancedStringSplit(in3)
    d = s.balancedStringSplit(in4)

    print(a)
    print(b)
    print(c)
    print(d)



""" Resources

    https://leetcode.com/problems/split-a-string-in-balanced-strings/

"""
