# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        summ=0
        if root is None:
            return 0
        
        if root.val >= L and root.val <= R:
            summ+=root.val
        
        summ+= self.rangeSumBST(root.left,L,R)+self.rangeSumBST(root.right,L,R)
        return summ
