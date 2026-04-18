# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            def sametree(n1, n2):
                if not n1 and not n2:
                    return True
                if not n1 or not n2:
                    return False

                if n1.val != n2.val:
                    return False

                return sametree(n1.left, n2.left) and sametree(n1.right, n2.right)

            if not node1:
                return False
                
            if sametree(node1, node2):
                return True

            return dfs(node1.left, node2) or dfs(node1.right, node2)
        
        return dfs(root, subRoot)