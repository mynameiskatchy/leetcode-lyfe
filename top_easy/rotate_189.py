"""
==============================================================================================
189. Rotate Array
rotate()
<https://leetcode.com/problems/rotate-array/>
<https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/>
==============================================================================================

Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
 

Example 1:
----------
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
----------
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 
Constraints:
------------
1 <= nums.length <= 2 * 10^4
It's guaranteed that nums[i] fits in a 32 bit-signed integer.
k >= 0

"""


class Solution(object):
    def rotate_inplace(self, nums, k):
        "TBD"
        return 0

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.

        Runtime: 52 ms, faster than 50.40% of Python online submissions for Rotate Array.
        Memory Usage: 13.7 MB, less than 6.25% of Python online submissions for Rotate Array.

        Runtime: 40 ms, faster than 97.76%  of Python online submissions for Rotate Array.
        Memory Usage: 13.6 MB, less than 6.25% of Python online submissions for Rotate Array.
        """
        x = len(nums)
        rotated = nums[x-k:] + nums[:x-k]

        for i in range(x):
            nums[i] = nums[x-k:] + nums[:x-k]                                                                                                                                              

        return None

    def rotate_1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.

        Runtime: 52 ms, faster than 50.40% of Python online submissions for Rotate Array.
        Memory Usage: 13.7 MB, less than 6.25% of Python online submissions for Rotate Array.

        Runtime: 40 ms, faster than 97.76%  of Python online submissions for Rotate Array.
        Memory Usage: 13.6 MB, less than 6.25% of Python online submissions for Rotate Array.
        """
        x = len(nums)
        rotated = nums[x-k:] + nums[:x-k]

        for i in range(x):
            nums[i] = nums[x-k:] + nums[:x-k]

        # A one-liner solution
        # nums[:] = nums[nums.__len__()-k:] + nums[:nums.__len__()-k]
        # Runtime: 36 ms, faster than 99.63% of Python online submissions for Rotate Array.

        return None

if __name__ == "__main__":
    nums1, k1= [1, 2, 3, 4, 5, 6, 7], 3
    output1 = [5, 6, 7, 1, 2, 3, 4]
    nums2, k2 = [-1, -100, 3, 99], 2
    output2 = [3, 99, -1, -100]

    s = Solution()
    a = s.rotate(nums1, k1)
    b = s.rotate(nums2, k2)
    print(a, b)

    pass
