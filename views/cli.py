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
                controller.registrar_profissional(category, name)

            # Registrar Utente
            elif commands[0] == "RU":
                name = commands[1]
                faixa_etaria = commands[2]
                controller.registrar_utente(name,faixa_etaria)

            # Registrar Familia
            elif commands[0] == "RF":
                family_name = commands[1]
                controller.registrar_familia(family_name)

            # Associar Utente de Familia
            elif commands[0] == "AF":
                name = commands[1]
                family_name = commands[2]
                controller.associar_utente_familia(name,family_name)

            # Disassoiar Utente a Familia
            elif commands[0] == "DF":
                name = commands[1]
                controller.desassociar_utente_familia(name)

            # Listar Profissionais
            elif commands[0] == " LP":                
                controller.listar_profissionais()

            # Listar Utentes
            elif commands[0] == "LU":
                controller.listar_utentes()

            # Listar Familias
            elif commands[0] == "LF":
                controller.listar_familias()

            # Mostrar Familia
            elif commands[0] == "MF":
                family_name = commands[1]
                controller.mostrar_familia(family_name)

            # Marcar Cuidados a Utente
            elif commands[0] == "MC":
                pass

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
                print("Invalid intruction")