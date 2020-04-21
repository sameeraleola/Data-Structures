"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    # Method 1
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head 
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    # Method 4
    def remove_from_head(self):
        # Must return the value that is in the current head before we delete it.
        value = self.head.value
        self.delete(self.head)
        return(value)

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    # Method 2
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # Must return the value that is in the current head before we delete it.
        value = self.tail.value
        self.delete(self.tail)
        return(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head: # Check that it is not already the head
            return
        self.add_to_head(node.value)
        self.delete(node) # delete the node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail: # Check that it is not already the head
            return
        self.add_to_tail(node.value)
        self.delete(node) # delete the node

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    # Method 3
    def delete(self, node):
        ### Planning ###
        # This is the only node so remove the pointers to it
        if self.head is self.tail:
            self.head = None
            self.tail = None 
        # It's the head
        elif node is self.head:
            self.head = node.next
            node.delete()
        # It's the tail
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        # It's in the middle
        else:
            node.delete()  # We only have to delete because we are being passed the node address (reference to the node)
        self.length -= 1 


    """Returns the highest value currently in the list"""
    def get_max(self):
        # How do we get max? Loop through the nodes
        # Create a variable to hold max which is the head because we're starting at the beginning
        max = self.head.value # TODO: Does this need to handle negative numbers
        # Create a tracking variable to know where we are
        current = self.head
        # Loop using a while because we don't know how many times we have to loop.  For-Loops are good when we know how many loops we have to make.
        while (current is not None):
            # Compare the value in the node to the max found
            if current.value > max:
                max = current.value
            current = current.next # Go to the next element in the DLL
        return max # when we are done


