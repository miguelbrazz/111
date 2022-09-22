# ExemploDicionario.py

# O que é um dicionário no python?
# como iniciar um dicionário
# como colocar dados em um dicionário
# como interagir com um dicionário - for
#   .items()
#   .values()
#   .keys()
# como alterar dados de um dicionário
# como deletar dados de um dicionário

# dicionario = { chave : valor} 

'''
Precisamos criar uma agenda para armazenar o nome e o telefone das pessoas.
Algoritmo:
1- Definir o dicionário para armazenar os dados
2- Inserir os dados no dicionário
    - digitar nome 
    - digitar telefone
    - guardar nome e telefone na agenda
3- Aleterar o telefone de alguém
    - ler um nome
    - localiza na agenda
    - le o novo número
4- Apagar o telefone de alguém
    - ler o nome
    - localizar na agenda
    - deletar da agenda
'''



def inserir():
    while True:
        print('Inserir dados na agenda [Enter] - finaliza')
        nome = input('Nome: ')
        if nome:
            telefone = input('Telefone: ')
            agenda[nome] = telefone

            print(agenda)
        else:
            break

def alterar():
    while True:
        print('Alterar Telefones da agenda. [Enter] - finaliza')
        nome = input('Nome para alterar: ')
        if nome:
            if nome in agenda:
                novo_telefone = input('Novo Número: ')
                agenda[nome] = novo_telefone
            else:
                input('Nome não existe na agenda. [Enter]')
        else: break

def excluir():
    ''' Esta função tem por objetivo ler o nome, verificar se este nome está cadastrado 
        na agenda, e estando cadastrado, exclui-lo.
    '''
    while True:
        print('Excluir Telefones da agenda. [Enter] - finaliza')
        nome_para_excluir = input('Nome para excluir: ')
        if nome_para_excluir:  # se existe algum caracter na variável
            if nome_para_excluir in agenda:
                del(agenda[nome_para_excluir])
            else:
                input('Nome não localizado na agenda. [Enter]')
        else: break   # quando for digitado apenas ENTER, sem nenhum caracter no input

# Definindo a agenda - dicionário
#agenda = {}
agenda = {'ana':['1111'],'maria':['2222'],'pedro':['3333'],'julio':['4444']}


def continua_laco():
    resposta = input('Continuar na agenda? s/n: ')
    if resposta != 's':
        return False
    return True

###############################
#  Programa principal
while continua_laco():
    inserir()
    alterar()
    excluir()
    print(agenda)

'''
print('Agenda Completa - Dicionário:\n',agenda)
print('\nUsando .keys() - o nome')
for pessoa in agenda.keys():
    print(pessoa)

print('\nUsando .values() - o telefone')
for telef in agenda.values():
    print(telef)

print('\nUsando .items() - chave e valor')
for dado in agenda.items():
    print(dado)
'''

print('Finalizando....')






