# Level: Medium

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'val: {self.val}, next: {self.next}'
        
def create_linked_list(l: List[int])->ListNode:
    head = ListNode(l[0])
    first = head
    for i in range(1, len(l)):
        tmp = ListNode(l[i])
        head.next = tmp
        head = tmp

    return first

def linked_list_to_array(head):
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    
    return out

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        first = head
        tail  = None
        while head is not None:
            temp = head.next

            if temp is None:
                if tail is not None:
                    tail.next = head
                    break
                else:
                    break

            temp_next = temp.next
            temp.next = head   

            if tail is not None:
                tail.next = temp      
            else:
                first = temp
            
            tail = head
            tail.next = None
            head = temp_next
        return first

if __name__ == "__main__":
    arr = [1,2,3,4, 5, 20]
    head = create_linked_list([0])
    print(linked_list_to_array(head))
    print(linked_list_to_array(Solution().swapPairs(head)))