"""
====================================================================================================
387. First Unique Character in a String
firstUniqChar()
<https://leetcode.com/problems/first-unique-character-in-a-string/>
<https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/>
====================================================================================================

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:
---------
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.

"""


class Solution(object):
    def firstUniqChar_attempt1(self, s):
        """
        :type s: str
        :rtype: int

        76 / 104 test cases passed. Didnt take into account "cc"
        """

        temp = -1
        d = {}
        for i, val in enumerate(s[::-1]):
            if val not in d:
                d[val] = 1
                temp = i
            else:
                d[val] += 1
                temp = -1
        
        return temp if temp == -1 else len(s) - 1 - temp
    
    def firstUniqChar_1(self, s):
        """ Very slow cuz O(2n)
        Runtime: 156 ms, faster than 55.95% of Python online submissions for First Unique Character in a String.
        Memory Usage: 14 MB, less than 10.81% of Python online submissions for First Unique Character in a String.
        """
        d = {}
        for val in s:
            if val not in d:
                d[val] = 1
            else:
                d[val] += 1
        
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
            
        return - 1
    
    def firstUniqChar(self, s):
        """
        Runtime: 72 ms, faster than 94.67% of Python online submissions for First Unique Character in a String.
        Memory Usage: 13.8 MB, less than 38.87% of Python online submissions for First Unique Character in a String.

        Runtime: 52 ms, faster than 96.36% of Python online submissions for First Unique Character in a String.
        Memory Usage: 13.9 MB, less than 18.07% of Python online submissions for First Unique Character in a String.
        """
        visited = set()
        for i in range(len(s)):
            if s[i] not in visited:
                visited.add(s[i])
                if s.count(s[i]) == 1:
                    return i
        return -1





if __name__ == "__main__":
    s1 = "leetcode"
    out1 = 0
    s2 = "loveleetcode"
    out2 = 2
    s3 = "cc"
    out3 = -1

    s = Solution()
    a = s.firstUniqChar(s1)
    b = s.firstUniqChar(s2)
    c = s.firstUniqChar(s3)
    print(a, b, c)

    pass
