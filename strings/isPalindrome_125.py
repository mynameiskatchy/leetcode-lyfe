"""
====================================================================================================
125. Valid Palindrome
isPalindrome()
<https://leetcode.com/problems/valid-palindrome/>
<https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/>
====================================================================================================

Given a string, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
----------
Input: "A man, a plan, a canal: Panama"
Output: true

amanaplanacanalpanama


Example 2:
----------
Input: "race a car"
Output: false
"""

class Solution(object):

    def isPalindrome_attempt1(self, s):
        """ This method uses 2 pointers
        :type s: str
        :rtype: bool

        Runtime: 52 ms, faster than 39.70% of Python online submissions for Valid Palindrome.
        Memory Usage: 13.6 MB, less than 68.68% of Python online submissions for Valid Palindrome.
        
        Runtime: 56 ms, faster than 35.69% of Python online submissions for Valid Palindrome.
        Memory Usage: 13.5 MB, less than 84.11% of Python online submissions for Valid Palindrome.
        
        Runtime: 44 ms, faster than 57.93% of Python online submissions for Valid Palindrome.
        Memory Usage: 13.5 MB, less than 85.16% of Python online submissions for Valid Palindrome.
        
        Runtime: 28 ms, faster than 95.85% of Python online submissions for Valid Palindrome.
        Memory Usage: 13.6 MB, less than 70.64% of Python online submissions for Valid Palindrome.
        
        Runtime: 40 ms, faster than 70.86% of Python online submissions for Valid Palindrome.
        Memory Usage: 13.7 MB, less than 55.41% of Python online submissions for Valid Palindrome.
        """
        i = 0
        j = len(s) - 1
        while (i <= j):
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False
            elif not s[j].isalnum():
                j -= 1
            elif not s[i].isalnum():
                i += 1
            else:
                i += 1
                j -= 1

        return True

    
    def isPalindrome(self, s):
        """
        Filter and cover to lowercase, then check cheatway

        Runtime: 64 ms, faster than 29.74% of Python online submissions for Valid Palindrome.
        Memory Usage: 15.2 MB, less than 12.42% of Python online submissions for Valid Palindrome.
        
        Runtime: 36 ms, faster than 82.77% of Python online submissions for Valid Palindrome.
        Memory Usage: 15.3 MB, less than 10.65% of Python online submissions for Valid Palindrome.
        
        Runtime: 44 ms, faster than 57.93% of Python online submissions for Valid Palindrome.
        Memory Usage: 15.1 MB, less than 14.61% of Python online submissions for Valid Palindrome.
        
        Runtime: 40 ms, faster than 70.86% of Python online submissions for Valid Palindrome.
        Memory Usage: 15.1 MB, less than 13.50% of Python online submissions for Valid Palindrome.
        
        Runtime: 28 ms, faster than 95.85% of Python online submissions for Valid Palindrome.
        Memory Usage: 15.1 MB, less than 13.60% of Python online submissions for Valid Palindrome.
        
        Runtime: 40 ms, faster than 70.86% of Python online submissions for Valid Palindrome.
        Memory Usage: 15.3 MB, less than 10.97% of Python online submissions for Valid Palindrome.
        """
        s = [x.lower() for x in s if x.isalnum()]
        return s == s[::-1]

    def isPalindrome_leetcode(self, s):
        # There's also a regex way
        pass

if __name__ == "__main__":
    # example 1
    input1 = "A man, a plan, a canal: Panama"
    output1 = True
    # example 2
    input2 = "race a car"
    output2 = False

    s = Solution()

    a = s.isPalindrome(input1)
    b = s.isPalindrome(input2)
    
    print(a, b)

    pass
