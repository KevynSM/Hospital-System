from aed_ds.dictionaries.hash_table import HashTable
from aed_ds.lists.singly_linked_list import SinglyLinkedList

class Servico:
    def __init__(self, name, utente):
        self.name = name        
        self.utente = utente
        self.profissionais = HashTable()        

        if name == "Consulta":
            self.profissionais.insert("Medicina", SinglyLinkedList())
        elif name == "PequenaCirurgia":
            self.profissionais.insert("Medicina", SinglyLinkedList())
            self.profissionais.insert("Enfermagem", SinglyLinkedList())
            self.profissionais.insert("Auxiliar", SinglyLinkedList())            
        elif name == "Enfermagem":
            self.profissionais.insert("Enfermagem", SinglyLinkedList())
            self.profissionais.insert("Auxiliar", SinglyLinkedList())