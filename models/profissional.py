from aed_ds.dictionaries.hash_table import HashTable
from aed_ds.lists.singly_linked_list import SinglyLinkedList

class Profissional:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.servicos = HashTable()
             
        if category == "Medicina":
            self.servicos.insert("Consulta", HashTable())
            self.servicos.insert("PequenaCirurgia", HashTable())
        elif category == "Enfermagem":
            self.servicos.insert("PequenaCirurgia", HashTable())
            self.servicos.insert("Enfermagem", HashTable())
        elif category == "Auxiliar":
            self.servicos.insert("PequenaCirurgia", HashTable())
            self.servicos.insert("Enfermagem", HashTable())
