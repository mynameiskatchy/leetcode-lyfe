
"""
====================================================================================================
344. Reverse String
reverseString()
<https://leetcode.com/problems/reverse-string/>
<https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/>
====================================================================================================

Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

Example 1:
----------
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
----------
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Hint #1  
The entire logic for reversing a string is based on using the opposite directional two-pointer approach!
"""

class Solution(object):
    def reverseString_troll(self, s):
        """
        Runtime: 164 ms, faster than 96.23% of Python online submissions for Reverse String.
        Memory Usage: 19.6 MB, less than 60.79% of Python online submissions for Reverse String.
        """
        s.reverse()
        return s

    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        Runtime: 172 ms, faster than 78.84% of Python online submissions for Reverse String.
        Memory Usage: 19.8 MB, less than 22.61% of Python online submissions for Reverse String.

        Runtime: 176 ms, faster than 62.19% of Python online submissions for Reverse String.
        Memory Usage: 19.8 MB, less than 26.84% of Python online submissions for Reverse String.

        Runtime: 168 ms, faster than 90.10% of Python online submissions for Reverse String.
        Memory Usage: 19.8 MB, less than 37.09% of Python online submissions for Reverse String.

        Runtime: 180 ms, faster than 43.81% of Python online submissions for Reverse String.
        Memory Usage: 19.6 MB, less than 59.24% of Python online submissions for Reverse String.

        Runtime: 192 ms, faster than 16.41% of Python online submissions for Reverse String.
        Memory Usage: 19.8 MB, less than 29.66% of Python online submissions for Reverse String

        Runtime: 220 ms, faster than 9.73% of Python online submissions for Reverse String.
        Memory Usage: 19.8 MB, less than 34.86% of Python online submissions for Reverse String.

        Runtime: 224 ms, faster than 9.29% of Python online submissions for Reverse String.
        Memory Usage: 19.8 MB, less than 35.92% of Python online submissions for Reverse String.
        """

        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]
        return s

    def reverseString1(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.

        Runtime: 172 ms, faster than 78.84% of Python online submissions for Reverse String.
        Memory Usage: 19.9 MB, less than 17.62% of Python online submissions for Reverse String.
        
        Runtime: 256 ms, faster than 6.68% of Python online submissions for Reverse String.
        Memory Usage: 19.8 MB, less than 21.94% of Python online submissions for Reverse String.

        Runtime: 260 ms, faster than 6.24% of Python online submissions for Reverse String.
        Memory Usage: 19.8 MB, less than 24.43% of Python online submissions for Reverse String

        Runtime: 204 ms, faster than 11.66% of Python online submissions for Reverse String.
        Memory Usage: 19.8 MB, less than 26.84% of Python online submissions for Reverse String.
        """
        pointer1 = 0
        pointer2 = len(s) - 1
        for _ in range(len(s)//2):
            s[pointer1], s[pointer2] = s[pointer2], s[pointer1]
            pointer1 += 1
            pointer2 -= 1
        return s

if __name__ == "__main__":
    input1 = ["h", "e", "l", "l", "o"]
    output1 = ["o", "l", "l", "e", "h"]

    input2 = ["H", "a", "n", "n", "a", "h"]
    output2 = ["h", "a", "n", "n", "a", "H"]

    s = Solution()
    a = s.reverseString(input1)
    b = s.reverseString(input2)

    print(a,b)

    input2.reverse()
    pass
