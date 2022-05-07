import bancodedadosVeiculos
def menuVeiculo():
    print('----------------MENU--------------')
    print('1 - Cadastrar Veiculo')
    print('2 - Buscar Veiculo por Placa')
    print('3 - Adicionar motorista ao veiculo')
    print('4 - Remover motorista do veiculo')
    print('5 - Listar veiculos com motoristas')
    print('6 - Listar veiculos sem motoristas')
    print('7 - Remover Veiculo')
    print('8 - SAIR')
    print('-'*35)
    escolha = int(input(""))

    if escolha == 1:
        bancodedadosVeiculos.cadasveiculo()
    elif escolha == 2:
        pass
    elif escolha == 3:
        pass
    elif escolha == 5:
        pass
    elif escolha == 6:
        pass
    elif escolha == 7:
        pass
    elif escolha == 8:
        pass
    else:
        print("Opção inválida!")