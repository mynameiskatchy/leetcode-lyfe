"""
====================================================================================
1436. Destination City
destCity()
<https://leetcode.com/problems/destination-city/>
====================================================================================

You are given the array paths, where paths[i] = [cityA_i, cityB_i] 
means there exists a direct path going from cityA_i to cityB_i. 
Return the destination city, that is, 
the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, 
therefore, there will be exactly one destination city.

Example 1:
----------
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. 
Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Example 2:
----------
Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".

Example 3:
----------
Input: paths = [["A","Z"]]
Output: "Z"
 
Constraints:
-----------
1 <= paths.length <= 100
paths[i].length == 2
1 <= cityAi.length, cityBi.length <= 10
cityAi != cityBi
All strings consist of lowercase and uppercase English letters and the space character.

"""


class Solution(object):

    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str

        Runtime: 32 ms, faster than 98.35% of Python online submissions for Destination City.
        Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for Destination City.
        """

        start, end = zip(*paths)
        return (set(end) - set(start)).pop()

    def destCity_2(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str

        Runtime: 44 ms, faster than 65.57% of Python online submissions for Destination City.
        Memory Usage: 12.9 MB, less than 100.00% of Python online submissions for Destination City.
        
        Runtime: 36 ms, faster than 91.39% of Python online submissions for Destination City.
        Memory Usage: 12.8 MB, less than 100.00% of Python online submissions for Destination City.
        """
        d = dict()

        for p in paths:
            d[p[0]] = p[1]

        j = [dest for dest in d.values() if dest not in d.keys()][0]
        return j

        
if __name__ == "__main__":

    paths1 = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
    dest1 = "Sao Paulo"
    paths2 = [["B", "C"], ["D", "B"], ["C", "A"]]
    dest2 = "A"
    paths3 = [["A", "Z"]]
    dest3 =  "Z"

    s = Solution()
    a = s.destCity(paths1)
    b = s.destCity(paths2)
    c = s.destCity(paths3)

    print(a, b, c)

    pass
