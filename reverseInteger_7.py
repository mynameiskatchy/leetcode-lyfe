"""
====================================================================================================
7. Reverse Integer
reverse()
<https://leetcode.com/problems/reverse-integer/>
<https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/>
====================================================================================================
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
----------
Input: 123
Output: 321

Example 2:
----------
Input: -123
Output: -321

Example 3:
----------
Input: 120
Output: 21

Note:
-----
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""

class Solution(object):
    def reverse(self, x):
        """
        This solution uses in-place mutations, and 2 pointers

        : type x: int
        : rtype: int

        1027 / 1032 test cases passed. missed the 2**31 condition
        1030 / 1032 test cases passed. missed the 2**31 condition on negative side

        Runtime: 20 ms, faster than 74.48% of Python online submissions for Reverse Integer.
        Memory Usage: 12.7 MB, less than 77.27% of Python online submissions for Reverse Integer.

        Runtime: 16 ms, faster than 90.97% of Python online submissions for Reverse Integer.
        Memory Usage: 12.6 MB, less than 95.71% of Python online submissions for Reverse Integer.

        Runtime: 28 ms, faster than 21.52% of Python online submissions for Reverse Integer.
        Memory Usage: 12.6 MB, less than 93.36% of Python online submissions for Reverse Integer.
        """

        digits = [d for d in str(x)]
        end = len(digits) - 1
        start = 0

        # adding plus one fixes issue, but then we swapping one extra time
        while(start <= end):
            if digits[start] != '-':
                digits[start], digits[end] = digits[end], digits[start]
                start += 1
                end -= 1
            else:
                start += 1
        
        new_val = int(''.join(digits))
        return 0 if abs(new_val) > 2**31 else new_val

    def reverse1(self, x):
        """
        This solution uses in-place mutations, and only one pointer

        : type x: int
        : rtype: int

        Issues with cases where 2 digits
        973 / 1032 test cases passed. Didnt take into account small numbers
        978 / 1032 test cases passed. Didnt take into account i < pointer
        """
        digits = [d for d in str(x)]
        pointer = len(digits)-1

        # adding plus one fixes issue, but then we swapping one extra time
        for i in (range((len(digits)//2)+1)): 
            if digits[i] != '-' and i < pointer:
                digits[i], digits[pointer] = digits[pointer], digits[i]
                pointer -= 1

        return int(''.join(digits))

if __name__ == "__main__":
    input1 = 123
    output1 = 321
    input2 = -123
    output2 = -321
    input3 = 120
    output3 = 21
    input4 = -10
    output4 = -1
    input5 = 10
    output5 = 1
    input6 = 901000
    output6 = 109
    input7 = 1534236469
    output7 = 9646324351
    input8 = -2147483648
    output8 = -8463847412

    s = Solution()
    a = s.reverse(input1)
    b = s.reverse(input2)
    c = s.reverse(input3)
    d = s.reverse(input4)
    e = s.reverse(input5)
    f = s.reverse(input6)
    g = s.reverse(input7)
    h = s.reverse(input8)

    print(a, b, c, d, e, f, g, h)
    pass
