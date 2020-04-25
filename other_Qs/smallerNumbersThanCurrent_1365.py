"""
==========================================================
1365. How Many Numbers Are Smaller Than the Current Number
smallerNumbersThanCurrent()
==========================================================

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
That is, for each nums[i] you have to count the number of valid j's such that 
j != i and nums[j] < nums[i].

Return the answer in an array.

Example 1:
----------
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

Example 2:
----------
Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]
 
Constraints:
------------
2 <= nums.length <= 500
0 <= nums[i] <= 100

"""

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Runtime: 44 ms, faster than 78.53% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.
        Memory Usage: 13.1 MB, less than 100.00% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.
        """
        sorted_nums = sorted(nums)
        sorted_nums.sort(reverse=True)
        count_dict = {}
        count_list = []
        len = nums.__len__()

        for i in range(len):
            if sorted_nums[i:i+1] == sorted_nums[i+1:i+2]:   # check if dupe
                continue
            else:   # count if not a dupe
                count_dict[sorted_nums[i]] = len - (i+1)

        for i, val in enumerate(nums):
            count_list.append(count_dict[val])

        return count_list


    def smallerNumbersThanCurrent_method1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Runtime: 228 ms, faster than 45.08% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.
        Memory Usage: 12.8 MB, less than 100.00% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.
        """
        count_smaller_list = []
        new_nums = nums[:]
        
        for i, val in enumerate(nums):
            bigger = new_nums.pop(i)   # remove val of interest (but not necessary)
            small_nums = [num for num in new_nums if num < bigger]   # filter with list comprehension
            count = small_nums.__len__()
            count_smaller_list.append(count)
            new_nums = nums[:]   # reset nums

        return count_smaller_list

if __name__ == "__main__":
    in1, out1 = [8, 1, 2, 2, 3], [4, 0, 1, 1, 3]
    in2, out2 = [6, 5, 4, 8], [2, 1, 0, 3]

    s = Solution()
    a = s.smallerNumbersThanCurrent(in1)
    b = s.smallerNumbersThanCurrent(in2)

    print(a)
    print(b)


""" Resources
    https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3
"""
