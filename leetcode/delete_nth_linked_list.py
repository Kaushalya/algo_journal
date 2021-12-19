# Level: Medium

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nth_node = head
        node_count = 1
        first =  head
        
        while head is not None:
            if node_count > n:
                if head.next is not None:
                    nth_node = nth_node.next
            head = head.next
            node_count += 1

        if n==node_count-1:
            first = first.next
        elif nth_node is not None and nth_node.next is not None:
            print(nth_node.val)
            nth_node.next = nth_node.next.next
            nth_node.next
            
        return first
