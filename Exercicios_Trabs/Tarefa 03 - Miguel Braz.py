
dicionarioSala = {}

def cadastrarSala():
    while True:
        print('Inserir dados na sala [Enter] - Finaliza')
        sala = input('Sala: ')
        if sala:
            andar = input('Andar: ')
            dicionarioSala[sala] = andar
            alunos = input('Quantidade de alunos: ')
            if alunos:
                computadores = input('Quantidade de computadores: ')
                dicionarioSala[alunos] = computadores

                print(dicionarioSala)
            else:
                break

###############################################################
def relatorioSalas():
    for saladigitada in dicionarioSala:
        print(dicionarioSala)

###############################################################
def alterarSala():
     while True:
        print('Alterar dados da sala. [Enter] - finaliza')
        nome = input('alterar: ')
        if sala:
            if sala in dicionarioSala:
                novo_dado = input('Novo Dado: ')
                dicionarioSala[sala] = novo_dado
            else:
                input('Dado não existe. [Enter]')
        else: break

################################################################
def excluir():
    while True:
        print('Excluir Dados da sala. [Enter] - finaliza')
        dado_p_excluir = input('Dados a ser excluído: ')
        if dado_p_excluir:
            if nome_p_excluir in dicionarioSala:
                del(dicionarioSala[dado_p_excluir])
            else:
                input('Dados não localizado. [Enter]')
        else: break

################################################################
def continuar():
    resposta = input('Deseja continuar? s/n: ')
    if resposta != 's':
        return False
    return False

#############################

while continuar():
    cadastrarSala()
    relatorioSalas()
    alterarSala()
    excluir()
    print(dicionarioSala)

'''
print('Sala Completa - Dicionário:\n',dicionarioSala)
print('\nUsando .keys() - o nome')
for pessoa in agenda.keys():
    print(sala)

print('\nUsando .values() - o telefone')
for telef in dicionarioSala.values():
    print(andar)

print('\nUsando .items() - chave e valor')
for dado in dicionarioSala.items():
    print(alunos,computadores)
'''

print('Finalizando....')



