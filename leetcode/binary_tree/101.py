'''101. Symmetric Tree'''


from create_bin_tree import root

class Solution:
    def isSymmetric(self, root) -> bool:
        def dfs(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            return dfs(a.left, b.right) and dfs(a.right, b.left)
        return dfs(root, root)

solution = Solution()
print(solution.isSymmetric(root))