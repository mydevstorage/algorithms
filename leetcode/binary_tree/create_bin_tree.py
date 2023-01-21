class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(7)
root.right.right = Node(7)
root.left.right = Node(6)
root.right.left = Node(6)
