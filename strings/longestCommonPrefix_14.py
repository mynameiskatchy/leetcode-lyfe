""" This one was kinda of hard for me
====================================================================================================
14. Longest Common Prefix
longestCommonPrefix()
<https://leetcode.com/problems/longest-common-prefix/>
<https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/>
====================================================================================================

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
---------
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
----------
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
-----
All given inputs are in lowercase letters a-z.
"""


class Solution(object):
    def longestCommonPrefix_nope(self, strs):
        """
        :type strs: List[str]
        :rtype: str


        95 / 118 test cases passed. missed ["a","a","b"] => ""
        105 / 118 test cases passed. missed ["caa","","a","acb"] => ""
        """
        if len(strs) == 1:
            return [strs[0]]

        common = ""

        for i in range(len(strs) - 1):
            curr = strs[i]
            next = strs[i + 1]
            j = 0
            temp = ""
            
            while (j < min(len(curr), len(next))):
                if curr[j] == next[j]:
                    temp += curr[j]
                    j += 1
                else:
                    break
            
                common = temp
        
        return [common]

    def longestCommonPrefix_1(self, strs):
        """
        :type strs: List[str]
        :rtype: str

        112 / 118 test cases passed. ["abab","aba",""] => ""
        Runtime: 16 ms, faster than 95.18% of Python online submissions for Longest Common Prefix.
        Memory Usage: 12.8 MB, less than 59.55% of Python online submissions for Longest Common Prefix.
        
        Runtime: 24 ms, faster than 59.53% of Python online submissions for Longest Common Prefix.
        Memory Usage: 12.7 MB, less than 84.26% of Python online submissions for Longest Common Prefix.
        
        Runtime: 48 ms, faster than 5.95% of Python online submissions for Longest Common Prefix.
        Memory Usage: 12.7 MB, less than 92.89% of Python online submissions for Longest Common Prefix.
        
        Runtime: 12 ms, faster than 99.14% of Python online submissions for Longest Common Prefix.
        Memory Usage: 12.8 MB, less than 46.86% of Python online submissions for Longest Common Prefix.
        """
        curr = strs[0] if len(strs) > 0 else ""
        
        for next in strs:
            j = 0
            if next == curr:
                continue
            elif next == "" or curr == "":
                return ""
            elif curr[j] == next[j]:
                temp = ""
                while (j < min(len(curr), len(next))):
                    if curr[j] == next[j]:
                        temp += curr[j]
                        j += 1
                    else:
                        curr = temp
                        break
                curr = temp
            else:
                curr = ""
        
        return curr

    def longestCommonPrefix2(self, strs):
        """ Code is short
        Runtime: 32 ms, faster than 19.75% of Python online submissions for Longest Common Prefix.
        Memory Usage: 13.1 MB, less than 5.14% of Python online submissions for Longest Common Prefix.
        
        Runtime: 16 ms, faster than 95.18% of Python online submissions for Longest Common Prefix.
        Memory Usage: 12.8 MB, less than 53.81% of Python online submissions for Longest Common Prefix.
        
        Runtime: 52 ms, faster than 5.95% of Python online submissions for Longest Common Prefix.
        Memory Usage: 12.8 MB, less than 52.28% of Python online submissions for Longest Common Prefix.
        
        Runtime: 24 ms, faster than 59.53% of Python online submissions for Longest Common Prefix.
        Memory Usage: 12.8 MB, less than 66.28% of Python online submissions for Longest Common Prefix.
        
        Runtime: 28 ms, faster than 33.03% of Python online submissions for Longest Common Prefix.
        Memory Usage: 12.8 MB, less than 43.50% of Python online submissions for Longest Common Prefix.
        
        Runtime: 20 ms, faster than 82.61% of Python online submissions for Longest Common Prefix.
        Memory Usage: 12.8 MB, less than 59.55% of Python online submissions for Longest Common Prefix.
       
        Runtime: 12 ms, faster than 99.14% of Python online submissions for Longest Common Prefix.
        Memory Usage: 12.8 MB, less than 43.50% of Python online submissions for Longest Common Prefix.
        
        Runtime: 32 ms, faster than 19.75% of Python online submissions for Longest Common Prefix.
        Memory Usage: 13.1 MB, less than 5.14% of Python online submissions for Longest Common Prefix.
        """
        s = zip(*strs)
        common = ""
        for i in s:
            if len(set(i)) > 1:
                break
            common += i[0]
        
        return common

    def longestCommonPrefix(self, strs):
        """
        Runtime: 16 ms, faster than 95.18% of Python online submissions for Longest Common Prefix.
        Memory Usage: 12.9 MB, less than 27.60% of Python online submissions for Longest Common Prefix.     
        
        Runtime: 20 ms, faster than 82.61% of Python online submissions for Longest Common Prefix.
        Memory Usage: 12.9 MB, less than 26.43% of Python online submissions for Longest Common Prefix.
        
        Runtime: 28 ms, faster than 33.03% of Python online submissions for Longest Common Prefix.
        Memory Usage: 12.8 MB, less than 76.49% of Python online submissions for Longest Common Prefix.
        
        Runtime: 32 ms, faster than 19.75% of Python online submissions for Longest Common Prefix.
        Memory Usage: 12.8 MB, less than 59.55% of Python online submissions for Longest Common Prefix.
        
        Runtime: 36 ms, faster than 12.47% of Python online submissions for Longest Common Prefix.
        Memory Usage: 13 MB, less than 8.09% of Python online submissions for Longest Common Prefix.
        """
        if not strs:
            return ''
        strs.sort()
        fst = strs[0]
        lst = strs[-1]
        l = min(len(fst), len(lst))
        i = 0
        while i < l and fst[i] == lst[i]:
            i += 1
        return fst[:i]

    def longestCommonPrefix_lc3(self, strs):
        """
        Runtime: 32 ms, faster than 19.75% of Python online submissions for Longest Common Prefix.
        Memory Usage: 12.9 MB, less than 30.65% of Python online submissions for Longest Common Prefix.
        
        Explanation: No sorting (which adds additional O(nlogn) complexity) needed. 
        The letters of the first word in the strs list will be used to compare against 
        the letters of all of the other strings in the list. 
        There are two main comparison cases while iterating over the letters of the 
        first word: 
        1) The current index of the first word is larger then current index 
        of the word being compared against. 
        2) The current first word letter does not 
        match the letter in the word being compared against. 
        In both cases, just return the substring of the first word up until this index. 
        If you make it though the entire first word, then the entire first word is the 
        common prefix
        """
        if not strs:
            return ''
        first_word = strs[0]
        for i in range(len(first_word)):
            for j in range(1, len(strs)):
                if i >= len(strs[j]):  # first_word larger than current_word
                    return first_word[:i]
                if strs[j][i] != first_word[i]:  # letters don't equal
                    return first_word[:i]

        return first_word  # made it to the end of the first word so this the common prefix

    def longestCommonPrefix_lc(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 1: return ""
        min_word, max_word = strs[0], strs[0]
        for w in strs:
            if min_word > w: min_word = w
            if max_word < w: max_word = w
        # find common prefix between min_word and max_word
        iterations = min(len(min_word), len(max_word))
        result = 0
        for i in range(iterations):
            if min_word[i] == max_word[i]:
                result += 1
            else: return min_word[:result]
        return min_word[:result]

if __name__ == "__main__":
    input1 = ["flower", "flow", "flight"]
    output1 = "fl"
    input2 = ["dog", "racecar", "car"]
    output2 = ""
    input3 = ["a"]
    output3 = "a"
    input4 = ["a", "a", "b"]
    output4 = ""
    input5 = ["caa", "", "a", "acb"]
    output5 = ""
    input6 = []
    output6 = ""
    input7 = ["abab", "aba", ""]
    output = ""

    s = Solution()

    a = s.longestCommonPrefix(input1)
    b = s.longestCommonPrefix(input2)
    c = s.longestCommonPrefix(input3)
    d = s.longestCommonPrefix(input4)
    e = s.longestCommonPrefix(input5)
    f = s.longestCommonPrefix(input6)
    g = s.longestCommonPrefix(input7)

    print([a, b, c, d, e, f, g])


    pass
