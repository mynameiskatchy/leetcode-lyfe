"""
====================================================================================================
38. Count and Say
countAndSay()
<https://leetcode.com/problems/count-and-say/>
<https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/886/>
====================================================================================================

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. 
You can do so recursively, in other words from the previous member read off the digits, 
counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:
----------
Input: 1
Output: "1"
Explanation: This is the base case.

Example 2:
----------
Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" 
in which we have two groups "2" and "1", "2" can be read as "12" 
which means frequency = 1 and value = 2, the same way "1" is read as "11", 
so the answer is the concatenation of "12" and "11" which is "1211".

HINT#1
------
The following are the terms from n=1 to n=10 of the count-and-say sequence:
 1.     1
 2.     11
 3.     21
 4.     1211
 5.     111221 
 6.     312211
 7.     13112221
 8.     1113213211
 9.     31131211131221
10.     13211311123113112211

HINT#2
------
To generate the nth term, just count and say the n-1th term.
"""


class Solution(object):

    def countAndSay(self, prev):
        next = ''

        counter = 1
        i = 0
        if len(prev) == 1:
            return '1' + prev[0]
        while i < len(prev)-1:
            if prev[i] == prev[i + 1]:
                counter += 1
                i += 1
            else:
                next += str(counter) + prev[i]
                counter = 1
                i += 1

        return next

    def countAndSay_(self, n):
        base = '1'
        for i in range(n):
            return s[-1]
            
        
if __name__ == "__main__":
    input1 = 1
    output = "1"

    input2 = 4
    output = "1211"

    s = Solution()

    # a = '1'
    # b = '11'
    # c = '21'
    # d = '1211'
    # e = '111221'
    # f = '312211'
    # g = '13112221'
    # h = '1113213211'
    # i = '31131211131221'
    # j = '13211311123113112211'

    a = s.countAndSay('1')
    b = s.countAndSay('11')
    c = s.countAndSay('21')
    d = s.countAndSay('1211')
    e = s.countAndSay('111221')
    f = s.countAndSay('312211')
    g = s.countAndSay('13112221')
    h = s.countAndSay('1113213211')
    i = s.countAndSay('31131211131221')
    j = s.countAndSay('13211311123113112211')



    print(a, b)
    pass
