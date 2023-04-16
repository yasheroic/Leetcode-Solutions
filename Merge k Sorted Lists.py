class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Create a dummy head node for the merged linked list
        dummy = ListNode()
        # Create a pointer to the current node in the merged linked list
        current = dummy
        # Create a heap to store the head nodes of all the linked lists
        heap = []
        
        # Add the head nodes of all non-empty linked lists to the heap
        for i in range(len(lists)):
            if lists[i]:
                heap.append((lists[i].val, i, lists[i]))
                
        # Convert the list into a heap
        heapq.heapify(heap)
        
        # While there are still nodes in the heap
        while heap:
            # Pop the node with the smallest value from the heap
            val, i, node = heapq.heappop(heap)
            # Add the node to the merged linked list
            current.next = node
            current = current.next
            # If there are still nodes in the linked list, add the next node to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        # Return the merged linked list (ignoring the dummy head node)
        return dummy.next
