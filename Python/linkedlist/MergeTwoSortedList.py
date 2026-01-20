
class LinkedList:
    def __init__(self):
        self.head = None
        self.curr = None
    
    def insert(self, val):
        newNode = LinkNode(val)
        if (self.head is None):
            self.head = newNode
            self.curr = self.head
        else:
            self.curr.next = newNode
            self.curr = self.curr.next

    def print(self):
        temp = self.head
        while(temp is not None):
            
class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class Solution:
    def mergeTwoList()