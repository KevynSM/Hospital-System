class SingleListNode:
    def __init__(self, element, next_node):
        self.element = element
        self.next_node = next_node
    
    def get_element(self):
        return self.element
    
    def get_next(self):
        return self.next_node
    
    def set_element(self, element):
        self.element = element
    
    def set_next(self, next_node):
        self.next_node = next_node

class DoubleListNode(SingleListNode):
    def __init__(self, element, next_node, previous_node):
        SingleListNode.__init__(self, element, next_node)
        self.previous_node = previous_node
    
    def get_previous(self):
        return self.previous_node
    
    def set_previous(self, previous_node):
        self.previous_node = previous_node
