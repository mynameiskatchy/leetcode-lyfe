"""
=========================================================================================
26. Remove Duplicates from Sorted Array
removeDuplicates()
<https://leetcode.com/problems/remove-duplicates-from-sorted-array/>
<https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/>
=========================================================================================

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
----------
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
----------
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.

Clarification:
--------------
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, 
which means modification to the input array will be known to the caller as well.

Internally you can think of this:
---------------------------------
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Runtime: 92 ms, faster than 21.39% of Python online submissions for Remove Duplicates from Sorted Array.
        Memory Usage: 14.5 MB, less than 6.25% of Python online submissions for Remove Duplicates from Sorted Array.

        Runtime: 80 ms, faster than 37.80%  of Python online submissions for Remove Duplicates from Sorted Array.
        Memory Usage: 14.5 MB, less than 6.25% of Python online submissions for Remove Duplicates from Sorted Array.
        """

        for i in range(len(nums)):
            if nums[i+1:i+2] == []:
                return i + 1
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
                i -= 1   # doesnt work because i forces next value 


    def removeDuplicates_3(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Runtime: 92 ms, faster than 21.39% of Python online submissions for Remove Duplicates from Sorted Array.
        Memory Usage: 14.5 MB, less than 6.25% of Python online submissions for Remove Duplicates from Sorted Array.
       
        Runtime: 80 ms, faster than 37.80%  of Python online submissions for Remove Duplicates from Sorted Array.
        Memory Usage: 14.5 MB, less than 6.25% of Python online submissions for Remove Duplicates from Sorted Array.
        """

        i = 0
        while nums[i+1:i+2] != []:
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
            else:
                i += 1
                
        return i + 1

    def removeDuplicates_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Runtime: 60 ms, faster than 97.48% of Python online submissions for Remove Duplicates from Sorted Array.
        Memory Usage: 14.7 MB, less than 6.25% of Python online submissions for Remove Duplicates from Sorted Array.
        """
        nums[:] = sorted(list(set(nums)))
        return nums.__len__()

if __name__ == "__main__":
    s = Solution()
    a = s.removeDuplicates([1,1,2])   # output = 2
    b = s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])   # output = 5
    c = s.removeDuplicates([-1, 0, 0, 0, 0, 3, 3])   # output = 3
    print(a, b, c)
    pass


"""
<https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python>
"""
