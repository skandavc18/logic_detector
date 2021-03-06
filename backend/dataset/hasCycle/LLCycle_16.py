class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        while head:
            if not head.val:
                return True
            head.val = None
            head = head.next
        return False
