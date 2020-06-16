from abc import ABC, abstractmethod
class List(ABC):
    # Returns true iff the list contains no elements.
    @abstractmethod
    def is_empty(self): pass

    # Returns the number of elements in the list.
    @abstractmethod
    def size(self): pass

    # Returns the first element of the list.
    # Throws EmptyListException.
    @abstractmethod
    def get_first(self): pass

    # Returns the last element of the list.
    # Throws EmptyListException.
    @abstractmethod
    def get_last(self): pass

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    @abstractmethod
    def get(self, position): pass

    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.
    @abstractmethod
    def find(self, element): pass

    # Inserts the specified element at the first position in the list.
    @abstractmethod
    def insert_first(self, element): pass

    # Inserts the specified element at the last position in the list.
    @abstractmethod
    def insert_last(self, element): pass

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
    @abstractmethod
    def insert(self, element, position): pass

    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    @abstractmethod
    def remove_first(self): pass

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    @abstractmethod
    def remove_last(self): pass
    
    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    @abstractmethod
    def remove(self, position): pass
    
    # Removes all elements from the list.
    @abstractmethod
    def make_empty(self): pass

    # Returns an iterator of the elements in the list (in proper sequence).
    @abstractmethod
    def iterator(self): pass
