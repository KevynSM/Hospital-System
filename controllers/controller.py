from aed_ds.dictionaries.hash_table import HashTable
from models.profissional import Profissional
from models.utente import Utente
from models.family import Family
import ctypes

class Controller:
    def __init__(self):
        self.category_array = (3 * ctypes.py_object)() # Array of pointers        
        for _ in range(3):
            self.category_array.insert_last(HashTable())

        self.utente_universe = HashTable()
        
        self.family_universe = HashTable()

    def registrar_profissional(self, category, name):
        if category == "Medicina":
            idx = 0
        elif category == "Enfermagem":
            idx = 1
        elif category == "Auxiliar":
            idx = 2
        else:
            print("Categoria  inexistente.\n")

        if self.category_array[idx].has_key(name):
            print("Profissional existente\n")
        else:
            self.category_array[idx].insert(name,Profissional(name,category))
            print("Profissional registrado com sucesso\n")

    def registrar_utente(self, name, faixa_etaria):
        if self.utente_universe.has_key(name):
            print("Utente existente.")
        elif faixa_etaria is not ["Jovem", "Adulto", "Idoso"]:
            print("Faixa etaria inexistente.\n")
        else:
            self.utente_universe.insert(name,Utente(name,faixa_etaria))
            print("Utente registrado com sucesso.\n")

    def registrar_familia(self,name):
        if self.family_universe.has_key(name):
            print("Familia existente.\n")
        else:
            self.family_universe.insert(name,Family(name))
            print("Familia registrada com sucesso.\n")
            

    def associar_utente_familia(self,name, family_name):
        if not(self.utente_universe.has_key(name)):
            print("Utente inexistente.\n")
        elif not(self.family_universe.has_key(family_name)):
            print("Familia inexistente.\n")
        elif self.family_universe.get(family_name).utentes_associados.find(name) != -1:
            print("Utente percente a familia.\n")
        else:
            # Associa o utente a familia
            self.family_universe.get(family_name).utentes_associados.insert_last(name)
            # Associa a familia ao utente
            self.utente_universe.get(name).familia_associada = family_name
            print("Utente associado a familia.\n")

    def desassociar_utente_familia(self,name):
        if not(self.utente_universe.has_key(name)):
            print("Utente inexistente.\n")
        elif self.utente_universe.get(name).familia_associada == None:
            print("Utente nao pertence a familia.\n")
        else:
            # Desassocia o utente da familia
            family_name = self.utente_universe.get(name).familia_associada
            position = self.family_universe.get(family_name).utentes_associados.find(name)
            self.family_universe.get(family_name).utentes_associados.remove(position)
            # Desassocia a familia do utente
            self.utente_universe.get(name).familia_associada = None

            

    def listar_profissionais(self):
        pass

    def listar_utentes(self):
        pass

    def listar_familias(self):
        # list_keys = self.family_universe.keys()
        pass
        