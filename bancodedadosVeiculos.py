import json
DiconarioDados = {}


# CADASTRO EM SE:
def cadasveiculo():
    LerDadosJson()
    while True:
        placa = input('Número da Placa')
        tipo = cadastipo()
        motorista = input('DIGITE O NOME DO MOTORISTA>>>')

        veiculos = {

            'placa': placa,
            'tipo': tipo,
            'motorista': motorista
        }
        DiconarioDados[placa] = veiculos

        gravardados()

        escolha = input('QUER CADASTRAR OUTRO SIM OU NÃO?').lower()
        if escolha == 'nao':
            break

#GRAVAR DADOS NO ARQUIVO JSON:
def gravardados():
    with open('BaseDadosVeiculos.json', 'w') as arqJson:
        json.dump(DiconarioDados, arqJson, indent=3)
# LER DADOS NO ARQUIVO JSON / E CHECAR SE JÁ EXISTEM:
def LerDadosJson():
    with open('BaseDadosVeiculos.json', 'r+') as arqjson:
        global DiconarioDados
        DiconarioDados = json.load(arqjson)
# FUNÇAO QUE CHECA OS VALORES PARA CARRO E MOTO:
def cadastipo():
    x = None
    op = int(input('O SEU VEICULO É UM CARRO OU UMA MOTO?'
                   '\n [1]-CARRO'
                   '\n [2]-MOTO'
                   '\n >>>'))
    if op == 1:
        x = 'CARRO'
    elif op == 2:
        x = 'MOTO'
    else:
        print('valor invalido')
        return cadastipo()
    return x
# CHECAR SE A PLACA EXISTE:
def checarplaca():
    pass
cadasveiculo()