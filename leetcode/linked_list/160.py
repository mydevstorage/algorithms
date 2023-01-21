'''Intersection of Two Linked Lists'''

class Solution:
    def getIntersectionNode(self, headA, headB):
        a, b = headA, headB
        while (a != b):
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a

class Solution:
    def getIntersectionNode(self, headA, headB):
        first_set=set()
        
        while headA:
            first_set.add(headA)
            headA=headA.next
        
        while headB:
            if headB in first_set:
                return headB
            headB=headB.next

        return None