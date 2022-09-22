
"""
Crie uma classe Lampada (=anterior)
Crie uma classe chamada lanterna.
Essa classe terá os seguintes atributos.
-lampada1 -instância de Lampada
-lampada2 -instância de Lampada
-botao    -uma tecla (tecla 1) (simula um botão :))
-capa -True/False
-cor_capa -[ 'TRANSPARENTE', 'AZUL', 'VERMELHO' , 'BRANCO' , 'PRETO']

Ações:
> Acender/Apagar lampada1/lampada2
> Colocar ou Retirar a capa
> Trocar a cor da capa
"""

"""
+-----------------+ 
| Lampada         |
|-----------------|
|.situacao - bool | 
|-----------------|
|.ligar()         |
|.desligar()      |
+-----------------+

+--------------------+
| Lanterna           |
|--------------------|
|.lampada1 - Lampada |
|.lampada2 - Lampada |
|.botao    - string  |
|.capa     - bool    |
|.cor_capa - lista   |
|--------------------|
+--------------------+


"""

class Lampada:
    def __init__(self):
        self.estado = False  # False - Desligada  True - Ligada

    def altera_estado(self):
        self.estado = not self.estado

    def ligado_desligado(self):
        if self.estado:
            return "LIGADA."
        return "DESLIGADA."

    def __str__(self):
        return f"Lâmpada {self.ligado_desligado()}"

class Lanterna:
    def __init__(self):
        self.lampada1 = Lampada()
        self.lampada2 = Lampada()
        self.botao = "DESLIGADO"
        self.capa = False
        self.cor_capa = None


    def ligar_desligar_lampada1(self):
        self.lampada1.altera_estado()

    def ligar_desligar_lampada2(self):
        self.lampada2.altera_estado()

    def botao_l_d(self):
            self.ligar_desligar_lampada1()
            self.ligar_desligar_lampada2()
            if self.botao == "DESLIGADO":
                self.botao = "LIGADO"
            else:
                self.botao = "DESLIGADO"

    def set_cor_capa(self,capa_escolhida):
        self.cor_capa = capa_escolhida
        self.capa = True

    def escolher_capa(self):
        cores = [ 'TRANSPARENTE', 'AZUL', 'VERMELHO' , 'BRANCO' , 'PRETO']
        if not self.capa:
            cor_capa = input("""
            Cores Disponíveis:
            1- Transparente
            2- Azul
            3- Vermelho
            4- Branco
            5- Preto 
        Escolha: """)
            try:
                return cores[int(cor_capa)-1]
            except:
                input("Erro. Escolha apenas uma das cores disponíveis. [Enter]")
            return self.escolher_capa()

    def colocar_capa(self):
        if self.capa:
            resposta = input("... Trocar de Capa? s/n: ").lower()
            if resposta == "n":
                return
            if resposta != "s":
                return self.cor_capa()
            self.retirar_capa()

        self.set_cor_capa(self.escolher_capa())

    def retirar_capa(self):
        self.cor_capa = None
        self.capa = False

    def status_capa(self):
        if self.capa:
            return "Colocada."
        return "Não Presente."

    def status_cor(self):
        if self.cor_capa:
            return self.cor_capa
        return "..."

    def __str__(self):
        return f""" 
        
        Lampada1 {str(self.lampada1)} 
        Lampada2 {str(self.lampada2)}
        Botão {self.botao}   Capa {str(self.status_capa())}  Cor {str(self.status_cor())}"""

lanterna = Lanterna()
print(lanterna)
lanterna.colocar_capa()
lanterna.botao_l_d()
print(lanterna)
lanterna.colocar_capa()
print(lanterna)
