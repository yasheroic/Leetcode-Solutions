# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Create a dummy node as the new head to simplify the swapping process
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy  # Pointer to keep track of the previous node
        
        while head and head.next:
            # Nodes to be swapped
            first_node = head
            second_node = head.next
            
            # Update pointers to bypass the nodes to be swapped
            first_node.next = second_node.next
            second_node.next = first_node
            prev.next = second_node
            
            # Move head and prev pointers for the next iteration
            head = first_node.next
            prev = first_node
        
        # Return the head of the modified linked list
        return dummy.next

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4
node4 = ListNode(4)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

s = Solution()
result = s.swapPairs(node1)

# Print the result: 2 -> 1 -> 4 -> 3
while result:
    print(result.val, end=" -> ")
    result = result.next
