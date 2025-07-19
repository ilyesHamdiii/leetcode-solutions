# https:https://leetcode.com/problems/leaf-similar-trees/description/?envType=study-plan-v2&envId=leetcode-75
# Difficulty: Easy


# Time: O(n)
# Space: O(n1+n2)
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root):
            
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            return dfs(root.left)+ dfs(root.right)
        return dfs(root1)==dfs(root2)
                    