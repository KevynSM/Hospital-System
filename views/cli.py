from controllers.controller import Controller
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
                    print("Familia registrada com sucesso.")
                else:
                    print("Familia existente.")
                

            # Associar Utente de Familia
            elif commands[0] == "AF":
                name = commands[1]
                family_name = commands[2]
                if controller.has_utente(name):
                    if controller.has_that_family(family_name):
                        if not(controller.utente_has_family(name)):
                            controller.associar_utente_familia(name, family_name)                            
                            print("Utente associado a familia.")
                        else:
                            print("Utente percente a familia.")
                    else:
                        print("Familia inexistente.")
                else:
                    print("Utente inexistente.")
                 

            # Disassoiar Utente a Familia
            elif commands[0] == "DF":
                name = commands[1]
                if controller.has_utente(name):
                    if controller.utente_has_family(name):
                        controller.desassociar_utente_familia(name)
                        print("Utente desassociado da familia.")
                    else:
                        print("Utente nao pertence a familia.")
                else:
                    print("Utente inexistente.")
                

            # Listar Profissionais
            elif commands[0] == "LP":
                if controller.has_profissional():
                    list_profissionais = controller.listar_profissionais()
                    it = list_profissionais.iterator()
                    while it.has_next():
                        current_item =  it.next()
                        print(current_item)                    
                else:
                    print("Sem profissional registrado.")
                

            # Listar Utentes
            elif commands[0] == "LU":
                controller.listar_utentes()

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
                controller.mostrar_familia(family_name)

            # Marcar Cuidados a Utente
            elif commands[0] == "MC":
                name = commands[1]
                if controller.has_utente(name):
                    while True:
                        servico = input()
                        if servico == "":
                            break
                        if controller.has_servico(servico):
                            new_line = input()
                            categoria_profissinal = new_line.split(" ")
                            categoria = categoria_profissinal[0]
                            profissional = categoria_profissinal[1]
                            if controller.has_category(categoria):
                                if controller.has_profissional_category(profissional, categoria):
                                    # marcar cuidado a utente
                                    pass
                                else:
                                    print("Profissinal de saude inexistente.")
                            else:
                                print("Categoria inexistente.")
                                break

                        else:
                            print("Servico Inexistente.")
                            break


                else:
                    print("Utente Inexistente.")

            # Cancelar Cuidados Marcados a Utente
            elif commands[0] == "CC":
                name = commands[1]
                pass

            # Listar Cuidados Marcados a Utente
            elif commands[0] == "LCU":
                name = commands[1]
                pass

            # Listar Cuidados Marcados a Familia
            elif commands[0] == "LCF":
                family_name = commands[1]
                pass

            # Listar Servicos Marcados a Profissionais
            elif commands[0] == "LSP":
                category = commands[1]
                name = commands[2]
                pass

            # Listar Marcacoes por tipo de Servico
            elif commands[0] == "LMS":
                service = commands[1]
                pass

            # Gravar
            elif commands[0] == "G":
                file = commands[1]
                pass

            # Ler
            elif commands[0] == "L":
                file = commands[1]
                pass
            
            else:
                print("Instrução invalida.")