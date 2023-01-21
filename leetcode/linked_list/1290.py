'''Convert Binary Number in a Linked List to Integer'''


class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"


cur = list = Node(1)
for i in [0, 0, 1]:
    cur.next = Node(i)
    cur = cur.next



class Solution:
    def getDecimalValue(self, head) -> int:
        binary = ''
        cur = head
        while cur:
            if cur.val == 1: 
                binary += '1'
            else: 
                binary += '0'
            cur = cur.next
        return int(binary, 2)

a = Solution()
print(a.getDecimalValue(list))