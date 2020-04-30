"""
=======================================================================
1389. Create Target Array in the Given Order
createTargetArray()
<https://leetcode.com/problems/create-target-array-in-the-given-order/>
=======================================================================

Given two arrays of integers nums and index. 
Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], 
insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.

Example 1:
----------
Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]

Example 2:
----------
Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
Output: [0,1,2,3,4]
Explanation:
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]

Example 3:
----------
Input: nums = [1], index = [0]
Output: [1]

Constraints:
------------
1 <= nums.length, index.length <= 100
nums.length == index.length
0 <= nums[i] <= 100
0 <= index[i] <= i

"""


class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]

        Runtime: 16 ms, faster than 92.29% of Python online submissions for Create Target Array in the Given Order.
        Memory Usage: 13.1 MB, less than 100.00% of Python online submissions for Create Target Array in the Given Order.
        """
        len = nums.__len__()
        arr = [-1] * len
        for n in range(0, len):
            i = index[n] 
            if arr[i] == -1:
                arr[i] = nums[i]
            else:
                arr = arr[:i] + [nums[n]] + arr[i:-1]
        return arr

    def createTargetArray_2(self, nums, index):
        target = []
        for i in zip(nums, index):
            target.insert(i[1], i[0])
        return target

if __name__ == "__main__":
    nums1, index1, output1 = [0, 1, 2, 3, 4], [0, 1, 2, 2, 1], [0, 4, 1, 3, 2]
    nums2, index2, output2 = [1, 2, 3, 4, 0], [0, 1, 2, 3, 0], [0, 1, 2, 3, 4]
    nums3, index3, output3 = [1], [0], [1]

    s = Solution()
    a = s.createTargetArray(nums1, index1)
    b = s.createTargetArray(nums2, index2)
    c = s.createTargetArray(nums3, index3)

    print(a)
    print(b)
    print(c)


""" Resources

    https://leetcode.com/problems/create-target-array-in-the-given-order/

"""
