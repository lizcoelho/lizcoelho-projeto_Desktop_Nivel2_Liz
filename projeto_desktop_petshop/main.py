
# Importando as classes
from models.cliente import Cliente
from models.pet import Pet
from models.atendente import Atendente
from models.gerente import Gerente
from models.banho import Banho
from models.tosa import Tosa
from models.consulta import Consulta
from models.agendamento import Agendamento
from models.petshop import PetShop
from models.venda import Venda
from models.dinheiro import Dinheiro
from models.pix import Pix
from models.cartao import Cartao
from models.sistema_pagamento import SistemaPagamento

# Listas para armazenar os dados
clientes = []
agendamentos = []
vendas = []

# Funcionários
funcionarios = [
    Atendente("Maria", 2000),
    Gerente("Carlos", 4000)
]

# Serviços
servicos = [
    Banho(50),
    Tosa(70),
    Consulta(120)
]

# Objetos do sistema
petshop = PetShop()
sistema = SistemaPagamento()

# Menu principal
while True:
    print("\n========== PET SHOP ==========")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Cadastrar pet")
    print("4 - Listar pets")
    print("5 - Listar funcionários")
    print("6 - Consultar serviços")
    print("7 - Realizar agendamento")
    print("8 - Realizar venda e pagamento")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "0":
        print("\nEncerrando o sistema...")
        break

    elif opcao == "1":
        print("\n--- CADASTRAR CLIENTE ---")

        nome = input("Digite o nome do cliente: ")

        cliente = Cliente(nome)
        clientes.append(cliente)

        print("Cliente cadastrado com sucesso!")

    elif opcao == "2":
        print("\n--- LISTA DE CLIENTES ---")

        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in clientes:
                print(cliente)

    elif opcao == "3":
        print("\n--- CADASTRAR PET ---")

        if len(clientes) == 0:
            print("Cadastre um cliente primeiro.")
        else:
            print("\nClientes cadastrados:")

            for i, cliente in enumerate(clientes):
                print(f"{i + 1} - {cliente.nome}")

            escolha = int(input("Escolha o número do cliente: "))

            if escolha >= 1 and escolha <= len(clientes):
                cliente = clientes[escolha - 1]

                nome_pet = input("Digite o nome do pet: ")
                especie = input("Digite a espécie do pet: ")

                pet = Pet(nome_pet, especie)
                cliente.adicionar_pet(pet)

                print("Pet cadastrado com sucesso!")
            else:
                print("Cliente inválido!")

    elif opcao == "4":
        print("\n--- LISTA DE PETS ---")

        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in clientes:
                print(f"\n{cliente}")

                if len(cliente.pets) == 0:
                    print("Nenhum pet cadastrado.")
                else:
                    cliente.listar_pets()

    elif opcao == "5":
        print("\n--- LISTA DE FUNCIONÁRIOS ---")

        for funcionario in funcionarios:
            print(funcionario)

            if isinstance(funcionario, Atendente):
                funcionario.atender_cliente()

            elif isinstance(funcionario, Gerente):
                funcionario.gerenciar_petshop()

    elif opcao == "6":
        print("\n--- SERVIÇOS DISPONÍVEIS ---")

        for servico in servicos:
            print(servico)

    elif opcao == "7":
        print("\n--- REALIZAR AGENDAMENTO ---")

        if len(clientes) == 0:
            print("Cadastre um cliente primeiro.")

        else:
            print("\nClientes cadastrados:")

            for i, cliente in enumerate(clientes):
                print(f"{i + 1} - {cliente.nome}")

            escolha = int(input("Escolha o número do cliente: "))

            if escolha >= 1 and escolha <= len(clientes):
                cliente = clientes[escolha - 1]

                if len(cliente.pets) == 0:
                    print("Esse cliente não possui pets cadastrados.")

                else:
                    print("\nPets cadastrados:")

                    for i, pet in enumerate(cliente.pets):
                        print(f"{i + 1} - {pet}")

                    escolha_pet = int(input("Escolha o número do pet: "))

                    if escolha_pet >= 1 and escolha_pet <= len(cliente.pets):
                        pet = cliente.pets[escolha_pet - 1]

                        print("\nServiços disponíveis:")

                        for i, servico in enumerate(servicos):
                            print(f"{i + 1} - {servico}")

                        escolha_servico = int(input("Escolha o serviço: "))

                        if escolha_servico >= 1 and escolha_servico <= len(servicos):
                            servico = servicos[escolha_servico - 1]

                            data = input("Digite a data do agendamento: ")

                            agendamento = Agendamento(
                                cliente,
                                pet,
                                type(servico),
                                servico.preco,
                                data
                            )

                            agendamentos.append(agendamento)

                            atendente = funcionarios[0]

                            petshop.confirmar_agendamento(
                                agendamento,
                                atendente
                            )

                        else:
                            print("Serviço inválido!")

                    else:
                        print("Pet inválido!")

            else:
                print("Cliente inválido!")

    elif opcao == "8":
        print("\n--- REALIZAR VENDA E PAGAMENTO ---")

        if len(clientes) == 0:
            print("Cadastre um cliente primeiro.")

        else:
            print("\nClientes cadastrados:")

            for i, cliente in enumerate(clientes):
                print(f"{i + 1} - {cliente.nome}")

            escolha = int(input("Escolha o número do cliente: "))

            if escolha >= 1 and escolha <= len(clientes):
                cliente = clientes[escolha - 1]

                venda = Venda(cliente)

                while True:
                    print("\nServiços disponíveis:")

                    for i, servico in enumerate(servicos):
                        print(f"{i + 1} - {servico}")

                    escolha_servico = int(input("Escolha o serviço: "))

                    if escolha_servico >= 1 and escolha_servico <= len(servicos):
                        servico = servicos[escolha_servico - 1]

                        quantidade = int(input("Digite a quantidade: "))

                        venda.adicionar_item(
                            servico.nome,
                            quantidade,
                            servico.preco
                        )

                        print("Item adicionado à venda!")

                        continuar = input("Adicionar outro serviço? (s/n): ")

                        if continuar.lower() != "s":
                            break

                    else:
                        print("Serviço inválido!")

                if len(venda.itens) > 0:
                    print("\n--- RESUMO DA VENDA ---")
                    venda.exibir_venda()

                    print("\nFormas de pagamento:")
                    print("1 - Dinheiro")
                    print("2 - Pix")
                    print("3 - Cartão")

                    pagamento_escolhido = input("Escolha a forma de pagamento: ")

                    if pagamento_escolhido == "1":
                        pagamento = Dinheiro()

                    elif pagamento_escolhido == "2":
                        pagamento = Pix()

                    elif pagamento_escolhido == "3":
                        pagamento = Cartao()

                    else:
                        pagamento = None
                        print("Forma de pagamento inválida!")

                    if pagamento is not None:
                        sistema.processar_pagamento(venda, pagamento)
                        vendas.append(venda)
                        print("Venda realizada com sucesso!")

            else:
                print("Cliente inválido!")

    else:
        print("\nOpção inválida! Tente novamente.")
