import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        '''
        A DLL is a good choice to store our elements because will must add and remove elements from both ends of the stack
        often.  The DLL will allow adding and removing elements without running into the size limits of an Array,
        nor the additional efficiency hit of shifting the elements.
        '''
        # Create the linked list that will contain the queue
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size