
# TRAB 1 - MIGUEL BRAZ

"""

Tarefa 1 – Dicionários


    Faça um algoritmo que realize uma pesquisa de satisfação sobre qual das empresas acima o
usuário mais se identifica. Em sua pesquisa o usuário deverá escolher qual empresa ele mais
gosta e para essa empresa o usuário deve dar uma nota de 1 a 5.

    Armazene esses dados em um dicionário ( pesquisa = {} ), a empresa e a nota para essa
empresa.

    Armazene esses dados no dicionário utilizando o nome da empresa como chave, e as notas
recebidas em uma lista.

    Não é necessária nenhuma identificação, ou validação do usuário. Este apenas escolhe uma
empresa e uma nota. Podendo realizar essas notas quantas vezes desejar.

"""

pesquisa = {}
pesquisa = {'QUALCOMM': [] , 'HISILICON': [] , 'APPLE' : []}



#------------------------------------------------------------------



bkp = open('BKP.txt', 'r')
linha = bkp.read()
pesquisa[linha] = []
print(pesquisa)
bkp.close()



#------------------------------------------------------------------



def adicionar_empresa():
    nome_empresa = input("Nome da Empresa: ")

    if nome_empresa in pesquisa:
        print ("-- Empresa já cadastrada! --")

    else:
        pesquisa[nome_empresa] = []



# -----------------------------------------------------------------



def avaliacao():
    print(pesquisa)
    nome_avaliacao = input("Empresa cadastrada que deseja avaliar: ")
    if nome_avaliacao in pesquisa:
        avaliacao_empresa = int(input("Avaliação da empresa(1 - 5): "))
        if avaliacao_empresa>0 and avaliacao_empresa<6:
            pesquisa[nome_avaliacao].append(avaliacao_empresa)
            
            if   avaliacao_empresa == 1 : print("Você avaliou a empresa como Péssima!")
            elif avaliacao_empresa == 2 : print("Você avaliou a empresa como Ruim!")
            elif avaliacao_empresa == 3 : print("Você avaliou a empresa como Regular!")
            elif avaliacao_empresa == 4 : print("Você avaliou a empresa como Boa!")
            elif avaliacao_empresa == 5 : print("Você avaliou a empresa como Ótima!")
        
        else:
            return print("A avaliação é válida do nº 1 ao 5!")

    else:
        return print("Empresa não cadastrada!")



# -----------------------------------------------------------------



def relatorio_geral():
    print(pesquisa)
    for nome_empresa,notas in pesquisa.items():
        print(nome_empresa,sum(notas))



# -----------------------------------------------------------------
    


def relatorio_por_empresa():
    nome_empresa = input("Nome da Empresa: ")
    for nome , notas in pesquisa.items():
        if nome_empresa == nome:
            for nota_empresa in notas:
                print(nota_empresa)

        valor = sum(notas)
        numero_notas = len(notas)
    print("Média das notas registradas: ",valor/numero_notas)



# -----------------------------------------------------------------



"--Menu--"
while True:
    resposta = input\
        ("""

        Menu
            0-  Finalizar o Programa
            1-  Inserir Empresa
            2-  Realizar avaliação
            3-  Relatório geral
            4-  Relatório por empresa
        Escolha: """
        )
    
    if   resposta == '0': break
    elif resposta == '1': adicionar_empresa()
    elif resposta == '2': avaliacao()
    elif resposta == '3': relatorio_geral()
    elif resposta == '4': relatorio_por_empresa()

    
