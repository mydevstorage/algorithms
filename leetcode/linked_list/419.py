'''Delete N nodes after M nodes in linked list'''

class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"


cur = list1 = Node(1)
for i in [2, 3, 4, 5, 6, 7]:
    cur.next = Node(i)
    cur = cur.next


class Solution:
    def deleteNodes(self, head, skip, delete):
        prev = None
        cur = head
        if not skip and delete:
            return None
        if not delete:
            return head
        while cur:
            for i in range(skip):
        
                prev = cur
                cur = cur.next
            for i in range(delete):
             
                prev.next = cur.next
                cur = cur.next
        return head

solution = Solution()
print(solution.deleteNodes(list1, 2, 2))