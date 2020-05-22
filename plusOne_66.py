
"""
====================================================================================================
66. Plus One
plusOne()
<https://leetcode.com/problems/plus-one/>
<https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/>
====================================================================================================

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, 
and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
----------
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
----------
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]

        """

        digits[-1] += 1
        if digits[-1] > 9:
            digits = [0] + digits
            i = len(digits) - 1
            while(digits[i] > 9 and i > 0):
                digits[i] = 0
                digits[i-1] += 1
                i -= 1

        return digits if digits[0] != 0 else digits[1:]

    def plusOne_iterative(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        Runtime: 20 ms, faster than 69.37% of Python online submissions for Plus One.
        Memory Usage: 12.6 MB, less than 6.25% of Python online submissions for Plus One.

        Runtime: 40 ms, faster than 5.90% of Python online submissions for Plus One.
        Memory Usage: 12.7 MB, less than 6.25% of Python online submissions for Plus One.
        """

        digits[-1] += 1
        if digits[-1] > 9:
            digits = [0] + digits
            i = len(digits) - 1
            while(digits[i] > 9 and i > 0):
                digits[i] = 0
                digits[i-1] +=1
                i -= 1
                
        return digits if digits[0] != 0 else digits[1:]

    def plusOne_1(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        Runtime: 16 ms, faster than 89.82% of Python online submissions for Plus One.
        Memory Usage: 12.7 MB, less than 6.25% of Python online submissions for Plus One.

        Runtime: 20 ms, faster than 68.78% of Python online submissions for Plus One.
        Memory Usage: 12.8 MB, less than 6.25% of Python online submissions for Plus One.

        Runtime: 40 ms, faster than 5.56% of Python online submissions for Plus One.
        Memory Usage: 12.8 MB, less than 6.25% of Python online submissions for Plus One.
        """

        s = [str(i) for i in digits]   # ['1', '2', '3']
        merge_s = ''.join(s)  #  '123'
        sum = int(merge_s) + 1   # 123 + 1 = 124
        stringify = str(sum)   # '124'
        return [int(i) for i in list(stringify)]

    
if __name__ == "__main__":
    digits1 = [1, 2, 3]
    output1 = [1, 2, 4]
    digits2 = [4, 3, 2, 1]
    output2 = [4, 3, 2, 2]
    digits3 = [9,9]
    output3 = [1, 0, 0]
    digits4 = [1, 9]
    output4 = [2, 0]
    digits5 = [9]
    output5 = [1, 0]
    digits6 = [9, 9, 9]
    output = [1, 0, 0, 0]
    digits7 = [8, 9, 9, 9]
    output = [9, 0, 0, 0]

    s = Solution()
    a = s.plusOne(digits1)
    b = s.plusOne(digits2)
    c = s.plusOne(digits3)
    d = s.plusOne(digits4)
    e = s.plusOne(digits5)
    f = s.plusOne(digits6)
    g = s.plusOne(digits7)
    print(a, b, c, d, e, f, g)
    pass
