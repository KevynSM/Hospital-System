from aed_ds.dictionaries.hash_table import HashTable
from aed_ds.lists.singly_linked_list import SinglyLinkedList
from models.profissional import Profissional
from models.utente import Utente
from models.family import Family
from models.servicos import Servico
import ctypes

class Controller:
    def __init__(self):
        # self.category_array = (3 * ctypes.py_object)() # Array of pointers        
        # for i in range(3):
        #     self.category_array[i] = HashTable()

        self.categories = HashTable()
        self.categories.insert("Medicina", HashTable())
        self.categories.insert("Enfermagem", HashTable())
        self.categories.insert("Auxiliar", HashTable())

        self.categories_list_ordered = SinglyLinkedList()
        self.categories_list_ordered.insert_last("Medicina")
        self.categories_list_ordered.insert_last("Enfermagem")
        self.categories_list_ordered.insert_last("Auxiliar")



        self.utente_universe = HashTable()
        
        self.family_universe = HashTable()

        self.servicos = HashTable()
        self.servicos.insert("Consulta",SinglyLinkedList())
        self.servicos.insert("PequenaCirurgia",SinglyLinkedList())
        self.servicos.insert("Enfermagem",SinglyLinkedList())

        self.servicos_list_ordered = SinglyLinkedList()
        self.servicos_list_ordered.insert_last("Consulta")
        self.servicos_list_ordered.insert_last("PequenaCirurgia")
        self.servicos_list_ordered.insert_last("Enfermagem")

#-------------------------------- Booleans --------------------------------------------
    def has_utente(self, name):
        if self.utente_universe.has_key(name):
            return True
        return False

    def there_are_utentes(self):
        if self.utente_universe.size() > 0:
            return True
        return False

    def has_faixa_etaria(self, faixa_etaria):
        if faixa_etaria in ["Jovem", "Adulto", "Idoso"]:
            return True
        return False

    def has_that_family(self, family_name):        
        if self.family_universe.has_key(family_name):
            return True
        return False

    def has_family(self):
        if self.family_universe.size():
            return True
        return False
        
    def utente_has_family(self, name):
        if self.utente_universe.get(name).familia_associada != None:
            return True 
        return False

    def has_category(self, name):
        list_categories = self.categories.keys()
        it = list_categories.iterator()
        while it.has_next():
            current_item = it.next()
            if name == current_item:
                return True
        return False


    def has_profissional(self):
        list_keys = self.categories.keys()        
        it = list_keys.iterator()
        while it.has_next():
            current_item = it.next()
            if self.categories.get(current_item).size() > 0:
                return True
        return False

    def has_profissional_category(self, name, category):
        list_profissionais = self.categories.get(category).keys()
        it = list_profissionais.iterator()
        while it.has_next():
            current_item = it.next()
            if name == current_item:
                return True
        return False

    def has_service(self, name):
        list_servicos = self.servicos.keys()
        it = list_servicos.iterator()
        while it.has_next():
            current_item = it.next()
            if name == current_item:
                return True
        return False

    def service_has_category(self, service, category):
        if service == "Consulta":
            if category == "Medicina":
                return True
        elif service == "PequenaCirurgia":
            if category in ["Medicina", "Enfermagem", "Auxiliar"]:
                return True
        elif service == "Enfermagem":
            if category in ["Enfermagem", "Auxiliar"]:
                return True
        return False

    def has_valid_sequence(self, service_list):
        last_consulta = False
        last_pequena_cirurgia = False        
        it = service_list.iterator()
        while it.has_next():
            current_service = it.next()            
            if current_service.name == "Consulta":
                last_consulta = True
            if current_service.name == "PequenaCirurgia" and last_consulta == False:
                return False
            if current_service.name == "PequenaCirurgia":
                last_pequena_cirurgia = True
                last_consulta = False
            if last_pequena_cirurgia == True and current_service.name == "Consulta":
                last_pequena_cirurgia = False
        if last_pequena_cirurgia == True:
            return False
        return True

                
    def has_service_utente(self, utente):
        list_keys = self.utente_universe.get(utente).servicos.keys()
        it = list_keys.iterator()
        while it.has_next():
            current_key = it.next()
            if not(self.utente_universe.get(utente).servicos.get(current_key).is_empty()):
                return True
        return False
                

    def has_service_family(self, family_name):
        list_utentes = self.family_universe.get(family_name).utentes_associados
        it = list_utentes.iterator()
        while it.has_next():
            current_item = it.next()
            if self.utente_universe.get(current_item).servicos.get("Consulta").size() > 0:
                return True
            if self.utente_universe.get(current_item).servicos.get("PequenaCirurgia").size() > 0:
                return True
            if self.utente_universe.get(current_item).servicos.get("Enfermagem").size() > 0:
                return True
        return False

    def has_service_profissional(self, name, category):
        if category == "Medicina":
            if self.categories.get("Medicina").get(name).servicos.get("Consulta").size() > 0:
                return True
            if self.categories.get("Medicina").get(name).servicos.get("PequenaCirurgia").size() > 0:
                return True
        elif category == "Enfermagem":
            if self.categories.get("Medicina").get(name).servicos.get("PequenaCirurgia").size() > 0:
                return True
            if self.categories.get("Medicina").get(name).servicos.get("Enfermagem").size() > 0:
                return True
        elif category == "Auxiliar":
            if self.categories.get("Medicina").get(name).servicos.get("PequenaCirurgia").size() > 0:
                return True
            if self.categories.get("Medicina").get(name).servicos.get("Enfermagem").size() > 0:
                return True
        return False


    def are_there_service(self, service):
        if self.servicos.get(service).size() > 0:
            return True
        return False


#------------------------------------ do something ----------------------------------
    def registrar_profissional(self, name, category):
        self.categories.get(category).insert(name,Profissional(name,category))

    def registrar_utente(self, name, faixa_etaria):
        self.utente_universe.insert(name,Utente(name,faixa_etaria))

    def registrar_familia(self, name):
        self.family_universe.insert(name,Family(name))

    def associar_utente_familia(self, name, family_name):
        # Associa o utente a familia
        self.family_universe.get(family_name).utentes_associados.insert_last(name)
        # Associa a familia ao utente
        self.utente_universe.get(name).familia_associada = family_name        

    def desassociar_utente_familia(self,name):
        # Desassocia o utente da familia
        family_name = self.utente_universe.get(name).familia_associada
        position = self.family_universe.get(family_name).utentes_associados.find(name)
        self.family_universe.get(family_name).utentes_associados.remove(position)
        # Desassocia a familia do utente
        self.utente_universe.get(name).familia_associada = None

    def listar_profissionais(self):
        #list that will be return
        list_profissionais = SinglyLinkedList()
        # list_categories = [Medicina, Enfermagem, Auxiliar]
        # list_categories = self.categories.keys()
        list_categories = self.categories_list_ordered
        # for each category
        it = list_categories.iterator()
        while it.has_next():
            #category name
            category = it.next()
            
            # list of names in the caregory
            list_names = self.categories.get(category).keys()
            list_names_size = list_names.size()
            
            if list_names_size > 0:
                # array_size = list_name_size
                profissionais_array = (list_names_size * ctypes.py_object)() # Array of pointers
                idx = -1
                # for each name in the category
                it_category = list_names.iterator()
                while it_category.has_next():
                    current_item = it_category.next()
                    
                    idx += 1 
                    
                    profissionais_array[idx] = current_item
                # order the array
                self.quicksort(profissionais_array, 0, idx, self.comp_strings)
                # pass the the names from the ordered array to the final list
                for i in range(idx+1):
                    list_profissionais.insert_last(f"{category} {profissionais_array[i]}")
        return list_profissionais

    def listar_utentes(self):
        # lsit that will be returned
        list_utentes = SinglyLinkedList()     
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
        if len(jovens_array) > 0:
            idx = -1
            it = list_jovens.iterator()
            while it.has_next():
                current_item = it.next()
                idx += 1
                jovens_array[idx] = current_item
            self.quicksort(jovens_array, 0, idx, self.comp_strings)
        # Adultos
        if len(adultos_array) > 0:
            idx = -1
            it = list_adultos.iterator()
            while it.has_next():
                current_item = it.next()
                idx += 1
                adultos_array[idx] = current_item
            self.quicksort(adultos_array, 0, idx, self.comp_strings)
        # Idosos
        if len(idosos_array) > 0:
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
        if len(families_array) > 0:
            it = list_families.iterator()
            while it.has_next():
                current_item = it.next()
                idx += 1
                families_array[idx] = current_item
            # Ordering the array with families
            self.quicksort(families_array, 0, idx, self.comp_strings)

        # Print the Jovem-Adulto-Idoso order for each Family
        if len(families_array) > 0: 
            for i in range(list_families_size):
                if len(jovens_array) > 0:
                    for j in range(list_jovens_size):
                        if families_array[i] == self.utente_universe.get(jovens_array[j]).familia_associada:
                            # print(f"{families_array[i]} Jovem {jovens_array[j]}")
                            list_utentes.insert_last(f"{families_array[i]} Jovem {jovens_array[j]}")
                
                if len(adultos_array) > 0:
                    for j in range(list_adultos_size):
                        if families_array[i] == self.utente_universe.get(adultos_array[j]).familia_associada:
                            # print(f"{families_array[i]} Adulto {adultos_array[j]}")
                            list_utentes.insert_last(f"{families_array[i]} Adulto {adultos_array[j]}")

                if len(idosos_array) > 0:
                    for j in range(list_idosos_size):
                        if families_array[i] == self.utente_universe.get(idosos_array[j]).familia_associada:
                            # print(f"{families_array[i]} Idoso {idosos_array[j]}")
                            list_utentes.insert_last(f"{families_array[i]} Idoso {idosos_array[j]}")

        # Print the utenes witchout families associated
        if len(jovens_array) > 0:
            for i in range(list_jovens_size):
                if self.utente_universe.get(jovens_array[i]).familia_associada == None:
                    # print(f"Jovem {jovens_array[i]}")
                    list_utentes.insert_last(f"Jovem {jovens_array[i]}")
        if len(adultos_array) > 0:   
            for i in range(list_adultos_size):
                if self.utente_universe.get(adultos_array[i]).familia_associada == None:
                    # print(f"Adulto {adultos_array[i]}")
                    list_utentes.insert_last(f"Adulto {adultos_array[i]}")
        if len(idosos_array) > 0:
            for i in range(list_idosos_size):
                if self.utente_universe.get(idosos_array[i]).familia_associada == None:
                    # print(f"Idoso {idosos_array[i]}")
                    list_utentes.insert_last(f"Idoso {idosos_array[i]}")
        return list_utentes

    
    def listar_familias(self):
        #list that will be returned
        list_families_final = SinglyLinkedList()
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
            list_families_final.insert_last(f"{families_array[i]}")
        return list_families_final



    def mostrar_familia(self, family_name):
        # lsit that will be returned
        list_family = SinglyLinkedList()
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
        if len(jovens_array) > 0:
            idx = -1
            it = list_jovens.iterator()
            while it.has_next():
                current_item = it.next()
                idx += 1
                jovens_array[idx] = current_item
            self.quicksort(jovens_array, 0, idx, self.comp_strings)
        # Adultos
        if len(adultos_array) > 0:
            idx = -1
            it = list_adultos.iterator()
            while it.has_next():
                current_item = it.next()
                idx += 1
                adultos_array[idx] = current_item
            self.quicksort(adultos_array, 0, idx, self.comp_strings)
        # Idosos
        if len(idosos_array) > 0:
            idx = -1
            it = list_idosos.iterator()
            while it.has_next():
                current_item = it.next()
                idx += 1
                idosos_array[idx] = current_item
            self.quicksort(idosos_array, 0, idx, self.comp_strings)
        # Print the Jovem-Adulto-Idoso order for the Family
        if len(jovens_array) > 0:
            for j in range(list_jovens_size):
                if family_name == self.utente_universe.get(jovens_array[j]).familia_associada:
                    # print(f"Jovem {jovens_array[j]}")
                    list_family.insert_last(f"Jovem {jovens_array[j]}")
        if len(adultos_array) > 0:      
            for j in range(list_adultos_size):
                if family_name == self.utente_universe.get(adultos_array[j]).familia_associada:
                    # print(f"Adulto {adultos_array[j]}")
                    list_family.insert_last(f"Adulto {adultos_array[j]}")
        if len(idosos_array) > 0:
            for j in range(list_idosos_size):
                if family_name == self.utente_universe.get(idosos_array[j]).familia_associada:
                    #print(f"Idoso {idosos_array[j]}")
                    list_family.insert_last(f"Idoso {idosos_array[j]}")

        return list_family




    def create_service(self, service, utente):
        return Servico(service, utente)

    def fill_service(self, service, profissional, category):
        service.profissionais.get(category).insert_last(profissional)


    def marcar_cuidados_utente(self, list_service, utente):            
        it = list_service.iterator()
        while it.has_next():            
            current_service = it.next()
            # variables needed = serviuce_name, service, utente, profissional, category
            # service = current_service
            # utente = OK
            # service_name:
            service_name = current_service.name
            # profissional e category
            list_profissionais_medicina = None
            list_profissionais_enfermagem = None
            list_profissionais_auxiliar = None
            if service_name == "Consulta":
                list_profissionais_medicina = current_service.profissionais.get("Medicina")
            elif service_name == "PequenaCirurgia":
                list_profissionais_medicina = current_service.profissionais.get("Medicina")
                list_profissionais_enfermagem = current_service.profissionais.get("Enfermagem")
                list_profissionais_auxiliar = current_service.profissionais.get("Auxiliar")
            elif service_name == "Enfermagem":
                list_profissionais_enfermagem = current_service.profissionais.get("Enfermagem")
                list_profissionais_auxiliar = current_service.profissionais.get("Auxiliar")

            # Marcar service com o utente
            self.utente_universe.get(utente).servicos.get(service_name).insert_last(current_service)
            # Marcar service na lista de servicos
            self.servicos.get(service_name).insert_last(current_service)
            # Marcar o service com os profissionais
            # Medicina
            if list_profissionais_medicina is not None:
                it_p = list_profissionais_medicina.iterator()
                while it_p.has_next():
                    current_profissional = it_p.next()
                    #existe key com nome do utente?
                    if not(self.categories.get("Medicina").get(current_profissional).servicos.get(service_name).has_key(utente)):
                        self.categories.get("Medicina").get(current_profissional).servicos.get(service_name).insert(utente, SinglyLinkedList())
                    # marca em cada profissional de medicina                                          
                    self.categories.get("Medicina").get(current_profissional).servicos.get(service_name).get(utente).insert_last(current_service)
                    # # marca em cada profissional de medicina
                    # self.categories.get("Medicina").get(current_profissional).servicos.get(service_name).insert(utente, current_service)
            # Enfermagem
            if list_profissionais_enfermagem is not None:
                it_p = list_profissionais_enfermagem.iterator()
                while it_p.has_next():
                    current_profissional = it_p.next()
                    #existe key com nome do utente?
                    if not(self.categories.get("Enfermagem").get(current_profissional).servicos.get(service_name).has_key(utente)):
                        self.categories.get("Enfermagem").get(current_profissional).servicos.get(service_name).insert(utente, SinglyLinkedList())
                    # marca em cada profissional de Enfermagem                                          
                    self.categories.get("Enfermagem").get(current_profissional).servicos.get(service_name).get(utente).insert_last(current_service)
                    # # marca em cada profissional de enfermagem
                    # self.categories.get("Enfermagem").get(current_profissional).servicos.get(service_name).insert(utente, current_service)
            # Auxiliar
            if list_profissionais_auxiliar is not None:
                it_p = list_profissionais_auxiliar.iterator()
                while it_p.has_next():
                    current_profissional = it_p.next()
                    #existe key com nome do utente?
                    if not(self.categories.get("Auxiliar").get(current_profissional).servicos.get(service_name).has_key(utente)):
                        self.categories.get("Auxiliar").get(current_profissional).servicos.get(service_name).insert(utente, SinglyLinkedList())
                    # marca em cada profissional de Auxiliar                                          
                    self.categories.get("Auxiliar").get(current_profissional).servicos.get(service_name).get(utente).insert_last(current_service)
                    # # marca em cada profissional de auxiliar
                    # self.categories.get("Auxiliar").get(current_profissional).servicos.get(service_name).insert(utente, current_service)


    def desmarcar_cuidado_utente(self, utente):
        # For each category service
        for service_category in ["Consulta", "PequenaCirurgia", "Enfermagem"]:
            # lista com os servicos de uma service_category
            list_service = self.utente_universe.get(utente).servicos.get(service_category)
            #Se essa lista nao estiver vazia
            if not(list_service.is_empty()):
                # for each servico de uma categoria de servico
                it = list_service.iterator()
                while it.has_next():
                    current_service = it.next()
                    # lista de profissionais de cada categoria por categoria de servico
                    if service_category == "Consulta":
                        list_profissionais_medicina = current_service.profissionais.get("Medicina")
                    elif service_category == "PequenaCirurgia":
                        list_profissionais_medicina = current_service.profissionais.get("Medicina")
                        list_profissionais_enfermagem = current_service.profissionais.get("Enfermagem")
                        list_profissionais_auxiliar = current_service.profissionais.get("Auxiliar")
                    elif service_category == "Enfermagem":
                        list_profissionais_enfermagem = current_service.profissionais.get("Enfermagem")
                        list_profissionais_auxiliar = current_service.profissionais.get("Auxiliar")

                if service_category in ["Consulta", "PequenaCirurgia"]:
                    # se a lista de profissinal nao estiver vazia
                    if not(list_profissionais_medicina.is_empty()):
                        # Para cara nome de profissional
                        it = list_profissionais_medicina.iterator()
                        while it.has_next():
                            current_profissional = it.next()
                            # remove o servico do profissional
                            self.categories.get("Medicina").get(current_profissional).servicos.get(service_category).remove(utente)

                if service_category in ["PequenaCirurgia", "Enfermagem"]:                    
                    # se a lista de profissinal nao estiver vazia
                    if not(list_profissionais_enfermagem.is_empty()):
                        # Para cara nome de profissional
                        it = list_profissionais_enfermagem.iterator()
                        while it.has_next():
                            current_profissional = it.next()
                            # remove o servico do profissional
                            self.categories.get("Enfermagem").get(current_profissional).servicos.get(service_category).remove(utente)

                    # se a lista de profissinal nao estiver vazia
                    if not(list_profissionais_auxiliar.is_empty()):
                        # Para cara nome de profissional
                        it = list_profissionais_auxiliar.iterator()
                        while it.has_next():
                            current_profissional = it.next()
                            # remove o servico do profissional
                            self.categories.get("Auxiliar").get(current_profissional).servicos.get(service_category).remove(utente)

               
            
            
            #deleto toda a lista de servicos de uma categoria de servico do utente 
            self.utente_universe.get(utente).servicos.get(service_category).make_empty()

            # lista para ter as posicoes contendo servicos com o utente
            list_positions = SinglyLinkedList()
            idx = -1
            # por cada servico
            it = self.servicos.get(service_category).iterator()
            while it.has_next():
                current_service = it.next()
                idx += 1
                # se o servico tiver o utente salva o idx do servico            
                if current_service.utente == utente:
                    list_positions.insert_last(idx)
            # para cada idx
            it = list_positions.iterator()
            while it.has_next():
                current_idx = it.next()
                # remove o servico do idx (idx dos servicos do utente)
                self.servicos.get(service_category).remove(current_idx)



    def listar_cuidados_utente(self, utente):
        list_cuidados_final = SinglyLinkedList()
        #
        list_services_category = self.servicos_list_ordered
        # ["Consulta", "PequenaCirurgia", "Enfermagem"]
        it = list_services_category.iterator()
        while it.has_next():
            service_category = it.next()
            # lista com os servicoes de uma categoria de servicos
            list_services = self.utente_universe.get(utente).servicos.get(service_category)

            

            # por cada servico dentro de uma categoria de servico
            it_s = list_services.iterator()
            while it_s.has_next():
                list_profissionais_medicina = None
                list_profissionais_enfermagem = None
                list_profissionais_auxiliar = None


                current_service = it_s.next()
                if current_service.name == "Consulta":
                    list_profissionais_medicina = current_service.profissionais.get("Medicina")
                elif current_service.name == "PequenaCirurgia":
                    list_profissionais_medicina = current_service.profissionais.get("Medicina")
                    list_profissionais_enfermagem = current_service.profissionais.get("Enfermagem")
                    list_profissionais_auxiliar = current_service.profissionais.get("Auxiliar")
                elif current_service.name == "Enfermagem":
                    list_profissionais_enfermagem = current_service.profissionais.get("Enfermagem")
                    list_profissionais_auxiliar = current_service.profissionais.get("Auxiliar")

                if list_profissionais_medicina is not None and list_profissionais_medicina.size() > 0:
                    list_profissionais_medicina_size = list_profissionais_medicina.size()
                    medicina_array = (list_profissionais_medicina_size * ctypes.py_object)() # Array of pointers
                    idx = -1
                    it_p = list_profissionais_medicina.iterator()
                    while it_p.has_next():
                        current_item = it_p.next()
                        idx += 1
                        medicina_array[idx] = current_item
                    self.quicksort(medicina_array, 0, idx, self.comp_strings)
                    for i in range(list_profissionais_medicina_size):
                        list_cuidados_final.insert_last(f"{service_category} Medicina {medicina_array[i]}")

                if list_profissionais_enfermagem is not None and list_profissionais_enfermagem.size() > 0:
                    list_profissionais_enfermagem_size = list_profissionais_enfermagem.size()
                    enfermagem_array = (list_profissionais_enfermagem_size * ctypes.py_object)() # Array of pointers
                    idx = -1
                    it_p = list_profissionais_enfermagem.iterator()
                    while it_p.has_next():
                        current_item = it_p.next()
                        idx += 1
                        enfermagem_array[idx] = current_item
                    self.quicksort(enfermagem_array, 0, idx, self.comp_strings)
                    for i in range(list_profissionais_enfermagem_size):
                        list_cuidados_final.insert_last(f"{service_category} Enfermagem {enfermagem_array[i]}")

                if list_profissionais_auxiliar is not None and list_profissionais_auxiliar.size() > 0:
                    list_profissionais_auxiliar_size = list_profissionais_auxiliar.size()
                    auxiliar_array = (list_profissionais_auxiliar_size * ctypes.py_object)() # Array of pointers
                    idx = -1
                    it_p = list_profissionais_auxiliar.iterator()
                    while it_p.has_next():
                        current_item = it_p.next()
                        idx += 1
                        auxiliar_array[idx] = current_item
                    self.quicksort(auxiliar_array, 0, idx, self.comp_strings)
                    for i in range(list_profissionais_auxiliar_size):
                        list_cuidados_final.insert_last(f"{service_category} Auxiliar {auxiliar_array[i]}")

        return list_cuidados_final


    def listar_cuidados_familia(self, family_name):
        # lsit that will be returned
        list_family = SinglyLinkedList()
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
        if len(jovens_array) > 0:
            idx = -1
            it = list_jovens.iterator()
            while it.has_next():
                current_item = it.next()
                idx += 1
                jovens_array[idx] = current_item
            self.quicksort(jovens_array, 0, idx, self.comp_strings)
        # Adultos
        if len(adultos_array) > 0:
            idx = -1
            it = list_adultos.iterator()
            while it.has_next():
                current_item = it.next()
                idx += 1
                adultos_array[idx] = current_item
            self.quicksort(adultos_array, 0, idx, self.comp_strings)
        # Idosos
        if len(idosos_array) > 0:
            idx = -1
            it = list_idosos.iterator()
            while it.has_next():
                current_item = it.next()
                idx += 1
                idosos_array[idx] = current_item
            self.quicksort(idosos_array, 0, idx, self.comp_strings)
        # Print the Jovem-Adulto-Idoso order for the Family
        if len(jovens_array) > 0:
            for j in range(list_jovens_size):
                if family_name == self.utente_universe.get(jovens_array[j]).familia_associada:
                    utente_name = jovens_array[j]
                    list_service = self.listar_cuidados_utente(utente_name)
                    it_s = list_service.iterator()
                    while it_s.has_next():
                        current_item = it_s.next()
                        list_family.insert_last(f"{utente_name} {current_item}")
                    # print(f"Jovem {jovens_array[j]}")
                    #list_family.insert_last(f"Jovem {jovens_array[j]}")

        if len(adultos_array) > 0:
            for j in range(list_adultos_size):
                if family_name == self.utente_universe.get(adultos_array[j]).familia_associada:
                    utente_name = adultos_array[j]
                    list_service = self.listar_cuidados_utente(utente_name)
                    it_s = list_service.iterator()
                    while it_s.has_next():
                        current_item = it_s.next()
                        list_family.insert_last(f"{utente_name} {current_item}")
                    # print(f"Adulto {adultos_array[j]}")
                    #list_family.insert_last(f"Adulto {adultos_array[j]}")
        if len(idosos_array) > 0:
            for j in range(list_idosos_size):
                if family_name == self.utente_universe.get(idosos_array[j]).familia_associada:
                    utente_name = idosos_array[j]
                    list_service = self.listar_cuidados_utente(utente_name)
                    it_s = list_service.iterator()
                    while it_s.has_next():
                        current_item = it_s.next()
                        list_family.insert_last(f"{utente_name} {current_item}")
                    #print(f"Idoso {idosos_array[j]}")
                    #list_family.insert_last(f"Idoso {idosos_array[j]}")

        return list_family


    def listar_marcados_profissional(self, name, category):
        list_final = SinglyLinkedList()
        list_consulta = SinglyLinkedList()
        list_pequenacirurgia = SinglyLinkedList()
        list_enfermagem = SinglyLinkedList()
        if category == "Medicina":
            list_consulta = self.categories.get(category).get(name).servicos.get("Consulta").keys()
            list_pequenacirurgia = self.categories.get(category).get(name).servicos.get("PequenaCirurgia").keys()
        elif category == "Enfermagem":
            list_pequenacirurgia = self.categories.get(category).get(name).servicos.get("PequenaCirurgia").keys()
            list_enfermagem = self.categories.get(category).get(name).servicos.get("Enfermagem").keys()
        elif category == "Auxiliar":
            list_pequenacirurgia = self.categories.get(category).get(name).servicos.get("PequenaCirurgia").keys()
            list_enfermagem = self.categories.get(category).get(name).servicos.get("Enfermagem").keys()
        
        list_consulta_size = list_consulta.size()
        consulta_array = (list_consulta_size * ctypes.py_object)() # Array of pointers
        
        list_pequenacirurgia_size = list_pequenacirurgia.size()
        pequenacirurgia_array = (list_pequenacirurgia_size * ctypes.py_object)() # Array of pointers
        
        list_enfermagem_size = list_enfermagem.size()
        enfermagem_array = (list_enfermagem_size * ctypes.py_object)() # Array of pointers

        if len(consulta_array) > 0:
            idx = -1
            it = list_consulta.iterator()
            while it.has_next():
                current_item = it.next()
                idx += 1
                consulta_array[idx] = current_item
            self.quicksort(consulta_array, 0, idx, self.comp_strings)
            
            for i in range(len(consulta_array)):
                multiplicador = self.categories.get(category).get(name).servicos.get("Consulta").get(consulta_array[i]).size()
                for j in range(multiplicador):
                    list_final.insert_last(f"Consulta {consulta_array[i]}")

        if len(pequenacirurgia_array) > 0:
            idx = -1
            it = list_pequenacirurgia.iterator()
            while it.has_next():
                current_item = it.next()
                idx += 1
                pequenacirurgia_array[idx] = current_item
            self.quicksort(pequenacirurgia_array, 0, idx, self.comp_strings)

            for i in range(len(pequenacirurgia_array)):
                multiplicador = self.categories.get(category).get(name).servicos.get("PequenaCirurgia").get(pequenacirurgia_array[i]).size() 
                for j in range(multiplicador):
                    list_final.insert_last(f"PequenaCirurgia {pequenacirurgia_array[j]}")

        if len(enfermagem_array) > 0:
            idx = -1
            it = list_enfermagem.iterator()
            while it.has_next():
                current_item = it.next()
                idx += 1
                enfermagem_array[idx] = current_item
            self.quicksort(enfermagem_array, 0 , idx, self.comp_strings)

            for i in range(len(enfermagem_array)):
                multiplicador = self.categories.get(category).get(name).servicos.get("Enfermagem").get(enfermagem_array[i]).size() 
                for j in range(multiplicador):
                    list_final.insert_last(f"Enfermagem {enfermagem_array[i]}")

        return list_final

        
    def listar_marcados_service(self, service):
        list_final = SinglyLinkedList()
        
        categories = SinglyLinkedList()
        if service == "Consulta":
            categories.insert_last("Medicina")
        elif service == "PequenaCirurgia":
            categories.insert_last("Medicina")
            categories.insert_last("Enfermagem")
            categories.insert_last("Auxiliar")
        elif service == "Enfermagem":
            categories.insert_last("Enfermagem")
            categories.insert_last("Auxiliar")

        # ["Medicina"] or ["Medicina", "Enfermagem", "Auxiliar"] or ["Enfermagem", "Auxiliar"] 
        it = categories.iterator()
        while it.has_next():
            current_category = it.next()

            list_profissionais = self.categories.get(current_category).keys()
            list_profissionais_size = list_profissionais.size()
            profissionais_array = (list_profissionais_size * ctypes.py_object)() # Array of pointers

            if len(profissionais_array) > 0:
                idx = -1
                it_p = list_profissionais.iterator()
                while it_p.has_next():
                    current_profissional = it_p.next()
                    idx += 1
                    profissionais_array[idx] = current_profissional
                self.quicksort(profissionais_array, 0 , idx, self.comp_strings)

                for j in range(len(profissionais_array)):
                    #if self.categories.get(current_category).get(profissionais_array[j]).servicos.get(service).size() > 0:
                    list_utentes = self.categories.get(current_category).get(profissionais_array[j]).servicos.get(service).keys()
                    list_utentes_size = list_utentes.size()
                    utentes_array = (list_utentes_size * ctypes.py_object)() # Array of pointers

                    if len(utentes_array) > 0:
                        idx = -1
                        it_u = list_utentes.iterator()
                        while it_u.has_next():
                            current_utente = it_u.next()
                            idx += 1
                            utentes_array[idx] = current_utente
                        self.quicksort(utentes_array, 0, idx, self.comp_strings)
                        for i in range(len(utentes_array)):
                            list_final.insert_last(f"{current_category} {profissionais_array[j]} {utentes_array[i]}")

        return list_final

        


            

            







# -----------------------------------quicksort ---------------------------    

    def comp_strings(self, a, b):
        for i in range(len(a)):
            if i >= (len(b)-1):
                return False
            elif a[i] < b[i]:
                return True
            elif a[i] > b[i]:
                return False
        return True

    def quicksort(self, l, left, right, comp):
        i = left
        j = right
        pivot = l[int((i+j)/2)]
        while i <= j:
            while comp(l[i], pivot) and i<len(l):
                i += 1
            while comp(pivot, l[j]) and j>-1:
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