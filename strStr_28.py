"""
====================================================================================================
28. Implement strStr()
strStr()
<https://leetcode.com/problems/implement-strstr/>
<https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/>
====================================================================================================

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
----------
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
----------
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
--------------
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int

        Runtime: 20 ms, faster than 68.18% of Python online submissions for Implement strStr().
        Memory Usage: 13 MB, less than 70.27% of Python online submissions for Implement strStr().

        Runtime: 12 ms, faster than 97.37% of Python online submissions for Implement strStr().
        Memory Usage: 13 MB, less than 64.21% of Python online submissions for Implement strStr().

        Runtime: 16 ms, faster than 85.61% of Python online submissions for Implement strStr().
        Memory Usage: 13.1 MB, less than 48.89% of Python online submissions for Implement strStr().

        Runtime: 24 ms, faster than 45.20% of Python online submissions for Implement strStr().
        Memory Usage: 13 MB, less than 79.71% of Python online submissions for Implement strStr().
        """
        if needle == "" or needle == haystack:
            return 0

        for i in range(len(haystack) - len(needle)+1):
            if haystack[i] == needle[0] and haystack[i:i + len(needle)] == needle[:]:
                return i
        return -1

if __name__ == "__main__":
    haystack1 = "hello"
    needle1 = "ll"
    haystack2 = "aaaaa"
    needle2 = "bba"
    haystack3 = "a"
    needle3 = "a"
    haystack4 = "mississippi"
    needle4 = "pi"

    s = Solution()

    a = s.strStr(haystack1, needle1)
    b = s.strStr(haystack2, needle2)
    c = s.strStr(haystack3, needle3)
    d = s.strStr(haystack4, needle4)

    print(a, b, c, d)
    pass
