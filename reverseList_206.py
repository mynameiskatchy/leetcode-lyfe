"""
====================================================================================================
206. Reverse Linked List
reverseLinkedList()
<https://leetcode.com/problems/reverse-linked-list/>
<https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/>
====================================================================================================

Reverse a singly linked list.

Example:
--------
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. 
Could you implement both?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode


        Runtime: 24 ms, faster than 80.79% of Python online submissions for Reverse Linked List.
        Memory Usage: 14.8 MB, less than 51.20% of Python online submissions for Reverse Linked List.
        """

        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev


    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head  # Empty.
        if not head.next:
            return head  # We reached end.
        # Traverse to end, orig_head is now end node.
        orig_head = self.reverseList(head.next)
        head.next.next = head  # Swap head with right node.
        head.next = None  # So we don't wind up in infinite loop.
        return orig_head  # Very last thing returned. End node!


if __name__ == "__main__":
    pass
