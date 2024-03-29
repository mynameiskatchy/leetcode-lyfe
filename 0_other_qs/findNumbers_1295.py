"""
========================================================================
1295. Find Numbers with Even Number of Digits
findNumbers()
<https://leetcode.com/problems/find-numbers-with-even-number-of-digits>
========================================================================

Given an array nums of integers, return how many of them contain an even number of digits.
 
Example 1:
----------
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

Example 2:
----------
Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.

Constraints:
------------
1 <= nums.length <= 500
1 <= nums[i] <= 10^5

"""


class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Runtime: 36 ms, faster than 89.19% of Python online submissions for Find Numbers with Even Number of Digits.
        Memory Usage: 12.8 MB, less than 100.00% of Python online submissions for Find Numbers with Even Number of Digits.
        """

        even_digits = []

        for i in nums:
            if len(str(i)) % 2 == 0:
                even_digits.append(i)

        return even_digits.__len__()

if __name__ == "__main__":
    in1, out1 = [12, 345, 2, 6, 7896], 2
    in2, out2 = [555, 901, 482, 1771], 1

    s = Solution()
    a = s.findNumbers(in1)
    b = s.findNumbers(in2)

    print(a)
    print(b)

