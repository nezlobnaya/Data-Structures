
class Node:
    def __init__(self, value=None,prev = None, next_node=None):
        self.value = value
        self.next_node = next_node
        self.prev = prev
        
    

# build a class to manage nodes
class LinkedList:
    def __init__(self, prev = None, node = None, next_node=None):
        self.head = None  # stores a node that is the begining of the list
        self.tail = None  # stores a node that is the end of the list
        self.prev = prev
        self.next_node = next_node
    
    
    def delete(self, prev = None):
        if self.prev:
            self.prev.next_node = self.next_node
        if self.next_node:
            self.next_node.prev = self.prev


    def add_to_head(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new_node should point to current head
            new_node.next_node = self.head
            # move head to the new node
            self.head = new_node
    def add_to_tail(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # point the node at the current tail to the new node
            self.tail.next_node = new_node
            self.tail = new_node
    def remove_head(self):
        # if list is empty, do nothing
        if not self.head:
            return None
        # if list only has one element, set head and tail to None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # otherwise we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value
    def contains(self, value):
        if self.head is None:
            return False
        # loop through each node, until we see the value, or we cannot go further
        current_node = self.head
        while current_node is not None:
            # check if this is the node we are looking for
            if current_node.value == value:
                return True
            # otherwise, go to the next node
            current_node = current_node.next_node
        return False

    def get_max(self):
        if not self.head: 
            return None
        if self.head.next_node is None:
            return self.head.value
        max_value = 0
        current_node = self.head
        while current_node is not None:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next_node
        return max_value
    
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value


  
