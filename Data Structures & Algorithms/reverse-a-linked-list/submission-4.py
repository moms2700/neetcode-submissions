class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr :
            suiv = curr.next
            curr.next = prev
            prev = curr
            curr = suiv
        return prev
