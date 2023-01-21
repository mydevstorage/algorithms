'''linked list cycle'''


class Solution:
    def hasCycle(self, head) -> bool:
        link_storage = set()
        while head:
            if head in link_storage:
                return True
            link_storage.add(head)
            head = head.next
        return False