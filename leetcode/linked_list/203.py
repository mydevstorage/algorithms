'''Remove Linked List Elements'''
class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"


cur = list1 = Node(1)
for i in [6, 6, 1]:
    cur.next = Node(i)
    cur = cur.next

class Solution:
    def removeElements(self, head, val: int):
        first_node = None
        while head:
            if head.val != val:
                first_node = back = head
                head = head.next
                break
            head = head.next
        while head:
            if head and head.val == val:
                back.next = head.next
                head = head.next
                continue
            back = head
            head = head.next
       
            
        return first_node


class Solution2:
    def removeElements(self, head, val):
        prev = None
        curr = head
        while curr:
    
            if head.val == val:
                head = head.next
            if curr.val == val:
                if prev:
                    prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            
        return head

a = Solution()
a.removeElements(list1, 6)