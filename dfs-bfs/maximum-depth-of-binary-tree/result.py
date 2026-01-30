# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, depth):
            if node is None:
                return depth - 1
            left_depth = dfs(node.left, depth+1)
            right_depth = dfs(node.right, depth+1)

            return max(left_depth, right_depth)

        return dfs(root, 1)