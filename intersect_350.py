
"""
====================================================================================================
350. Intersection of Two Arrays II
intersect()
<https://leetcode.com/problems/intersection-of-two-arrays-ii/>
<https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/>
====================================================================================================

Given two arrays, write a function to compute their intersection.

Example 1:
----------
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
----------
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and 
the memory is limited such that you cannot load all elements into the memory at once?

"""

class Solution(object):

    def intersect_almost(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        sets dont work here because it removes duplicates 
        """
        return list(set(nums1) & set(nums2))

    def intersect_almost2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        This implimentation doesnt work because it doesnt necesarily show
        a particular number as many times as it shows in both arrays

        not returned as a list, and set operator not working
        """
        return set(nums1 and nums2)

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        Runtime: 104 ms, faster than 5.77% of Python online submissions for Intersection of Two Arrays II.
        Memory Usage: 12.8 MB, less than 5.13% of Python online submissions for Intersection of Two Arrays II.
        
        Runtime: 92 ms, faster than 7.11% of Python online submissions for Intersection of Two Arrays II.
        Memory Usage: 12.8 MB, less than 5.13% of Python online submissions for Intersection of Two Arrays II.
        """
        if len(nums1) >= len(nums2):
            # swap smaller one to nums1
            nums1, nums2 = nums2, nums1   
        
        d = dict()
        intersection = []
        # count frequencies using dictionaries 
        for i in nums2:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 0
        # stage ones that intersect by checking frequency
        for i in nums1:
            if i in d.keys() and d[i] >= 0:
                intersection.append(i)
                d[i] -= 1

        return intersection

            
                
        
if __name__ == "__main__":

    nums1a = [1, 2, 2, 1]
    nums1b = [2, 2]
    output1 = [2, 2]

    nums2a = [4, 9, 5]
    nums2b = [9, 4, 9, 8, 4]
    output2 = [4, 9]

    s = Solution()
    a = s.intersect(nums1a, nums1b)
    b = s.intersect(nums2a, nums2b)

    print(a, b)
    pass


"""
'and' vs '&' keywords/operators:
    https://stackoverflow.com/questions/22646463/and-boolean-vs-bitwise-why-difference-in-behavior-with-lists-vs-nump
    # 'and' is a boolean operator
    # '&' is a bitwise operator 
"""
