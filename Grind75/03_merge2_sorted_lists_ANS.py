class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    # Create a dummy node to act as the start of the merged list
    dummy = ListNode()
    # Pointer to build the new list
    current = dummy
    
    # Iterate while both lists are not empty
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Append the remaining nodes from either list1 or list2
    if list1:
        current.next = list1
    elif list2:
        current.next = list2
    
    # The merged list starts from the next of the dummy node
    return dummy.next