# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
  
    def reorderList(self, head: Optional[ListNode]) -> None:
        def inverser(head):
            prev = None      
            current = head   
            
            while current:
                next_temp = current.next  
                current.next = prev       
                prev = current            
                current = next_temp       
            
            return prev  
        
        # Trouver le milieu et séparer en deux listes
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Séparer les deux moitiés
        second = slow.next
        slow.next = None
        
        # Inverser la deuxième moitié
        list_2 = inverser(second)
        
        # Fusionner les deux listes
        current = head
        current_2 = list_2
        while current_2:
            temp1 = current.next
            temp2 = current_2.next
            current.next = current_2
            current_2.next = temp1
            current = temp1
            current_2 = temp2