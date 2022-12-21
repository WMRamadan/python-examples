# Complexity is O(n)
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize the head and current node of the result linked list
        head = current = ListNode(0)
        # Initialize the carry variable to 0
        carry = 0
        # Iterate until both linked lists are not empty
        while l1 or l2 or carry:
            # Get the values of the current nodes in the two linked lists and the carry
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            # Calculate the sum of the values and the carry
            sum = val1 + val2 + carry
            # Update the carry to the quotient of the sum divided by 10
            carry = sum // 10
            # Update the current node's value to the remainder of the sum divided by 10
            current.next = ListNode(sum % 10)
            # Move to the next nodes in the two linked lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            # Move to the next node in the result linked list
            current = current.next
        # Return the head of the result linked list, skipping the dummy node
        return head.next

# Test the function
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = Solution().addTwoNumbers(l1, l2)
print(result.val, result.next.val, result.next.next.val)  # 7 0 8
