from controllers.controller import Controller
from aed_ds.lists.singly_linked_list import SinglyLinkedList
# Comand Line Interface 
class CLI:
    def __init__(self):
        controller = Controller()

        while True:
            line = input()

            if line == "":
                exit()

            commands = line.split(" ") 

            # Registrar Profissional
            if commands[0] == "RP":
                category = commands[1]
                name = commands[2]
                if controller.has_category(category):
                    if not(controller.has_profissional_category(name, category)):
                        controller.registrar_profissional(name, category)
                        print("Profissional registrado com sucesso")
                    else:
                        print("Profissinal existente.")
                else:
                    print("Categoria Inexistente.")
                

            # Registrar Utente
            elif commands[0] == "RU":
                name = commands[1]
                faixa_etaria = commands[2]
                if not(controller.has_utente(name)):
                    if controller.has_faixa_etaria(faixa_etaria):
                        controller.registrar_utente(name, faixa_etaria)
                        print("Utente registrado com sucesso.")
                    else:
                        print("Faixa etaria inexistente.")
                else:
                    print("Utente existente.")
                

            # Registrar Familia
            elif commands[0] == "RF":
                family_name = commands[1]
                if not(controller.has_that_family(family_name)):
                    controller.registrar_familia(family_name)
                    print("Família registrada com sucesso.")
                else:
                    print("Família existente.")
                

            # Associar Utente de Familia
            elif commands[0] == "AF":
                name = commands[1]
                family_name = commands[2]
                if controller.has_utente(name):
                    if controller.has_that_family(family_name):
                        if not(controller.utente_has_family(name)):
                            controller.associar_utente_familia(name, family_name)                            
                            print("Utente associado a família.")
                        else:
                            print("Utente percente a família.")
                    else:
                        print("Família inexistente.")
                else:
                    print("Utente inexistente.")
                 

            # Disassoiar Utente a Familia
            elif commands[0] == "DF":
                name = commands[1]
                if controller.has_utente(name):
                    if controller.utente_has_family(name):
                        controller.desassociar_utente_familia(name)
                        print("Utente desassociado da família.")
                    else:
                        print("Utente não pertence a família.")
                else:
                    print("Utente inexistente.")
                

            # Listar Profissionais
            elif commands[0] == "LP":
                if controller.has_profissional():
                    list_profissionais = controller.listar_profissionais()
                    it = list_profissionais.iterator()
                    while it.has_next():
                        current_item =  it.next()
                        print(f"{current_item}.")                    
                else:
                    print("Sem profissional registrado.")
                

            # Listar Utentes
            elif commands[0] == "LU":
                if controller.there_are_utentes():                    
                    list_utentes = controller.listar_utentes()
                    it = list_utentes.iterator()
                    while it.has_next():
                        current_item = it.next()
                        print(f"{current_item}.")
                else:
                    print("Sem utentes registrados.")
                # controller.listar_utentes()

            # Listar Familias
            elif commands[0] == "LF":
                if controller.has_family():
                    list_families = controller.listar_familias()
                    it = list_families.iterator()
                    while it.has_next():
                        current_item = it.next()
                        print(f"{current_item}.")
                else:
                    print("Sem famílias registradas.")

            # Mostrar Familia
            elif commands[0] == "MF":
                family_name = commands[1]
                if controller.has_that_family(family_name):
                    list_family = controller.mostrar_familia(family_name)
                    it = list_family.iterator()
                    while it.has_next():
                        current_item = it.next()
                        print(f"{current_item}.")
                else:
                    print("Família inexistente.")
                controller.mostrar_familia(family_name)


            # Marcar Cuidados a Utente
            elif commands[0] == "MC":
                service_list = SinglyLinkedList()
                name = commands[1]
                if controller.has_utente(name):
                    service = None
                    while True:
                        line = input()
                        if line == "":
                            if service is not None:
                                service_list.insert_last(service)
                            break
                        commands = line.split(" ")
                        
                        
                        if len(commands) == 1:
                            service_name = commands[0]
                            if service is not None:
                                service_list.insert_last(service)
                                service = None
                            if controller.has_service(service_name):
                                service = controller.create_service(service_name, name)
                            else:
                                print("Serviço Inexistente.")
                        else:                            
                            if service == None:
                                print("Serviço Inexistente.")
                                break
                            categoria = commands[0]
                            profissional = commands[1]
                            if controller.has_category(categoria):
                                if controller.has_profissional_category(profissional, categoria):
                                    if controller.service_has_category(service_name, categoria):
                                        controller.fill_service(service, profissional, categoria)
                                    else:
                                        print("Categoria inválida.")
                                else:
                                    print("Profissinal de saude inexistente.")
                            else:
                                print("Categoria inexistente.")

                    if controller.has_valid_sequence(service_list):
                        controller.marcar_cuidados_utente(service_list, name)
                        print("Cuidados marcados com sucesso.")
                    else:
                        print("Sequencia inválida.")
                else:
                    print("Utente Inexistente.")

            

            # Cancelar Cuidados Marcados a Utente
            elif commands[0] == "CC":
                name = commands[1]
                if controller.has_utente(name):
                    if controller.has_service_utente(name):
                       controller.desmarcar_cuidado_utente(name)
                       print("Cuidados de saúde desmacados com sucesso.")
                    else:
                        print("Utente sem cuidados de saúde marcados.")
                else:
                    print("Utente inexistente.")

            # Listar Cuidados Marcados a Utente
            elif commands[0] == "LCU":
                name = commands[1]
                if controller.has_utente(name):
                    if controller.has_service_utente(name):
                        list_services = controller.listar_cuidados_utente(name)
                        it = list_services.iterator()
                        while it.has_next():
                            current_item = it.next()
                            print(f"{current_item}.")
                    else:
                        print("Utente sem cuidados de saúde marcados.")
                else:
                    print("Utente inexistente.")

            # Listar Cuidados Marcados a Familia
            elif commands[0] == "LCF":
                family_name = commands[1]
                if controller.has_that_family(family_name):
                    if controller.has_service_family(family_name):
                        list_services = controller.listar_cuidados_familia(family_name)
                        it = list_services.iterator()
                        while it.has_next():
                            current_item = it.next()
                            print(f"{current_item}.")
                    else:
                        print("Família sem cuidados de saúde marcados.")
                else:
                    print("Família inexistete.")

            # Listar Servicos Marcados a Profissionais
            elif commands[0] == "LSP":
                category = commands[1]
                name = commands[2]
                if controller.has_profissional_category(name, category):
                    if controller.has_service_profissional(name, category):
                        list_services = controller.listar_marcados_profissional(name, category)
                        it = list_services.iterator()
                        while it.has_next():
                            current_item = it.next()
                            print(f"{current_item}.")
                    else:
                        print("Profissional de saúde sem marcações.")
                else:
                    print("Profissional de saúde inexistente.")
                

            # Listar Marcacoes por tipo de Servico
            elif commands[0] == "LMS":
                service = commands[1]
                if controller.has_service(service):
                    if controller.are_there_service(service):
                        list_service = controller.listar_marcados_service(service)
                        it = list_service.iterator()
                        while it.has_next():
                            current_item = it.next()
                            print(f"{current_item}.")
                    else:
                        print("Serviço sem marcações.")
                else:
                    print("Serviço inexistente.")

                        
            else:
                print("Instrução inválida.")