"""
=====================================================================================
1431. Kids With the Greatest Number of Candies
kidsWithCandies()
<https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/>
=====================================================================================

Given the array candies and the integer extraCandies, 
where candies[i] represents the number of candies that the ith kid has.
For each kid check if there is a way to distribute extraCandies among the kids 
such that he or she can have the greatest number of candies among them. 
Notice that multiple kids can have the greatest number of candies.

Example 1:
----------
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: 
Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies --- the greatest number of candies among the kids. 
Kid 2 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 
Kid 3 has 5 candies and this is already the greatest number of candies among the kids. 
Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies. 
Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 

Example 2:
----------
Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false] 
Explanation: There is only 1 extra candy, therefore only kid 1 will have the greatest number of candies among the kids regardless of who takes the extra candy.

Example 3:
----------
Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]
 
Constraints:
------------
2 <= candies.length <= 100
1 <= candies[i] <= 100
1 <= extraCandies <= 50
"""


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]

        Runtime: 16 ms, faster than 98.84% of Python online submissions for Kids With the Greatest Number of Candies.
        Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for Kids With the Greatest Number of Candies.
        """

        x = max(candies)
    
        return [True if i + extraCandies >= x else False for i in candies]

if __name__ == "__main__":
    candies1, extraCandies1, out1 = [2, 3, 5, 1, 3], 3, [True,True,True,False,True] 
    candies2, extraCandies2, out2 = [4, 2, 1, 1, 2], 1, [True,False,False,False,False] 
    candies3, extraCandies3, out3 = [12, 1, 12], 10, [True, False, True]

    s = Solution()
    a = s.kidsWithCandies(candies1, extraCandies1)
    b = s.kidsWithCandies(candies2, extraCandies2)
    c = s.kidsWithCandies(candies3, extraCandies3)

    print (a, b, c)
    pass
