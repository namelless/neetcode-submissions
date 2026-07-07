# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def greatest_divisor(num1, num2):
            divisor = 1
            ans = divisor
            while divisor <= min(num1,num2):
                if (num1/divisor).is_integer() and (num2/divisor).is_integer():
                    ans = divisor
                divisor += 1
            return ans

        node = head
        while node.next:
            n = node.next
            node.next = ListNode(greatest_divisor(node.val, n.val), n)
            node = n
        return head
