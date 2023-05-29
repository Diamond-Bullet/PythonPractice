class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, vals):
        self.root = ListNode()
        node = self.root
        for i in vals:
            node.val = i
            node.next = ListNode()
            node = node.next

def merge_two_lists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    new_root = ListNode()
    node = new_root
    while list1 and list2:
        if list1.val <= list2.val:
            node.val = list1.val
            list1 = list1.next
        else:
            node.val = list2.val
            list2 = list2.next
        node.next = ListNode()
        node = node.next
    if not list1:
        node = list2
    if not list2:
        node = list1
    return new_root

l1 = LinkedList([1])
l2 = LinkedList([1, 2, 3])
