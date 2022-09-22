
class Fechadura:
    def __init__(self, segredo):
        self.chave  = segredo
        self.status = True   # True Trancada   False Destrancada

    def trancar(self,segredo):
        if self.chave == segredo:
            self.status = True
        else:
            input('>>> Chave incorreta. ')

    def destrancar(self,segredo):
        if self.chave == segredo:
            self.status = False
        else: input('>>> Chave incorreta. ')

    def strSituacaoFechadura(self):
        if self.status == True:
            return " TRANCADA. "
        return " DESTRANCADA. "

    def __str__(self):
        return " Chave: " + str(self.chave) + "  status: " + self.strSituacaoFechadura()

    #  # semelhante ao __str__()   acima
    # def mostrar_fechadura(self):
    #     return " Chave: " + str(self.chave) + "  status: " + str(self.status)

class Porta:
    def __init__(self): # construtor
        # atributos
        self.situacao = True  # True Aberta   False Fechada
        self.alt = 210
        self.lar = 80
        self.cor = None
        self.fechadura = None

    def trancar_porta(self, chave):
        if self.situacao == False:
            self.fechadura.trancar(chave)
        else: input('>>> Não dá. A porta esta Aberta. ')

    def destrancar_porta(self,chave):
        if self.situacao == False:
            self.fechadura.destrancar(chave)
        else: input('>>> Porta Está aberta. ')

    def instalar_fechadura(self,fechadura):
        self.fechadura = fechadura

    def strSituacao(self):
        if self.situacao == True:
            return "Porta Aberta."
        return "Porta Fechada."

    def situacaoCor(self):
        if self.cor == None:
            return " Porta sem Cor."
        return self.cor

    def abrir_porta(self):
        self.situacao = True

    def fechar_porta(self):
        self.situacao = False

    def pintar(self, cor):
        self.cor = cor

    def __str__(self):
        return  "... A:"+str(self.alt) + " L:"+str(self.lar) + "  Fechadura: " + str(self.fechadura) +\
                "  Sit.:"+self.strSituacao()+ "  Cor:"+self.situacaoCor()

    # def mostrar_dados(self):
    #     return  "... A:"+str(self.alt) + " L:"+str(self.lar) + \
    #             "  Sit.:"+self.strSituacao()+ "  Cor:"+self.situacaoCor()
        # return "... Fechadura: "+str(self.fechadura.mostrar_dados_fechadura()) +\
        #        "  Sit.:"+self.getStrSituacao()+"  Cor:"+self.situacaoCor()



#------- Programa Principal
p1 = Porta()

fechadura = Fechadura(input("Digite o segredo da chave: "))
print(fechadura)

p1.instalar_fechadura(fechadura)
#print(fechadura.mostrar_fechadura())

#input()

# print(f.mostrar_dados_fechadura())
# input()

while True:
    print("=-=-=-=-=-=-=")
    print(p1)
    print("=-=-=-=-=-=-=")
    e = input('''
    MENU
    --------
    0- Finaliza
    1- Abrir a Porta.
    2- Fechar a Porta.
    3- Pintar a Porta.
    4- Trancar a Porta.
    5- Destrancar a Porta.
    
    Escolha: ''')

    if e == '0':
        break
    if e == '1':
        p1.abrir_porta()
    if e == '2':
        p1.fechar_porta()
    if e == '3':
        p1.pintar(input("Digite a Cor: "))
    if e == '4':
        p1.trancar_porta(input('... Insira a chave: '))

    if e == '5':
        p1.destrancar_porta(input('...Insira a chave: '))
