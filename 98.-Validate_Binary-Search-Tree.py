# The idea is to do pre order traversal and checking the range of root
# The lower range will be parent if right child 
# The upper range will be parent if left child
# There are also some other things to consider like in the subtree of any node ex:- Right subtree no node can be lower than the current node
# So for the left sub trees value of low will not change similarly for the right subtrees high value will not change

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:  
        def preOrder(root,low,high):
            if root == None:
                return True
            if root.val <=low or root.val>=high:
                return False
            return preOrder(root.left,low,root.val) and preOrder(root.right,root.val,high)
        return preOrder(root,float('-inf'),float('inf'))
