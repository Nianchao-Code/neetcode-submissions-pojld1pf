# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, cur_largest):
            if not node:
                return 0

            good = 1 if node.val >= cur_largest else 0
            cur_largest = max(cur_largest, node.val)

            return good + dfs(node.left, cur_largest) + dfs(node.right, cur_largest)

        return dfs(root, root.val)

