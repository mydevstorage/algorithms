'''Middle of the Linked List'''

class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"


cur = list = Node(1)
for i in range(2, 10):
    cur.next = Node(i)
    cur = cur.next


class Solution:
    def middleNode(self, head):
        res = head
        l = 0
        while head:
            head = head.next
            l += 1
        mid = l//2
        while mid:
            res = res.next
            mid -= 1
        return res

class Solution2:
    def middleNode(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

a = Solution2()
print(a.middleNode(list))