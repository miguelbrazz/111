"""
Exercício utilizando Listas

Faça um algoritmo que, através da digitação pelo teclado, armazene várias cidades e seus estados.

Exemplo da estrutura das listas:
lista_de_cidades	lista_de_estados
0 	PORTO ALEGRE	RIO GRANDE DO SUL
1	CANOAS		    RIO GRANDE DO SUL
2	GRAVATAI		RIO GRANDE DO SUL
3	FLORIANÓPOLIS	SANTA CATARINA
4	TUBARÃO		    SANTA CATARINA
5	SANTA MARIA		RIO GRANDE DO SUL



Exemplo da digitação dos dados:
Digite uma nova cidade: CANOAS
Digite o estado desta cidade: RIO GRANDE DO SUL

Seu programa deverá utilizar o seguinte menu:

Menu
0-	Finalizar o Programa
1-	Adicionar cidades e estados
2-	Listar as cidades e seus respectivos estados
3-	Alterar o nome de uma cidade
4-	Alterar o nome de um estado
5-	Listar todas as cidades de um determinado estado
6-	Retirar da lista uma cidade ou estado
Escolha:

Obs:
- Você não deve aceitar duas cidades com o mesmo nome.
- A opção 2 deverá ser no seguinte formato:
	Relatório Geral:
	Cidade: CANOAS		    Estado: RIO GRANDE DO SUL
	Cidade: PORTO ALEGRE	Estado: RIO GRANDE DO SUL
	Cidade: GRAVATAI		Estado: RIO GRANDE DO SUL
	Cidade: FLORIANÓPOLIS	Estado: SANTA CATARINA
	Cidade: TUBARÃO		    Estado: SANTA CATARINA

- A Opção 5, deverá pedir ao usuário para escolher um estado e listar todas as cidades deste estado. Exemplo:
Escolha o estado: SANTA CATARINA
As cidades deste estado são:
- FLORINÓPLIS
- TUBARÃO

- Ao excluir um estado, não esqueça de excluir também todas as cidades relacionadas a este estado.

"""


""" 
Exemplo:
dicionario = {'RIO GRANDE DO SUL' : ['PORTO ALEGRE','CANOAS','GRAVATAÍ'], 'SANTA CATARINA':['FLORIANÓPOLIS','TUBARÃO']}
"""


dicionario = {}
dicionario = {'RIO GRANDE DO SUL' : ['PORTO ALEGRE','CANOAS','GRAVATAÍ'], 'SANTA CATARINA':['FLORIANÓPOLIS','CANOAS','TUBARÃO']}




""" Menus """
def menu_principal():
    return input(("\n"*8) + """ 
                    
            Menu
            0-	Finalizar o Programa
            1-	Adicionar cidades e estados
            2-	Listar as cidades e seus respectivos estados
            3-	Alterar o nome de uma cidade
            4-	Alterar o nome de um estado
            5-	Listar todas as cidades de um determinado estado
            6-	Retirar da lista uma cidade ou estado
            Escolha: """)


def menu_retirar_lista():
    return input(""" 
                    
            Menu
            1-	Retirar Cidade da lista
            2-	Retirar Estado da lista
            Escolha:""")

""" Menus """




""" Funções do programa principal """

def adicionar_cidade():
    """ Esta função tem o objetivo de adicionar uma nova
        cidade na lista de cidades.
    """
    pass

def adicionar_estado():
    """ Esta função tem o objetivo de adicionar um novo
        estado na lista de estados.
        - lista os estados existentes (caso lista não vazia)
        - adiciona um estado novo ou existente.
    """
    pass


def listar_cidades():
    """ Esta função tem a finalidade de mostrar todas as
        cidades da lista_de_cidades e seu estado.
    """
    print("\n"*5)
    print("=-=-=-=- Cidades existentes na lista:")


def mostra_cidades_do_estado(estado_escolhido):
    pass


def mostrar_cidades_por_estado():
    print("--- Estados Existentes:")


def alterar_cidade():
    """ Esta função tem a finalidade de alterar o nome de
        alguma cidade.
    """
    nome_cidade = input('Nome da cidade para alterar: ')

    for chave,lst_cidades in dicionario.items():
        if nome_cidade in lst_cidades:
            confirma = input("Alterar a cidade"+nome_cidade+"do estado"+chave+" s/n? : ")
            if confirma.lower() == 's':
                indice = lst_cidades.index(nome_cidade)
                lst_cidades[indice] = input('Novo Nome: ')

    print(dicionario)




def alterar_estado():
    """ Esta função tem a finalidade de alterar o nome de
        algum estado.
    """
    pass


def excluir_cidade():
    """ Esta função tem a finalidade de retirar o nome de uma cidade da lista
        de cidades.
    """
    nome_cidade = input('Nome da cidade para alterar: ')

    for chave,lst_cidades in dicionario.items():
        if nome_cidade in lst_cidades:
            confirma = input("Excluir a cidade "+nome_cidade+" do estado "+chave+" s/n? : ")
            if confirma.lower() == 's':
                lst_cidades.remove(nome_cidade)


def excluir_estado():
    """ Esta função tem a finalidade de retirar o nome de um estado da lista
        de estados, retirando também as cidades vinculadas a este estado.
    """
    pass

def retirar_cidade_ou_estado():
    resposta = menu_retirar_lista()
    if resposta == '1':
        excluir_cidade()
    if resposta == '2':
        excluir_estado()


def adicionar_cidade_estado():
    nome_cidade = input("Nome cidade: ")
    nome_estado = input("Nome estado: ")

    if not nome_estado in dicionario:
        dicionario[nome_estado] = []

    if not nome_cidade in dicionario[nome_estado]:
        dicionario[nome_estado].append(nome_cidade)
    else: print('NAAAAAOOOO')

    print(dicionario)


# Programa - Início
while True:
    resposta = menu_principal()
    if   resposta == '0': break
    elif resposta == '1': adicionar_cidade_estado()
    elif resposta == '2': listar_cidades()
    elif resposta == '3': alterar_cidade()
    elif resposta == '4': alterar_estado()
    elif resposta == '5': mostrar_cidades_por_estado()
    elif resposta == '6': retirar_cidade_ou_estado()



