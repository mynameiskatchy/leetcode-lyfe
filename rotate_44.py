
""" Gucci for most part. Could improve without reverse maybe
====================================================================================================
48. Rotate Image
rotate()
<https://leetcode.com/problems/rotate-image/>
<https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/>
====================================================================================================

You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
----------
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:
----------
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.

        Runtime: 20 ms, faster than 87.10% of Python online submissions for Rotate Image.
        Memory Usage: 12.8 MB, less than 5.41% of Python online submissions for Rotate Image.
        
        Runtime: 24 ms, faster than 63.75% of Python online submissions for Rotate Image.
        Memory Usage: 12.9 MB, less than 5.41% of Python online submissions for Rotate Image.
        """
        # Transpose regularly
        for i in range(len(matrix)):
          for j in range(len(matrix[0])):
            if i < j:
              matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
          matrix[i] = matrix[i][::-1]
        # # Reverse columns
        # for i in range(len(matrix)):
        #   matrix[i].reverse()

        return matrix

    
if __name__ == "__main__":
  # example1
  input1 = \
    [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]
  output1 = \
    [
      [7, 4, 1],
      [8, 5, 2],
      [9, 6, 3]
    ]
  # example2
  input2 = \
    [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
        ]

  output2 = \
    [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11]
        ]

  s = Solution()
  a = s.rotate(input1)
  b = s.rotate(input2)
  print(a, b)
  pass
