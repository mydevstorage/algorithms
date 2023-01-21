'''108. Convert Sorted Array to Binary Search Tree'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        m = len(nums) // 2
        return TreeNode(nums[m], self.sortedArrayToBST(nums[:m]),
                                 self.sortedArrayToBST(nums[m+1:]))