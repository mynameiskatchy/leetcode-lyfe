"""
====================================================================================================
237. Delete Node in a Linked List
deleteNode()
<https://leetcode.com/problems/delete-node-in-a-linked-list/>
<https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/553/>
====================================================================================================

Write a function to delete a node (except the tail) in a singly linked list, 
given only access to that node.

<see page>
Given linked list -- head = [4,5,1,9], which looks like following:

Example 1:
----------
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

Example 2:
----------
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
 
Note:
-----
The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        
        Runtime: 32 ms, faster than 40.35% of Python online submissions for Delete Node in a Linked List.
        Memory Usage: 13.3 MB, less than 23.70% of Python online submissions for Delete Node in a Linked List.
        
        Runtime: 28 ms, faster than 70.29% of Python online submissions for Delete Node in a Linked List.
        Memory Usage: 13.3 MB, less than 33.80% of Python online submissions for Delete Node in a Linked List.
        
        Runtime: 24 ms, faster than 90.42% of Python online submissions for Delete Node in a Linked List.
        Memory Usage: 13.2 MB, less than 69.43% of Python online submissions for Delete Node in a Linked List.
        """
        node.val = node.next.val
        node.next = node.next.next

        


if __name__ == "__main__":
    head = [4, 5, 1, 9]
    head = [ListNode(i) for i in head]

    for i in range(len(head)-1):
        head[i].next = head[i + 1]
        
    node1 = 5
    node2 = 1



    pass
