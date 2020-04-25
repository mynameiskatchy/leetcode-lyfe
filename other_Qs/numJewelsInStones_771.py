"""
======================
771. Jewels and Stones
numJewelsInStones()
======================


You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int

        Runtime: 12 ms, faster than 96.07 % of Python online submissions for Jewels and Stones.
        Memory Usage: 12.9 MB, less than 5.38 % of Python online submissions for Jewels and Stones.

        """
        
        counter = 0
        for i in S:
            if i in J:
                counter += 1
        return counter



if __name__ == "__main__":
    J1, S1, ans1 = "aA", "aAAbbbb", 3
    J2, S2, ans2 = "z", "ZZ", 0

    s = Solution()
    out1 = s.numJewelsInStones(J1, S1)
    out2 = s.numJewelsInStones(J2, S2)

    print(out1)
    print(out2)

    pass
