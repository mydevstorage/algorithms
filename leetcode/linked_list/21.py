'''Merge Two Sorted Lists'''

class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"


cur = list1 = Node(1)
for i in [2, 4]:
    cur.next = Node(i)
    cur = cur.next
cur = list2 = Node(1)
for i in [3, 8, 9]:
    cur.next = Node(i)
    cur = cur.next

print(list1, list2)



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        '''Create new list '''
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else: 
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next

a = Solution()
print(a.mergeTwoLists(list1.head, list2.head))