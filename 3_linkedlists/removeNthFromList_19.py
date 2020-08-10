"""
====================================================================================================
19. Remove Nth Node From End of List
removeNthFromEnd()
<https://leetcode.com/problems/remove-nth-node-from-end-of-list/>
<https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/>
====================================================================================================

Given a linked list, remove the n-th node from the end of list and return its head.

Example:
--------
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
-----
Given n will always be valid.

Follow up:
Could you do this in one pass?

Hide Hint #1  
------------
Maintain two pointers and update one with a delay of n steps.
"""


def make_links(nums):
    nodes = [ListNode(i) for i in nums]

    for i in range(len(nums) - 1):
        nodes[i].next = nodes[i + 1]
    
    return nodes[0]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.len = 1
    
    def __repr__(self):
        print(self.val)
        if self.next != None:
            self.next.__repr__()

    def __len__(self):
        if self.next == None:
            return self.len
        else:
            return self.len + self.next.__len__()


class Solution(object):
    def removeNthFromEnd_1(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr = head
        # Find out length of linked list by traversing it
        l = len(head)
        for i in range(l):
            if i == l - n - 1:
                curr.next = curr.next.next
                break
            else:
                curr = curr.next

        return head

    def removeNthFromEnd_2(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr = head
        # Find out length of linked list by traversing it
        l = len(head)
        for i in range(l):
            if i == l - n - 1:
                curr.next = curr.next.next
                break
            else:
                curr = curr.next

        return head

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode

        # without knowing the number of nodes in advance

        Runtime: 24 ms, faster than 66.77% of Python online submissions for Remove Nth Node From End of List.
        Memory Usage: 12.7 MB, less than 69.30% of Python online submissions for Remove Nth Node From End of List.
        
        Runtime: 12 ms, faster than 99.70% of Python online submissions for Remove Nth Node From End of List.
        Memory Usage: 12.6 MB, less than 95.27% of Python online submissions for Remove Nth Node From End of List.
        
        Runtime: 16 ms, faster than 96.98% of Python online submissions for Remove Nth Node From End of List.
        Memory Usage: 12.7 MB, less than 74.97% of Python online submissions for Remove Nth Node From End of List.
        """

        # initialize fast and slow pointers 
        fast = head
        slow = head

        # move the fast pointer up n nodes ahead
        for _ in range(n):
            fast = fast.next
        
        # if fast pointer doesnt point to a node
        if not fast:
            return head.next

        # move both pointers up until one of them points to last node
        # then we know slow pointer is n spots behind
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        #return head node
        return head
        

if __name__ == "__main__":
    
    input1 = [1, 2, 3, 4, 5]
    head1 = make_links(input1)
    
    s = Solution()
    s.removeNthFromEnd(head1, 2)


    pass
