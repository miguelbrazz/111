

class Pessoa:
    def __init__(self,nome,idade):
        self.nome   = nome
        self.idade  = idade
        self.carro  = None

    def adquirir(self,carro):
        self.carro = carro

    def adulto(self):
        if self.idade >= 18:
            return True
        return False

    def __str__(self):
        return ">>>Nome: "+self.nome + "  Idade: " + str(self.idade) + "  Automovel: " + str(self.carro)


class Automovel:
    def __init__(self,marca,cor):
        self.marca  = marca
        self.cor    = cor
        self.placa  = None

    def emplacar(self,placa):
        self.placa = placa

    def __str__(self):
        return" ...Marca: "+self.marca + "  Cor: " + self.cor + "  Placa: " + str(self.placa)


def imprime_pessoas():
    for i,p in enumerate(lst_Pessoas):
        print(i,p)

def insere_objetos_lista_pessoas():
    lst_Pessoas.append(Pessoa("Maria", 33))
    lst_Pessoas.append(Pessoa("Pedro", 44))
    lst_Pessoas.append(Pessoa("Fabio", 24))

def imprime_automoveis():
    for i,a in enumerate(lst_automoveis):
        print(i,a)

def insere_objetos_lista_automoveis():
    lst_automoveis.append(Automovel("Ford","Branca"))
    lst_automoveis.append(Automovel("Fiat","Verde"))
    lst_automoveis.append(Automovel("GM","Vermelho"))

def emplaca_automovel():
    imprime_automoveis()
    escolha = int(input("...Escolha o indice: "))
    lst_automoveis[escolha].emplacar(input("..Digite a placa"))

def dono_carro():
    imprime_pessoas()
    escolha_pess = int(input("...Escolha o indice: "))

    dono = lst_Pessoas[escolha_pess]

    if dono.adulto():
        imprime_automoveis()
        escolha_auto = int(input("...Escolha o indice: "))

        dono.adquirir(lst_automoveis[escolha_auto])

##################
# Principal
lst_automoveis = []
lst_Pessoas = []

while True:
    opcao = input('''
    
    1- cadastrar pessoa
    2- cadastrar automoveis
    3- relatorio pessoas
    4- relatorio de automoveis
    5- emplacar automovel
    6- adquirir automovel
    
    escolha: ''')

    if opcao == '1':
        insere_objetos_lista_pessoas()
    if opcao == '2':
        insere_objetos_lista_automoveis()
    if opcao == '3':
        imprime_pessoas()
    if opcao == '4':
        imprime_automoveis()
    if opcao == '5':
        emplaca_automovel()
    if opcao == '6':
        dono_carro()

