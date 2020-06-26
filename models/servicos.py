from aed_ds.lists.singly_linked_list import SinglyLinkedList

class Servico:
    def __init__(self, name, utente):
        self.name = name        
        self.utente = utente
        self.profissionais = SinglyLinkedList()