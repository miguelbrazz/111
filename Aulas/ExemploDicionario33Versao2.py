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
5- Imprimir a agenda
'''

agenda = {'ivonei':['1111'], 'maria':['2222'], 'pedro': ['3333'],'aaa':['999991111','999992222','999993333']}
''' agenda tem como função armazenar os valores que estão dentro das chaves(chaves e valores) '''



def ler_telefone(telefones = []):
# lê o que está dentro dos parentêses, ou seja, os numeros telefonicos
    def entrar_outro_numero():
        resposta = input('Entrar outro número? s/n: ')
        if resposta.upper() == 'S':
#       devolve a string com todas as letras maiúsculas
            return True
        return False

    telefone = input('   Entre o Telefone: ')
    if len(telefone) == 9:
#   tem a função de deixar prosseguir só se o numero conter 9 digitos
        if telefone.isnumeric():
#       essa função pega o que há de numeros no dicionario
            telefones.append(telefone)
#           armazena os numeros telefonicos
            if entrar_outro_numero():
                return ler_telefone(telefones)
            else: 
                return telefones
        else:
            input('   Número deve conter apenas dígitos numéricos. [Enter] ')
    else:
        input('   Número deve ter 9 dígitos. [Enter] ')
    return ler_telefone()





def insere():
# está função tem por objetivo inserir na lista "insere" o que for digitado 
#    print('- - - Insere nome na Agenda - - -')
    print('Insere nome na Agenda'.center(35,'-'))
#   executa o que for digitado no centro dos demais caracteres

    while True:
        print('[Enter] finaliza o cadastro')
        nome = input('Nome: ')
        if nome: 
            if nome not in agenda:
                agenda[nome] = ler_telefone()
#               confere se o nome que foi digitado está na agenda 
            else: input('   Nome Já cadastrado na Agenda. [Enter] ')
        else:
            break




def alterar_nome_telefone():
# tem por objetivo alterar algum elemento contido no dicionario
    resposta = input(''' 
            --------------------------
            O que você deseja alterar:
            --------------------------
            1 - Nome
            2 - Telefone
            Escolha: ''')
    if resposta not in ('1','2'):
#   faz o usuário somente poder digitar os numeros "1" e "2"
        return alterar_nome_telefone
    return resposta




def alterar_nome(nome):
''' o objetivo dessa função é substituir um NOME no dicionario '''
    novo_nome = input('...[Enter] - Retorna\n...Digite o nome correto: ')
    if novo_nome:
        if novo_nome in agenda:
#       confere se o nome substituido já não consta no dicionario
            input('...Este nome já consta na agenda! ')
        else:
            agenda[novo_nome] = agenda[nome]
            del(agenda[nome])
#           deleta o antigo nome




def alterar_telefone(nome):
''' o objetivo dessa função é substituir um NUMERO no dicionario '''
    print('...Escolha o telefone: ')
    telefones = agenda[nome]
    for ind,fone in enumerate(telefones):
#   se indice for numeros cadastrados na agenda, mostra-los
        print(f'...{ind} - {fone}')
    escolha = int(input('   Escolha pelo indice: '))
    if escolha >= 0 and escolha <= len(telefones):
#   da continuidade ao programa se o que for digitado for numeros não negativos e com 9 caracteres(len)
        telefones.pop(escolha)
#   retorna o item presente no índice especificado. Este item também é removido da lista.
        agenda[nome] = ler_telefone(telefones)
print(agenda)




def alterar():
''' essa lista tem a função de alterar tanto o nome quanto o telefone '''
    print('Altera Agenda'.center(35,'-'))
    while True:
        print('[Enter] finaliza a alteração')
        nome = input('Nome para alterar: ')  # se for digitado enter. o conteúdo é nulo
        if nome:  # nome é válido
            if nome in agenda: # nome está na agenda?
#           consta se o NOME está no dicionario
                if alterar_nome_telefone() == '1': # Alterar Nome
                    alterar_nome(nome)
                else: 
                    alterar_telefone(nome)
#                   é executado se o usuario não digitar "1"
                print(agenda)
            else:
                input('Nome não consta na agenda. [Enter]')
        else:   # nome NÃO válido
            break





def excluir():
''' lista com função de deletar elementos da agenda '''
        print('Excluir'.center(35,'-'))
        nome = input('Nome para excluir: ')  
        if nome in agenda:
            confirma = input(f'...Confirma a exclusão {nome}? s/n: ')
            if confirma.upper() == 'S':
#           verifica se o que foi digitado são caracteres estão em LETRAS maiúsculas
                del(agenda[nome])
#               deleta na agenda o que foi digitado
                input('...Nome Excluido...[Enter]')
        else:
            input('Nome não consta na agenda. [Enter]')
        print(agenda)


def menu():
''' tem a função de gerenciar as demais listas '''
    resposta = input('''

+---------------------------------+
| Menu Principal                  |
+---------------------------------+
| 0 - Finalizar                   |
| 1 - Inserir Dados na Agenda     |
| 2 - Alterar Telefone            |
| 3 - Excluir Pessoa na Agenda    |
| 4 - Mostrar Agenda              |
+---------------------------------+
Escolha: ''')

    if resposta in ('0','1','2','3','4'):
#   da continuidade ao programa se o que estiver dentro dos parenteses for digitado
        return resposta # retorna ao menu principal
    input('Escolha incorreta. [Enter] - Tente Novamente.')
    return menu()



def imprime_agenda():
''' lista para exibir todos os itens da agenda '''
    print('Agenda'.center(35,'-'))
    for nome,fones in agenda.items():
        telefones = str(fones).strip("[]").replace("'","")
        print(f'  {nome.ljust(15,".")} - {telefones}')
#       não entendi o que faz :(




#####################################
# Programa Principal
#     
while True:
    escolha = menu()
    if escolha   == '1': # programa é encaminhado para lista "insere"
        insere()
    elif escolha == '2': # programa é encaminhado para lista "alterar"   
        alterar()
    elif escolha == '3': # programa é encaminhado para lista "excluir"
        excluir()
    elif escolha == '4': # programa é encaminhado para lista "imprime_agenda"
        imprime_agenda() 
    else: break

print('Fim')

# Miguel Braz











