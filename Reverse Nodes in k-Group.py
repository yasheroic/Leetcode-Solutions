# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Count the number of nodes in the linked list
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        # Create a dummy node as the new head to simplify the reversal process
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy  # Pointer to keep track of the previous node
        
        # Reverse nodes k at a time
        while n >= k:
            # Initialize pointers for reversal
            first_node = prev.next
            second_node = first_node.next
            
            # Reverse k nodes
            for i in range(k - 1):
                first_node.next = second_node.next
                second_node.next = prev.next
                prev.next = second_node
                second_node = first_node.next
            
            # Move prev and head pointers for the next iteration
            prev = first_node
            head = first_node.next
            n -= k
        
        return dummy.next

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

s = Solution()
k = 2
result = s.reverseKGroup(node1, k)

# Print the result: 2 -> 1 -> 4 -> 3 -> 5
while result:
    print(result.val, end=" -> ")
    result = result.next
