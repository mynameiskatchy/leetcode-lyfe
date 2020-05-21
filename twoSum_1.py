
"""
====================================================================================================
1. Two Sum
twoSum()
<https://leetcode.com/problems/two-sum/>
<https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/>
====================================================================================================

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
--------
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Runtime: 60 ms, faster than 46.27% of Python online submissions for Two Sum.
        Memory Usage: 14.4 MB, less than 5.13% of Python online submissions for Two Sum.

        """
        d = {nums[i]: i for i in range(len(nums))} #if it's same number it will overwrite
        for i, val1 in enumerate(nums):
            val2 = target - val1 
            if d.get(val2) and i != d[val2]: 
                return [i, d[val2]]

    def twoSum_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Runtime: 3968 ms, faster than 26.27% of Python online submissions for Two Sum.
        Memory Usage: 13.4 MB, less than 11.30% of Python online submissions for Two Sum.

        This one has two nested loops so slow
        """
        
        for i, val1 in enumerate(nums):
            counter = 0
            for val2 in nums[i+1:]:
                counter += 1
                if val1 + val2 == target:
                    return [i, (counter + i)]


    def twoSum_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Runtime: 2860 ms, faster than 28.50% of Python online submissions for Two Sum.
        Memory Usage: 13.4 MB, less than 12.33% of Python online submissions for Two Sum.
        """

        for i, val1 in enumerate(nums):
            check = target - val1
            counter = 0
            for val2 in nums[i+1:]:
                counter += 1
                if val2 == check:
                    return [i, (counter + i)]

    
if __name__ == "__main__":
    nums1 = [2, 7, 11, 15]
    target1 = 9
    output1 = [0, 1]
    nums2 = [3, 2, 4]
    target2 = 6
    output2 = [1, 2]
    nums3 = [3, 2, 3]
    target3 = 6
    output = [0, 2]

    s = Solution()
    a = s.twoSum(nums1, target1)
    b = s.twoSum(nums2, target2)
    c = s.twoSum(nums3, target3)
    print(a, b, c)
    pass
