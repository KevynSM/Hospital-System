from aed_ds.lists.singly_linked_list import SinglyLinkedList

class Family:
    def __init__(self, name):
        self.name = name
        self.utentes_associados = SinglyLinkedList()