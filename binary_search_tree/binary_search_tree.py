import sys
#sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # If check if empty.  If it is create the node at root. If empty is the base case.
    # If not empty if new < node.value add it to the left else go right
    # Repeat for other left nodes
    # Populate the right side
    def insert(self, value):
        #  if self.svalue = value # This new node is = to current node so put it on the right
        # Put node here/at root
        # self.storage.add_to_tail.value
        
        # if value >= self.value:
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                # rightnode.insertvalue
                self.right = BinarySearchTree(value)
        else:
            if self.left:
                self.left.insert(value)
            else:
                # leftnode.insert value
                self.left = BinarySearchTree(value)
        
    # Return True if the tree contains the value
    # False if it does not
     # If the search node  is found return true
    # If the node is < node.value go left.  If no left node return.  If node is left keep going left
    #---- Notes
        # if node is none
        #     return false

        # if node.value == findvalue
        #     return true
        # else
        #     if find <  node.value
        #         find on  left node
        #     else
        #         find on right node
    def contains(self, target):
        if self.value == target:
            return True
        
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
     
    # Sean's solution 4/23/2020     
    # def contains(self, target):
    #     # Check for the value at the root (base case)
    #     if target == self.value:
    #         return True
            # Look for the value on the right
        # if target > self.value:
        #     if contains(self.right, self.right.value)
        #         if target == self.right.value:
        #             return True
        #         else:
        #             return False


    # Return the maximum value found in the tree
    # The max is always the right most node
    # If there is no value, return
    # ------ Psudo code notes
        # if there's a right:
        #     get max on  right
        # else
        #     return node.value
    def get_max(self): 
        # if there's a right:
        if self.right:
        # get max on  right
            return self.right.get_max()
        else:
        # return node.value
            return self.value


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach (it's cleaner and simplier)
    def for_each(self, cb):
        # Call the cb function is step 1
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        # This is actually a depth first traversal of the tree!
    
    # From Sean in lecture
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

    # Difference between traversal and search: in traversal you go through all the nodes, in a search you (attempt) to go to a specific node.
       # search you (attempt) to go to a specific node.
    # We are using binary trees for this project is just because we have one handy to use 

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # Research how to do this
    def in_order_print(self, node):
       if node.left is not None:
           node.left.in_order_print(node.left)
       if node.right is not None:
           node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
     # This is good to do iterative.  
    # Best structure for this is a stack
    # This one you to get to the bottom
    # To go from bfs to dfs change the data structure from 
        #------ Notes
    # We go layer by layer one node at a time its broad).  This can be used to find the shortest path in a graph
    # We must use a queue to do breath first search.  It has a runtime complexity of O(n)   
    def bft_print(self, node):
         # Create the queue
        # Add node to queue (node = root = head of queue)
        # While the queue is not empty
        # DO THE NODE ACTION (we are printing)
        # Add children of node to queue
        # Pop the node off of the queue
        # When do we print?  Right after the while       
        queue = Queue()
        queue.enqueue(node)
        while queue.size > 0:
            node_value = queue.dequeue()
            if node_value.left is not None:
                queue.enqueue(node_value.left)
            if node_value.right is not None:
                queue.enqueue(node_value.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Create the stack
        # Add node to stack  (node = root = head of queue)
        # While the stack is not empty
        # Pop the node off of the stack to temp variable
        # DO THE NODE ACTION (we are printing)
         # Add children of node to stack
        the_stack = Stack()
        the_stack.push(node)
        while the_stack.len() > 0:
            temp_var = the_stack.pop()
            if temp_var.right is not None:
                the_stack.push(temp_var.right)
            if temp_var.left is not None:
                the_stack.push(temp_var.left)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
