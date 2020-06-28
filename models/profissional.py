from aed_ds.lists.singly_linked_list import SinglyLinkedList

class Profissional:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.servicos = SinglyLinkedList()