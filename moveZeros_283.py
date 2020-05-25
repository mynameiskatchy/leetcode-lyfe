
"""
====================================================================================================
283. Move Zeroes
moveZeroes()
<https://leetcode.com/problems/move-zeroes/>
<https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/>
====================================================================================================

Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Example:
--------
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""


class Solution(object):

    def moveZeroes(self, nums):
        """
        Runtime: 28 ms, faster than 98.76% of Python online submissions for Move Zeroes.
        Memory Usage: 13.6 MB, less than 5.06% of Python online submissions for Move Zeroes.

        Runtime: 24 ms, faster than 99.83% of Python online submissions for Move Zeroes.
        Memory Usage: 13.7 MB, less than 5.06% of Python online submissions for Move Zeroes.

        move zero pointer whenever we encounter a non-zero. 
        will give us potential position to swap to
        """
        # zero = 0
        # i = 0
        # while i < len(nums):
        #     if nums[i] != 0:
        #         nums[zero], nums[i] = nums[i], nums[zero]
        #         zero+=1
        #     i+=1
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero+=1
        return nums

    def moveZeroes_3(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        Runtime: 60 ms, faster than 31.69% of Python online submissions for Move Zeroes.
        Memory Usage: 13.7 MB, less than 5.06% of Python online submissions for Move Zeroes.
        """
        zeros = 0
        for i in nums:
            if i == 0:
                zeros += 1
                
        for i in range(zeros):
            n = nums.index(0)
            nums.append(0)
            nums.pop(n)
        
        return nums

    def moveZeroes_2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        Runtime: 536 ms, faster than 6.96% of Python online submissions for Move Zeroes.
        Memory Usage: 13.6 MB, less than 5.06% of Python online submissions for Move Zeroes.
      
        # Dont like how slow this is
        """
        
        for i in range(len(nums)-1):
            if nums[i] == 0 and nums[i+1] != 0:
                nums[i] = nums[i+1]
                nums[i+1] = 0
            elif nums[i] == 0 and nums[i+1] == 0:
                curr = i
                while(i < len(nums)-1):
                    if nums[i+1] != 0:
                        nums[curr] = nums[i+1]
                        nums[i+1] = 0
                        break
                    else:
                        i += 1
        return nums

    def moveZeroes_1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        Runtime: 40 ms, faster than 57.46% of Python online submissions for Move Zeroes.
        Memory Usage: 13.7 MB, less than 5.06% of Python online submissions for Move Zeroes.

        Runtime: 32 ms, faster than 93.75% of Python online submissions for Move Zeroes.
        Memory Usage: 13.8 MB, less than 5.06% of Python online submissions for Move Zeroes.
        
        Runtime: 28 ms, faster than 98.76% of Python online submissions for Move Zeroes.
        Memory Usage: 13.7 MB, less than 5.06% of Python online submissions for Move Zeroes.
        
        # Dont like this one cuz uses pop
        """
        i = 0
        counter = 0
        while (counter < len(nums)-1):
            if nums[i] == 0:
                nums.append(nums[i])
                nums.pop(i)
            else:
                i += 1
            counter += 1

    def moveZeroes_Nope(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)  # does not work cuz numbers have to stay in place
        return nums
                                                                                                                                                                                                          
    
if __name__ == "__main__":
    input1 = [0, 1, 0, 3, 12]
    output1 = [1, 3, 12, 0, 0]

    input2 = [0, 0, 1]
    output2 = [1, 0, 0]

    input3 = [0, 0, 0, 0, 0]

    input4 = [1, 0, 0, 2, 9, 0]

    input5 = [1, 2, 3, 4, 5]

    s = Solution()
    a = s.moveZeroes(input1)
    b = s.moveZeroes(input2)
    c = s.moveZeroes(input3)
    d = s.moveZeroes(input4)
    e = s.moveZeroes(input5)
    print(a, b, c, d, e) 
    pass
