"""
====================================================================================================
141. Linked List Cycle
hasCycle()
<https://leetcode.com/problems/linked-list-cycle/>
<https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/>
====================================================================================================

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, 
we use an integer pos which represents the position (0-indexed) 
in the linked list where tail connects to. If pos is -1, 
then there is no cycle in the linked list.

Example 1
----------
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
----------
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
----------
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Follow up:
----------
Can you solve it using O(1) (i.e. constant) memory?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """



if __name__ == "__main__":

    def change(i=1, j=2):
        i = i + j
        j = j + 1
        print(i, j)
        
    print(change(j = 1, i = 2))
    

    def teaTest(num):
        DIV_BY_3_RESULT = "Tea"
        DIV_BY_5_RESULT = "Test"

        result = ""

        if num % 3 == 0:
            result += DIV_BY_3_RESULT
        if num % 5 == 0:
            result += DIV_BY_5_RESULT

        return result if result != "" else num

    input = [('CACUL1', 1002.238), ('NACC1', 0.324), ('MYC', 0.92), ('MAP2K7', 2327.46), ('SLC16A2', 32.38)]

    result = ['CACUL1', 'MAP2K7']


    def filter_genes(input_list):
        
        new_list = filter(lambda x: x[1] > 1000, input_list)
        
        return new_list

    def filter_genes_list_comprehension(input_list):

        return [x for x in input_list if x[1 > 1000]]

    for i in filter_genes(input):
        print(filter_genes(input))

    print(input)
    for i in input:
        print(i[1])

    print(filter_genes_list_comprehension(input))
