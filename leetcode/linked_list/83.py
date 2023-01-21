'''Remove Duplicates from Sorted List'''

class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"


cur = list1 = Node(1)
for i in [1, 1, 4, 5]:
    cur.next = Node(i)
    cur = cur.next




class Solution:
    def deleteDuplicates(self, head):
        cur = prev = head
        while cur:
            cur = cur.next
            if cur and cur.val == prev.val:
                prev.next =  cur.next
                cur = cur.next
            prev = cur   
        return head

a = Solution()
print(a.deleteDuplicates(list1))