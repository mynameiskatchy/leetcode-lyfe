"""
==================================================================
1313. Decompress Run-Length Encoded List
decompressRLElist()
<https://leetcode.com/problems/decompress-run-length-encoded-list>
==================================================================

We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  
For each such pair, there are freq elements with value val concatenated in a sublist. 
Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.

 
Example 1:

Input: nums = [1,2,3,4]
Output: [2,4,4,4]
Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].

Example 2:

Input: nums = [1,1,2,3]
Output: [1,3,3]
 

Constraints:

2 <= nums.length <= 100
nums.length % 2 == 0
1 <= nums[i] <= 100
"""


class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Runtime: 52 ms, faster than 86.43% of Python online submissions for Decompress Run-Length Encoded List.
        Memory Usage: 12.9 MB, less than 100.00% of Python online submissions for Decompress Run-Length Encoded List.
        """

        decomp_list = []
        rest = nums[:]   # copy nums list for manipulation

        for i in range(int(len(rest)/2)):
            pair = rest[0:2]   # [freq, val] pair
            decomp_list.extend([pair[1]] * pair[0])   # expand [freq, val] pair
            rest = rest[2:]    # remaining pairs

        return decomp_list

if __name__ == "__main__":
    in1, out1 = [1, 2, 3, 4], [2, 4, 4, 4]
    in2, out2 = [1, 1, 2, 3], [1, 3, 3]
    in3, out3 = [11, 5, 9, 2, 8, 1], [11, 11, 11, 11, 11, 9, 9, 8]
    in4 = [55, 11, 70, 26, 62, 64]

    s = Solution()
    # a = s.decompressRLElist(in1)
    # b = s.decompressRLElist(in2)
    c = s.decompressRLElist(in3)

    # print(a)
    # print(b)
    print(c)

    pass      






""" Resources
    https://thispointer.com/python-how-to-create-a-list-and-initialize-with-same-values/
"""
