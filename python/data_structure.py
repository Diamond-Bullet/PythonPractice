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

    def merge(self, list2):
        if not list2:
            return

        list1 = self.root
        if not list1:
            self.root = list2
            return

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
        self.root = new_root

class UnionFind:
    def __init__(self, n):
        self.__parents = [i for i in range(n)]
        self.__size = [1] * n
        self.__pile = n

    def parent(self, x):
        while x != self.__parents[x]:
            x = self.__parents[x]
        return x

    def unite(self, x, y):
        px, py = self.parent(x), self.parent(y)
        if px != py:
            self.__parents[py] = px
            self.__size[px] += self.__size[py]

    def connected(self, x, y):
        return self.parent(x) == self.parent(y)

    def get_pile(self):
        return self.__pile
