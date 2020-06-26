from aed_ds.dictionaries.hash_table import HashTable
from aed_ds.lists.singly_linked_list import SinglyLinkedList
from models.profissional import Profissional
from models.utente import Utente
from models.family import Family
import ctypes

class Controller:
    def __init__(self):
        self.category_array = (3 * ctypes.py_object)() # Array of pointers        
        for i in range(3):
            self.category_array[i] = HashTable()

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
            print("Categoria  inexistente.")

        if self.category_array[idx].has_key(name):
            print("Profissional existente")
        else:
            self.category_array[idx].insert(name,Profissional(name,category))
            print("Profissional registrado com sucesso")

    def registrar_utente(self, name, faixa_etaria):
        if self.utente_universe.has_key(name):
            print("Utente existente.")
        elif faixa_etaria not in ["Jovem", "Adulto", "Idoso"]:
            print("Faixa etaria inexistente.")
        else:
            self.utente_universe.insert(name,Utente(name,faixa_etaria))
            print("Utente registrado com sucesso.")

    def registrar_familia(self,name):
        if self.family_universe.has_key(name):
            print("Familia existente.")
        else:
            self.family_universe.insert(name,Family(name))
            print("Familia registrada com sucesso.")
            

    def associar_utente_familia(self,name, family_name):
        if not(self.utente_universe.has_key(name)):
            print("Utente inexistente.")
        elif not(self.family_universe.has_key(family_name)):
            print("Familia inexistente.")
        elif self.family_universe.get(family_name).utentes_associados.find(name) != -1:
            print("Utente percente a familia.")
        else:
            # Associa o utente a familia
            self.family_universe.get(family_name).utentes_associados.insert_last(name)
            # Associa a familia ao utente
            self.utente_universe.get(name).familia_associada = family_name
            print("Utente associado a familia.")

    def desassociar_utente_familia(self,name):
        if not(self.utente_universe.has_key(name)):
            print("Utente inexistente.")
        elif self.utente_universe.get(name).familia_associada == None:
            print("Utente nao pertence a familia.")
        else:
            # Desassocia o utente da familia
            family_name = self.utente_universe.get(name).familia_associada
            position = self.family_universe.get(family_name).utentes_associados.find(name)
            self.family_universe.get(family_name).utentes_associados.remove(position)
            # Desassocia a familia do utente
            self.utente_universe.get(name).familia_associada = None
            print("Utente desassociado da familia.")

            

    def listar_profissionais(self):
        for i in range(3):
            list_names = self.category_array[i].keys()
            list_names_size = list_names.size()
            profissionais_array = (list_names_size * ctypes.py_object)() # Array of pointers
            idx = -1
            # Passing the profissional names from the linkedList to an Array
            it = list_names.iterator()
            while it.has_next():
                current_item = it.next()
                idx += 1
                profissionais_array[idx] = current_item
            # Ordering the array with profissional names
            self.quicksort(profissionais_array, 0, idx, self.comp_strings)
            # Print the profissonal names
            if i == 0:
                category_name = "Medicina"
            elif i == 1:
                category_name = "Enfermagem"
            elif i == 2:
                category_name = "Auxiliar"
            for j in range(list_names_size ):
                print(f"{category_name} {profissionais_array[j]}")    

    def listar_utentes(self):
        if self.utente_universe.size() == 0:
            print(f"Sem utentes registrados")
        else:
            list_itens = self.utente_universe.items()
            # 3 list to separate the "faixas etarias"
            list_jovens = SinglyLinkedList()
            list_adultos = SinglyLinkedList()
            list_idosos = SinglyLinkedList()
            # filing the lists
            it = list_itens.iterator()
            while it.has_next():
                current_item = it.next()
                if current_item.get_value().faixa_etaria == "Jovem":
                    list_jovens.insert_last(current_item.get_value().name)
                elif current_item.get_value().faixa_etaria == "Adulto":
                    list_adultos.insert_last(current_item.get_value().name)
                elif current_item.get_value().faixa_etaria == "Idoso":
                    list_idosos.insert_last(current_item.get_value().name)
            # Create an array for each "faixa etaria" list
            list_jovens_size = list_jovens.size()
            jovens_array = (list_jovens_size * ctypes.py_object)() # Array of pointers
            list_adultos_size = list_adultos.size()
            adultos_array = (list_adultos_size * ctypes.py_object)() # Array of pointers
            list_idosos_size = list_idosos.size()
            idosos_array = (list_idosos_size * ctypes.py_object)() # Array of pointers
            # Passing the lists to an Array and ordering
            # jovens
            idx = -1
            it = list_jovens.iterator()
            while it.has_next():
                current_item = it.next()
                idx += 1
                jovens_array[idx] = current_item
            self.quicksort(jovens_array, 0, idx, self.comp_strings)
            # Adultos
            idx = -1
            it = list_adultos.iterator()
            while it.has_next():
                current_item = it.next()
                idx += 1
                adultos_array[idx] = current_item
            self.quicksort(adultos_array, 0, idx, self.comp_strings)
            # Idosos
            idx = -1
            it = list_idosos.iterator()
            while it.has_next():
                current_item = it.next()
                idx += 1
                idosos_array[idx] = current_item
            self.quicksort(idosos_array, 0, idx, self.comp_strings)
            # Create an ordered array of familis names
            # Exacly how it is in the function listar_familias()
            list_families = self.family_universe.keys()
            list_families_size = list_families.size()
            families_array = (list_families_size * ctypes.py_object)() # Array of pointers
            idx = -1
            # Passing the families from the linkedlist to an Array
            it = list_families.iterator()
            while it.has_next():
                current_item = it.next()
                idx += 1
                families_array[idx] = current_item
            # Ordering the array with families
            self.quicksort(families_array, 0, idx, self.comp_strings)

            # Print the Jovem-Adulto-Idoso order for each Family
            for i in range(list_families_size):
                for j in range(list_jovens_size):
                    if families_array[i] == self.utente_universe.get(jovens_array[j]).familia_associada:
                        print(f"{families_array[i]} Jovem {jovens_array[j]}")
                
                for j in range(list_adultos_size):
                    if families_array[i] == self.utente_universe.get(adultos_array[j]).familia_associada:
                        print(f"{families_array[i]} Adulto {adultos_array[j]}")

                for j in range(list_idosos_size):
                    if families_array[i] == self.utente_universe.get(idosos_array[j]).familia_associada:
                        print(f"{families_array[i]} Idoso {idosos_array[j]}")

            # Print the utenes witchout families associated
            for i in range(list_jovens_size):
                if self.utente_universe.get(jovens_array[i]).familia_associada == None:
                    print(f"Jovem {jovens_array[i]}")
            
            for i in range(list_adultos_size):
                if self.utente_universe.get(adultos_array[i]).familia_associada == None:
                    print(f"Adulto {adultos_array[i]}")

            for i in range(list_idosos_size):
                if self.utente_universe.get(idosos_array[i]).familia_associada == None:
                    print(f"Idoso {idosos_array[i]}")



    def listar_familias(self):
        list_families = self.family_universe.keys()
        list_families_size = list_families.size()
        families_array = (list_families_size * ctypes.py_object)() # Array of pointers
        idx = -1
        # Passing the families from the linkedlist to an Array
        it = list_families.iterator()
        while it.has_next():
            current_item = it.next()
            idx += 1
            families_array[idx] = current_item
        # Ordering the array with families
        self.quicksort(families_array, 0, idx, self.comp_strings)
        # Print the families
        for i in range(list_families_size):
            print(f"{families_array[i]}")
        
    
    def mostrar_familia(self, family_name):
        if not(self.family_universe.has_key(family_name)):
            print("Familia inexistente")
        else:
            list_itens = self.utente_universe.items()
            # 3 list to separate the "faixas etarias"
            list_jovens = SinglyLinkedList()
            list_adultos = SinglyLinkedList()
            list_idosos = SinglyLinkedList()
            # filing the lists
            it = list_itens.iterator()
            while it.has_next():
                current_item = it.next()
                if current_item.get_value().faixa_etaria == "Jovem":
                    list_jovens.insert_last(current_item.get_value().name)
                elif current_item.get_value().faixa_etaria == "Adulto":
                    list_adultos.insert_last(current_item.get_value().name)
                elif current_item.get_value().faixa_etaria == "Idoso":
                    list_idosos.insert_last(current_item.get_value().name)
            # Create an array for each "faixa etaria" list
            list_jovens_size = list_jovens.size()
            jovens_array = (list_jovens_size * ctypes.py_object)() # Array of pointers
            list_adultos_size = list_adultos.size()
            adultos_array = (list_adultos_size * ctypes.py_object)() # Array of pointers
            list_idosos_size = list_idosos.size()
            idosos_array = (list_idosos_size * ctypes.py_object)() # Array of pointers
            # Passing the lists to an Array and ordering
            # jovens
            idx = -1
            it = list_jovens.iterator()
            while it.has_next():
                current_item = it.next()
                idx += 1
                jovens_array[idx] = current_item
            self.quicksort(jovens_array, 0, idx, self.comp_strings)
            # Adultos
            idx = -1
            it = list_adultos.iterator()
            while it.has_next():
                current_item = it.next()
                idx += 1
                adultos_array[idx] = current_item
            self.quicksort(adultos_array, 0, idx, self.comp_strings)
            # Idosos
            idx = -1
            it = list_idosos.iterator()
            while it.has_next():
                current_item = it.next()
                idx += 1
                idosos_array[idx] = current_item
            self.quicksort(idosos_array, 0, idx, self.comp_strings)
            # Print the Jovem-Adulto-Idoso order for the Family
            for j in range(list_jovens_size):
                if family_name == self.utente_universe.get(jovens_array[j]).familia_associada:
                    print(f"Jovem {jovens_array[j]}")
                
            for j in range(list_adultos_size):
                if family_name == self.utente_universe.get(adultos_array[j]).familia_associada:
                    print(f"Adulto {adultos_array[j]}")

            for j in range(list_idosos_size):
                if family_name == self.utente_universe.get(idosos_array[j]).familia_associada:
                    print(f"Idoso {idosos_array[j]}")


    def comp_strings(self, a, b):
        return not(any([a[i] > b[i] for i in range(min(len(a),len(b)))]))

    def quicksort(self, l, left, right, comp):
        i = left
        j = right
        pivot = l[int((i+j)/2)]
        while i <= j:
            while comp(l[i], pivot):
                i += 1
            while comp(pivot, l[j]):
                j -= 1
            if i <= j:
                tmp = l[j]
                l[j] = l[i]
                l[i] = tmp
                i += 1
                j -= 1
        if left < j:
            self.quicksort(l, left, j, comp)
        if i < right:
            self.quicksort(l, i, right, comp)

    