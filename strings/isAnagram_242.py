"""
====================================================================================================
242. Valid Anagram
isAnagram()
<https://leetcode.com/problems/valid-anagram/>
<https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/>
====================================================================================================

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
----------
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
----------
Input: s = "rat", t = "car"
Output: false

Note:
-----
You may assume the string contains only lowercase alphabets.

Follow up:
----------
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution(object):
    # Other Leetcode solns
    def isAnagram_leetcode1(self, s, t):
        """
        actually not much faster than the others
        """
        # from collections
        # return Counter(s) == Counter(t)
        return 0
    
    def isAnagram_leetcode2(self, s, t):
        """
        Runtime: 16 ms, faster than 99.81% of Python online submissions for Valid Anagram.
        Memory Usage: 13.6 MB, less than 52.51% of Python online submissions for Valid Anagram.
       
        Runtime: 20 ms, faster than 99.38% of Python online submissions for Valid Anagram.
        Memory Usage: 13.6 MB, less than 59.78% of Python online submissions for Valid Anagram.
        """
        if len(s) != len(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True
    
    def isAnagram(self, s, t):
        """
        interesting
        """
        # return all([s.count(c) == t.count(c) for c in string.ascii_lowercase])
        return 0

    def isAnagram_attempt1(self, s, t):
        """ Very slow cuz of sort. O(2logn) + O(n)
        :type s: str
        :type t: str
        :rtype: bool

        Runtime: 100 ms, faster than 7.01% of Python online submissions for Valid Anagram.
        Memory Usage: 16 MB, less than 5.12% of Python online submissions for Valid Anagram.
        
        Runtime: 88 ms, faster than 8.99% of Python online submissions for Valid Anagram.
        Memory Usage: 16.1 MB, less than 5.12% of Python online submissions for Valid Anagram.

        Runtime: 76 ms, faster than 12.72% of Python online submissions for Valid Anagram.
        Memory Usage: 16 MB, less than 5.12% of Python online submissions for Valid Anagram.
        
        Runtime: 72 ms, faster than 14.64% of Python online submissions for Valid Anagram.
        Memory Usage: 16.1 MB, less than 5.12% of Python online submissions for Valid Anagram.

        Runtime: 60 ms, faster than 25.97% of Python online submissions for Valid Anagram.
        Memory Usage: 16.3 MB, less than 5.12% of Python online submissions for Valid Anagram.
        """
        s = sorted(s)
        t = sorted(t)
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] != t[i]:
                return False

        return True

    def isAnagram_attempt2(self, s, t):
        """ Kind of slow O(2n) from counting and comparing dictionaries
        :type s: str
        :type t: str
        :rtype: bool

        Runtime: 68 ms, faster than 16.75% of Python online submissions for Valid Anagram.
        Memory Usage: 15.3 MB, less than 7.57% of Python online submissions for Valid Anagram.

        Runtime: 60 ms, faster than 25.97% of Python online submissions for Valid Anagram.
        Memory Usage: 15.4 MB, less than 5.12% of Python online submissions for Valid Anagram.
       
        Runtime: 44 ms, faster than 66.24% of Python online submissions for Valid Anagram.
        Memory Usage: 15.3 MB, less than 9.43% of Python online submissions for Valid Anagram.
        
        Runtime: 48 ms, faster than 53.68% of Python online submissions for Valid Anagram.
        Memory Usage: 15.3 MB, less than 8.76% of Python online submissions for Valid Anagram.
        
        Runtime: 36 ms, faster than 86.40% of Python online submissions for Valid Anagram.
        Memory Usage: 15.3 MB, less than 5.94% of Python online submissions for Valid Anagram.
        
        Runtime: 28 ms, faster than 96.33% of Python online submissions for Valid Anagram.
        Memory Usage: 15.3 MB, less than 9.32% of Python online submissions for Valid Anagram.
        """
        sdict = {}
        tdict = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            # count letters in s
            if s[i] not in sdict:
                sdict[s[i]] = 1
            else:
                sdict[s[i]] += 1
            # count letters in t
            if t[i] not in tdict:
                tdict[t[i]] = 1
            else:
                tdict[t[i]] += 1
        
        return False if sdict != tdict else True

    def isAnagram_attempt3(self, s, t):
        """ Kind of slow O(2n) from counting and comparing dictionaries
        :type s: str
        :type t: str
        :rtype: bool

        Runtime: 68 ms, faster than 16.75% of Python online submissions for Valid Anagram.
        Memory Usage: 15.5 MB, less than 5.12% of Python online submissions for Valid Anagram.

        Runtime: 48 ms, faster than 53.68% of Python online submissions for Valid Anagram.
        Memory Usage: 15.3 MB, less than 7.16% of Python online submissions for Valid Anagram
        
        Runtime: 40 ms, faster than 76.86% of Python online submissions for Valid Anagram.
        Memory Usage: 15.3 MB, less than 7.87% of Python online submissions for Valid Anagram.
        
        Runtime: 72 ms, faster than 14.64% of Python online submissions for Valid Anagram.
        Memory Usage: 15.3 MB, less than 7.83% of Python online submissions for Valid Anagram.
        
        Runtime: 92 ms, faster than 8.31% of Python online submissions for Valid Anagram.
        Memory Usage: 15.5 MB, less than 5.12% of Python online submissions for Valid Anagram.
        """
        sdict = {}
        tdict = {}

        if len(s) != len(t) or set(s) != set(t):
            return False
        
        for i in range(len(s)):
            # count letters in s
            if s[i] not in sdict:
                sdict[s[i]] = 1
            else:
                sdict[s[i]] += 1
            # count letters in t
            if t[i] not in tdict:
                tdict[t[i]] = 1
            else:
                tdict[t[i]] += 1
        
        return False if sdict != tdict else True
        
if __name__ == "__main__":
    # Example 1:
    s1 = "anagram"
    t1 = "nagaram"
    output1 = True
    # Example 2:
    s2 = "rat"
    t2 = "car"
    output2 = False
    # Example 3:
    s3 = "ab"
    t3 = "a"
    output3 = False


    s = Solution()
    a = s.isAnagram(s1, t1)
    b = s.isAnagram(s2, t2)
    c = s.isAnagram(s3, t3)

    print(a, b, c)  

    pass
