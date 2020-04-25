"""
==========================================================
1281. Subtract the Product and Sum of Digits of an Integer
subtractProductAndSum()
==========================================================

Given an integer number n, return the difference 
between the product of its digits and the sum of its digits.
 
Example 1:
----------
Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15

Example 2:
----------
Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21

Constraints:
------------
1 <= n <= 10^5
"""


class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int

        Runtime: 12 ms, faster than 91.89% of Python online submissions for Subtract the Product and Sum of Digits of an Integer.
        Memory Usage: 12.8 MB, less than 100.00% of Python online submissions for Subtract the Product and Sum of Digits of an Integer.
        """
        nums = [int(x) for x in str(n)]
        prod_nums = 1
        sum_nums = 0
        
        for i in nums:
            prod_nums *= i
            sum_nums += i

        return prod_nums - sum_nums

if __name__ == "__main__":
    in1, out1 = 234, 15
    in2, out2 = 4421, 21

    s = Solution()
    a = s.subtractProductAndSum(in1)
    b = s.subtractProductAndSum(in2)
    print(a)
    print(b)
    pass
