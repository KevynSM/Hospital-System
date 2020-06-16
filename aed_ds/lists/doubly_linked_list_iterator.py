from ..tad_iterator import TwoWayIterator
from .singly_linked_list_iterator import SinglyLinkedListIterator
from ..exceptions import NoSuchElementException  

class DoublyLinkedListIterator(TwoWayIterator, SinglyLinkedListIterator):
    def __init__(self, linked_list):
        SinglyLinkedListIterator.__init__(self, linked_list)
        self.last = self.linked_list.get_tail()

    # Returns true iff the iteration has more elements in the reverse direction.
    # In other words, returns true if previous would return an element rather than throwing an exception.
    def has_previous(self): 
        return self.position != None
    
    # Returns the previous element in the iteration.
    # Throws NoSuchElementException
    def previous(self): 
        if self.has_previous():
            element = self.position.get_element()
            self.position = self.position.get_previous()
            return element
        else:
            raise NoSuchElementException()   

    # Restarts the iteration in the reverse direction. After fullForward, if the iteration is not empty, previous will return the last element in the iteration.
    def full_forward(self):
        if self.linked_list.is_empty():
            self.position = None
        else:
            self.position = self.linked_list.get_tail()