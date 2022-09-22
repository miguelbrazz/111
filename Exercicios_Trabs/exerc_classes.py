# Declaração da classe ---

class Lampada:
    def __init__(self):
        self.situacao = False

    def liga_desliga(self):
        self.situacao = not self.situacao

    def valida_situacao(self):
        if self.situacao == True:
            return "LIGADA"
        return "DESLIGADA"

    def __str__(self):
        return "Lâmpada: "+self.valida_situacao()


# Programa ---

lampada1 = Lampada()
lampada2 = Lampada()

while True:
    escolha = input("Lampada 1 ou 2: ")
    if escolha == '1':
        lampada_escolhida = lampada1
    if escolha == '2':
        lampada_escolhida = lampada2

    botao = input("Aperte o botão para Ligar/Desligar [1] ")
    if botao == '1':
      lampada_escolhida.liga_desliga()
    print("Lampada1: ",lampada1)
    print("Lampada2: ",lampada2)


    
