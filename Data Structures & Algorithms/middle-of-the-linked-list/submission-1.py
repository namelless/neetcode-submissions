# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        length = 1
        while cur.next:
            cur = cur.next
            length+=1
        
        for i in range(length//2):
            head = head.next
        return head