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
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.

        Use an array and copy...
        Complexity Analysis
            - Time complexity: \mathcal{O}(n)O(n). 
            One pass is used to put the numbers in the new array. 
            And another pass to copy the new array to the original one.
            - Space complexity: \mathcal{O}(n)O(n). 
            Another array of the same size is used.
        """
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]

        nums[:] = a
        
        return nums

    def rotate_meh(self, nums, k):
        """
        I think you have to rotate one spot at a time, else
        you end up mutating too many numbers at once, with no way to store

        Does not work for even cases.
        9 / 35 test cases passed.
        """
        length = len(nums)
        counter = 0
        i = 0
        first = nums[0]
        while(counter < length+3):
            j = (i+k) % length
            next = nums[j]
            nums[j] = first
            first = next
            i = j
            counter += 1

        return nums

    def rotate_toolong(self, nums, k):
        """
        I think you have to rotate one spot at a time, else 
        you end up mutating too many numbers at once, with no way to store

        Time limit exceeded. 34/35 test cases

        Complexity Analysis
            Time complexity: \mathcal{O}(n \times k)O(n×k). 
            All the numbers are shifted by one step(\mathcal{O}(n)O(n)) k times(\mathcal{O}(n)O(n)).
            Space complexity: \mathcal{O}(1)O(1). No extra space is used.
        """
        
        length = len(nums)
        for k in range(k):
            first = nums[0]
            for i in range(length):
                j = (i+1)%length
                next = nums[j]
                nums[j] = first
                first = next
        
        return nums


    def rotate_2(self, nums, k):
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
    nums1, k1= [0, 1, 2, 3, 4, 5], 3
    output1 = [5, 6, 7, 1, 2, 3, 4]
    nums2, k2 = [-1, -100, 3, 99], 3
    nums3, k3 = [-1], 5
    nums4, k4 = [0, 1, 2, 3], 2
    output2 = [3, 99, -1, -100]

    s = Solution()
    a = s.rotate(nums1, k1)
    b = s.rotate(nums2, k2)
    c = s.rotate(nums3, k3)
    d = s.rotate(nums4, k4)
    print(a, b, c, d)

    pass


"""
class Solution:
    def rotate_CyclicReplacements(self, nums: List[int], k: int) -> None:
        """
        # O(n) time and O(1) space
        """
        n = len(nums)
        k %= n
        
        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                
                if start == current:
                    break
            start += 1

class Solution:
    # O(n) time and O(1) space
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
                
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

"""
