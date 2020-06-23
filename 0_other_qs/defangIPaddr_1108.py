"""
========================================================
1108. Defanging an IP Address
depandIPaddr()
<https://leetcode.com/problems/defanging-an-ip-address/>
========================================================

A defanged IP address replaces every period "." with "[.]".


Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"


Constraints:

The given address is a valid IPv4 address.
"""


class Solution(object):

    def defangIPaddr_listcomprehension(self, address):
        """
        :type address: str
        :rtype: str

        Runtime: 8 ms, faster than 98.48 % of Python online submissions for Defanging an IP Address.
        Memory Usage: 12.6 MB, less than 100.00 % of Python online submissions for Defanging an IP Address.
        """

        s = ['[{}]'.format('.') if c == '.' else c for c in address2]
        return ''.join(s)

    def defangIPaddr_recursion(self, address):
        
        return


if __name__ == "__main__":
    address1, output1 = "1.1.1.1", "1[.]1[.]1[.]1"
    address2, output2 = "255.100.50.0", "255[.]100[.]50[.]0"

    a = Solution(address1)
    b = Solution(address2)
    
    s = ['[{}]'.format('.') if c == '.' else c for c in address2]
    ''.join(s)

    Solution().defangIPaddr_listcomprehension(address1)
    Solution().defangIPaddr_listcomprehension(address2)
    pass
