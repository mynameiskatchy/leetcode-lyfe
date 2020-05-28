"""
====================================================================================================
217. Contains Duplicate
containsDuplicate()
<https://leetcode.com/problems/contains-duplicate/>
<https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/>
====================================================================================================

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.

Example 1:
----------
Input: [1,2,3,1]
Output: true

Example 2:
----------
Input: [1,2,3,4]
Output: false

Example 3:
----------
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

class Solution(object):

    def containsDuplicate(self,nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return False
        return True

    def containsDuplicate_z(self, nums):
        """
        just testing something
        """
        d = dict()
        i = 0
        while (nums[i] not in d):
            return 0

    def containsDuplicate_2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        Runtime: 108 ms, faster than 59.06% of Python online submissions for Contains Duplicate.
        Memory Usage: 18.5 MB, less than 5.55% of Python online submissions for Contains Duplicate.
        """
        d = {}
        for i in nums:
            if i in d:
                return True
            else:
                d[i] = False
        return False

    def containsDuplicate_1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        Runtime: 104 ms, faster than 79.11% of Python online submissions for Contains Duplicate.
        Memory Usage: 18.1 MB, less than 5.55% of Python online submissions for Contains Duplicate.

        Runtime: 100 ms, faster than 92.33% of Python online submissions for Contains Duplicate.
        Memory Usage: 18 MB, less than 5.55% of Python online submissions for Contains Duplicate.
        """
        return True if len(set(nums)) < len(nums) else False
        # return len(set(nums)) < len(nums)

if __name__ == "__main__":
    input1 = [1, 2, 3, 1]
    output1 = True
    input2 = [1, 2, 3, 4]
    output2 = False
    input3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    output3 = True

    s = Solution()
    a = s.containsDuplicate(input1)
    b = s.containsDuplicate(input2)
    c = s.containsDuplicate(input3)

    print(a, b, c)
    pass
