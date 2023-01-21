'''Reverse Linked List'''

class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


cur = head = Node(1)
for i in [2, 3, 4, 5, 6]:
    cur.next = Node(i)
    cur = cur.next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, head):
        # Временная переменная обязательна
        prev = None
        cur  = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
a = Solution()    
print(a.mergeTwoLists(head))