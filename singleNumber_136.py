"""
====================================================================================================
136. Single Number
singleNumber()
<https://leetcode.com/problems/single-number/>
<https://leetcode.com/explore/iginterview/card/top-interview-questions-easy/92/array/549/>
====================================================================================================

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
----------
Input: [2,2,1]
Output: 1

Example 2:
----------
Input: [4,1,2,1,2]
Output: 4
"""


class Solution(object):
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Runtime: 60 ms, faster than 99.02% of Python online submissions for Single Number.
        Memory Usage: 15 MB, less than 5.40% of Python online submissions for Single Number.

        Time Complexity: This one super smart O(2n)
        """
         
        return 2 * sum(set(nums)) - sum(nums)
                
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Runtime: 80 ms, faster than 38.45% of Python online submissions for Single Number.
        Memory Usage: 14.5 MB, less than 5.40% of Python online submissions for Single Number.

        Runtime: 72 ms, faster than 68.49% of Python online submissions for Single Number.
        Memory Usage: 14.6 MB, less than 5.40% of Python online submissions for Single Number.
        
        Time complexity: O(nlogn) to sort + O(n) to loop
        """
        nums.sort()  # O(nlogn)
        for i in range(0, len(nums), 2): # O(n)
            if nums[i:i+1] != nums[i+1:i+2]:
                return nums[i]

        

        # for i in range(0, len(nums) - 1, 2):
        #     if nums[i] != nums[i + 1]:
        #         return nums[i]
        # return nums[len(nums) - 1]
            

    def singleNumber_recursive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        14 / 16 test cases passed. Last test case is v big
        """
        nums.sort()
        for i in range(0, len(nums), 2):
            if nums[i:i+1] != nums[i+1:i+2]:
                return nums[i:i+1][0]
            else:
                return self.singleNumber_recursive2(nums[2:])

    def singleNumber_recursive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        15 / 16 test cases passed. Last test case is v big
        """
        nums.sort()
        if len(nums) == 1:
            return nums[0]
        elif nums[:1] == nums[1:2]:
            return self.singleNumber_recursive(nums[2:])
        else:
            return self.singleNumber_recursive(nums[:1])

                
    def singleNumber_with_memory(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Runtime: 80 ms, faster than 38.09% of Python online submissions for Single Number.
        Memory Usage: 16.1 MB, less than 5.40% of Python online submissions for Single Number.

        Runtime: 92 ms, faster than 30.25% of Python online submissions for Single Number.
        Memory Usage: 15.9 MB, less than 5.40% of Python online submissions for Single Number.

        Runtime: 72 ms, faster than 68.31% of Python online submissions for Single Number.
        Memory Usage: 15.9 MB, less than 5.40% of Python online submissions for Single Number.
        """
        d = {} 
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for k, v in d.items():
            if v == 1:
                return k
        


if __name__ == "__main__":
    input1 = [2, 2, 1]
    input2 = [4, 1, 2, 1, 2]
    s = Solution()
    a = s.singleNumber(input1)
    b = s.singleNumber(input2)
    print(a, b)
    pass
