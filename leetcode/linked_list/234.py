'''Palindrom'''

class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"


cur = list1 = Node(1)
for i in [2, 2, 1]:
    cur.next = Node(i)
    cur = cur.next

class Solution:
    def isPalindrome(self, head) -> bool:
        list = []
        while head:
            list.append(head.val)
            head = head.next
        return list==list[::-1]


a = Solution()
print(a.isPalindrome(list1))