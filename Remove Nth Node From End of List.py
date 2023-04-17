class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Create a dummy node and connect it to the head
        dummy = ListNode(0, head)
        # Calculate the length of the list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        # Calculate the index of the node to be removed from the beginning
        index = length - n
        # Traverse the list to the node before the node to be removed
        curr = dummy
        for i in range(index):
            curr = curr.next
        # Remove the node
        curr.next = curr.next.next
        return dummy.next
