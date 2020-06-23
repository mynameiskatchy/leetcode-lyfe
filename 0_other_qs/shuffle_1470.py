"""
==============================================================================
1470. Shuffle the Array
shuffle()
<https://leetcode.com/problems/shuffle-the-array>
==============================================================================

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].


Example 1:
==========
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

Example 2:
==========
Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]

Example 3:
==========
Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]
 
Constraints:
============
1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3
"""


class Solution:
    def shuffle_attempt1(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]

        Runtime: 44 ms, faster than 94.02% of Python online submissions for Shuffle the Array.
        Memory Usage: 12.8 MB, less than 100.00% of Python online submissions for Shuffle the Array.
        
        Runtime: 84 ms, faster than 17.83% of Python online submissions for Shuffle the Array.
        Memory Usage: 13 MB, less than 100.00% of Python online submissions for Shuffle the Array.
        
        Runtime: 60 ms, faster than 50.00% of Python online submissions for Shuffle the Array.
        Memory Usage: 13 MB, less than 100.00% of Python online submissions for Shuffle the Array.
        
        Runtime: 48 ms, faster than 83.30% of Python online submissions for Shuffle the Array.
        Memory Usage: 12.8 MB, less than 100.00% of Python online submissions for Shuffle the Array.
        """
        temp = []
        front = nums[:n]
        end = nums[n:]
        
        for i in range(n):
            temp.extend()
            
        return temp


    def shuffle_attempt2(self, nums, n):
        """
        Runtime: 52 ms, faster than 69.19% of Python online submissions for Shuffle the Array.
        Memory Usage: 13.1 MB, less than 100.00% of Python online submissions for Shuffle the Array.
        
        Runtime: 60 ms, faster than 50.00% of Python online submissions for Shuffle the Array.
        Memory Usage: 12.8 MB, less than 100.00% of Python online submissions for Shuffle the Array.
        
        Runtime: 76 ms, faster than 27.88% of Python online submissions for Shuffle the Array.
        Memory Usage: 13 MB, less than 100.00% of Python online submissions for Shuffle the Array.
        
        Runtime: 64 ms, faster than 44.47% of Python online submissions for Shuffle the Array.
        Memory Usage: 13.1 MB, less than 100.00% of Python online submissions for Shuffle the Array.
        
        Runtime: 56 ms, faster than 55.19% of Python online submissions for Shuffle the Array.
        Memory Usage: 12.9 MB, less than 100.00% of Python online submissions for Shuffle the Array.
        
        Runtime: 40 ms, faster than 98.08% of Python online submissions for Shuffle the Array.
        Memory Usage: 12.8 MB, less than 100.00% of Python online submissions for Shuffle the Array.
        """
        temp = []
        for i, j in zip(nums[:n], nums[n:]):
            temp.extend([i, j])
        return temp

    def shuffle(self, nums, n):
        """
        Runtime: 60 ms, faster than 50.00% of Python online submissions for Shuffle the Array.
        Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for Shuffle the Array.
        
        Runtime: 48 ms, faster than 83.30% of Python online submissions for Shuffle the Array.
        Memory Usage: 12.8 MB, less than 100.00% of Python online submissions for Shuffle the Array.
        
        Runtime: 72 ms, faster than 34.42% of Python online submissions for Shuffle the Array.
        Memory Usage: 12.9 MB, less than 100.00% of Python online submissions for Shuffle the Array.
        
        Runtime: 52 ms, faster than 69.19% of Python online submissions for Shuffle the Array.
        Memory Usage: 13 MB, less than 100.00% of Python online submissions for Shuffle the Array.
        
        Runtime: 52 ms, faster than 69.19% of Python online submissions for Shuffle the Array.
        Memory Usage: 13 MB, less than 100.00% of Python online submissions for Shuffle the Array.
        
        Runtime: 44 ms, faster than 94.02% of Python online submissions for Shuffle the Array.
        Memory Usage: 13 MB, less than 100.00% of Python online submissions for Shuffle the Array.
        """
        temp = []
        for i in range(n):
            temp.extend([nums[i], nums[i + n]])
        return temp

if __name__ == "__main__":
  # Test Cases
  # Example 1
  nums1 = [2, 5, 1, 3, 4, 7]
  n1 = 3
  output1 = [2, 3, 5, 4, 1, 7]
  # Example 2
  nums2 = [1, 2, 3, 4, 4, 3, 2, 1]
  n2 = 4
  output2 = [1, 4, 2, 3, 3, 2, 4, 1]
  # Example 3
  nums3 = [1, 1, 2, 2]
  n3 = 2
  output3 = [1, 2, 1, 2]

  s = Solution()
  a = s.shuffle(nums1, n1)
  b = s.shuffle(nums2, n2)
  c = s.shuffle(nums3, n3)

  print(a, b, c)
  pass
