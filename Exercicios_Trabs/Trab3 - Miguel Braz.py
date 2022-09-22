#Miguel Braz - Manhã

#-----------------------------------------------------

lista_de_atletas = {}
lista_de_clubes = {}
lista_de_saltos = {}

#-----------------------------------------------------


class Atleta:
    def __init__(self,nome_atleta,saltos = None):
        self.nome_atleta = nome_atleta
        self.saltos = [0,0,0,0,0]

    def atleta_nome(self):
        return self.nome_atleta
    def saltos1(self):
        return self.saltos


class lista_atleta(Atleta):
    pass


class Clube(lista_atleta):
    def __init__(self,nome_clube):
        self.nome_clube = nome_clube
        
    def atletas_clube(self,nome_atleta):
        self.atletas_clube(nome_atleta)
    def saltos_atletas_clube1(self,saltos):
        self.saltos_atletas_clube(saltos)



#-----------------------------------------------------



def cadastro_atleta():
    nome_atleta = input("Nome do Atleta: ")

    if nome_atleta in lista_de_atletas:
        print ("-- Atleta já cadastrado! --")

    else:
        lista_de_atletas[nome_atleta] = []



#-----------------------------------------------------



def saltos_atleta():
    atleta_saltos = input("Atleta cadastrado que desejas registrar os saltos: ")
    if atleta_saltos in lista_de_atletas:
        for saltos1 in range(5): saltos1 = input("Saltos: ")
        saltos_registrar = Atleta(saltos1)
        lista_de_saltos[0,saltos_registrar] = []
        
        print("Saltos registrados!")

    else:
        return print("Atleta não cadastrado!")

        

#-----------------------------------------------------



def relatorio_geral():
    for nome_atleta,saltos1 in lista_de_atletas.items():
        print("Atleta: ", nome_atleta,"\nsaltos: ", saltos1)
        print(lista_de_saltos)



#-----------------------------------------------------



def cadastro_clube():
    nome_clube = input("Nome do clube: ")

    if nome_clube in lista_de_clubes:
        print ("-- Clube já cadastrado! --")

    else:
        lista_de_clubes[nome_clube] = []

    

#-----------------------------------------------------



def relatorio_atleta_por_clube():
    print(lista_de_atletas)
    print(lista_de_clubes)
    for nome_atleta,saltos in lista_de_atletas.items():
        print(nome_atleta,sum(saltos1))



#-----------------------------------------------------


def relatorio_final():
    print(lista_de_atletas)
    print(lista_de_clubes)
    for atleta , saltos in lista_de_atletas.items():
        if nome_atleta == atleta:
            for saltos1 in saltos:
                print(saltos1)
                
    valor = sum(saltos1)
    numero_notas = len(saltos1)
    print("Média dos saltos registradas: ",valor/numero_notas)


 
"--Menu--"
while True:
    resposta = input\
        ("""
        =================================
        MENU
        =================================
            0-  Finaliza
            1-  Cadastrar Atleta
            2-  Cadastrar Saltos do Atleta
            3-  Relatório Geral do Atleta
            4-  Cadastrar Clube do Atleta
            5-  Relatório de Atletas por Clube
            6-  Relatório Final
        =================================
        Escolha: """
        )
    
    if   resposta == '0': break
    elif resposta == '1': cadastro_atleta()
    elif resposta == '2': saltos_atleta()
    elif resposta == '3': relatorio_geral()
    elif resposta == '4': cadastro_clube()
    elif resposta == '5': relatorio_atleta_por_clube()
    elif resposta == '6': relatorio_final()

