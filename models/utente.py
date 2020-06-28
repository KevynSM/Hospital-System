from aed_ds.lists.singly_linked_list import SinglyLinkedList

class Utente:
    def __init__(self, name, faixa_etaria):
        self.name = name
        self.faixa_etaria = faixa_etaria
        self.familia_associada = None
        self.servico = SinglyLinkedList()