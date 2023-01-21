'''SubTree'''

class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

    def isSubTree(self, root, subtree):
        if not subtree:
            return True
        if not root:
            return False
        if self.isSameTree(root, subtree):
            return True
        return self.isSameTree(root.left) or self.isSameTree(root.right)