"""
=================================================
938. Range Sum of BST
rangeSumBST()
<https://leetcode.com/problems/range-sum-of-bst/>
=================================================

Given the root node of a binary search tree, return the sum of values of 
all nodes with value between L and R (inclusive).
The binary search tree is guaranteed to have unique values.

Example 1:
----------
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

Example 2:
----------
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
 
Note:
-----
The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.

"""

#  for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def insert_node(self, node):
        if node is None:
            pass
        elif node.val < self.val:
            if self.left is None:
                self.left = node
            else:
                self.left.insert_node(node)
        elif node.val > self.val:
            if self.right is None:
                self.right = node
            else:
                self.right.insert_node(node)
        else:
            pass

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int

        Runtime: 236 ms, faster than 99.15% of Python online submissions for Range Sum of BST.
        Memory Usage: 29 MB, less than 6.45% of Python online submissions for Range Sum of BST.
        """
        
        def bst_sum(node):
            if node is None: 
                return 0
            elif node.val >= L and node.val <= R:
                return node.val + bst_sum(node.left) + bst_sum(node.right)
            elif node.val < L:
                return bst_sum(node.right)
            else:   # node.val > R:
                return bst_sum(node.left)
        
        return bst_sum(root)

        



if __name__ == "__main__":
    root1, L1, R1, out1 = [10, 5, 15, 3, 7, None, 18], 7, 15, 32
    root2, L2, R2, out2 = [10, 5, 15, 3, 7, 13, 18, 1, None, 6], 6, 10, 23
    
    make_nodes = lambda l: [TreeNode(x) if x is not None else x for x in l]
    nodes1 = make_nodes(root1)
    nodes2 = make_nodes(root2)

    get_first = lambda x: x[0:1] if len(x) >= 1 else []
    get_rest = lambda x: x[1:] if len(x) >= 1 else []
    f1 = get_first(nodes1)[0]
    r1 = get_rest(nodes1)
    f2 = get_first(nodes2)[0]
    r2 = get_rest(nodes2)

    [f1.insert_node(x) for x in r1]
    [f2.insert_node(x) for x in r2]

    s = Solution()
    a = s.rangeSumBST(f1, 7, 15)
    b = s.rangeSumBST(f2, 6, 10)

    print(a, b)

    pass



    # s = Solution()
    # a = s.rangeSumBST(root1, L1, R1)
    # b = s.rangeSumBST(root2, L2, R2)

    pass


""" Resources

"""
