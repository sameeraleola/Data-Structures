import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # Populate the left side
    def insert(self, value):
        if value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Check for the value at the root (base case)
        if target == self.value:
            return True

            # Look for the value on the right
        if target > self.value:
            if contains(self.right, self.right.value)
                if target == self.right.value:
                    return True
                else:
                    return False


            
        

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # apply the call back
        cb(self.value)

        # base case: the node has no children
        # call the cb on the children of this node
        # let's check that this node has children
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
    
    def iterative_for_each(self, cb):
        # need a while loop and a stack to push and pop elements.
        stack = []
        # must add the root of the tree to the stack so that the loop will run
        stack.append(self)

        # Use a while loop to limit the stack
        while len(stack) > 0:
            current_node = stack.pop()
            #check if the right child exists
            if current_node.right:
                stack.append(current_node.right)
            #check if the left child exists
            if current_node.left:
                stack.append(current_node.left)
            # The cb has to be done after checking for a child
            cb(current_node.value)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
