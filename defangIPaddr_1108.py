"""
1108. Defanging an IP Address

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
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """

if __name__ == "__main__":
    address1 = "1.1.1.1"
    address2 = "255.100.50.0"

    a = Solution(address1)
    b = Solution(address2)
    
    a.defangIPaddr(a)

    s = ['[{}]'.format('.') if c == '.' else c for c in address2]
    ''.join(s)

    
    pass
