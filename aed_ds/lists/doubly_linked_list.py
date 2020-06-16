from .nodes import DoubleListNode
from ..exceptions import EmptyListException, InvalidPositionException
from .doubly_linked_list_iterator import DoublyLinkedListIterator
from .singly_linked_list import SinglyLinkedList

class DoublyLinkedList(SinglyLinkedList):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position):
        if self.size() == 0:
            raise EmptyListException()
        if position <= int(self.count/2):
            return SinglyLinkedList.get(self, position)
        elif position > int(self.count/2):
            current_node = self.tail
            for _ in range(self.count - 1, position, -1):
                current_node = current_node.get_previous()
            return current_node.get_element()

    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):
        new_node = DoubleListNode(element, self.head, None)
        if self.count == 0:
            self.head = new_node
            self.tail = new_node
        self.head.set_previous(new_node)
        self.head = new_node
        self.count += 1

    # Inserts the specified element at the last position in the list.
    def insert_last(self, element):
        new_node = DoubleListNode(element, None, self.tail)
        if self.count == 0:
            self.head = new_node
            self.tail = new_node
        else:    
            self.tail.set_next(new_node)    
            self.tail = new_node
        self.count += 1

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
    def insert(self, element, position):
        if position not in range(0, self.count+1):
            raise InvalidPositionException()

        if position == 0:
            self.insert_first(element)
        elif position == self.count:
            self.insert_last(element)
        elif position <= int(self.count/2):
            new_node = DoubleListNode(element, None, None)
            previous_node = self.head
            current_node = self.head.get_next()
            for _ in range(0, position-1):
                previous_node = previous_node.get_next()
                current_node = current_node.get_next()
            previous_node.set_next(new_node)
            new_node.set_next(current_node)
            current_node.set_previous(new_node)
            new_node.set_previous(previous_node)
            self.count += 1
        elif position > int(self.count/2):
            new_node = DoubleListNode(element, None, None)
            previous_node = self.tail
            current_node = self.tail.get_previous()
            for _ in range(self.tail, position-1. -1):
                previous_node = previous_node.get_previous()
                current_node = current_node.get_previous()
            previous_node.set_previous(new_node)
            new_node.set_previous(current_node)
            current_node.set_next(new_node)
            new_node.set_next(previous_node)
            self.count += 1      

    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    def remove_first(self):
        if self.size() == 0:
            raise EmptyListException()
        first_node = self.head
        self.head = self.head.get_next()
        first_node.set_next(None)
        if self.count == 1:
            self.count -= 1
            return first_node.get_element()
        self.head.set_previous(None)
        self.count -= 1
        return first_node.get_element()  


    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self):
        if self.size() == 0:
            raise EmptyListException()    
        last_node = self.tail
        self.tail = self.tail.get_previous()
        last_node.set_previous(None)
        if self.count == 1:
            self.count -= 1
            return last_node.get_element()
        self.tail.set_next(None)
        self.count -= 1
        return last_node.get_element()
    
    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    def remove(self, position):
        if position not in range(0, self.count):
            raise InvalidPositionException()
        elif self.count == 1:
            new_node = self.head
            self.make_empty()
            return new_node.get_element()
        elif self.count != 0:
            if position == 0:
                return self.remove_first()
            elif position == self.count - 1:
                return self.remove_last()
            elif position <= int(self.count/2):
                selected_node = self.head
                selected_node = selected_node.get_next()
                current_node = self.head
                for _ in range(0, position - 1):
                    selected_node = selected_node.get_next()
                    current_node = current_node.get_next()
                current_node.set_next(selected_node.get_next())
                selected_node.get_next().set_previous(current_node)
                selected_node.set_next(None)
                selected_node.set_previous(None)
                self.count -= 1
                return selected_node.get_element()
            elif position > int(self.count/2):
                selected_node = self.tail
                selected_node = selected_node.get_previous()
                current_node = self.tail
                for _ in range(self.count - 1, position, -1):
                    selected_node = selected_node.get_previous()
                    current_node = current_node.get_previous()
                current_node.set_previous(selected_node.get_previous())
                selected_node.get_previous().set_next(current_node)    
                selected_node.set_next(None)
                selected_node.set_previous(None)
                self.count -= 1
                return selected_node.get_element()
    
    # Returns an iterator of the elements in the list (in proper sequence).
    def iterator(self):
        return DoublyLinkedListIterator(self)
