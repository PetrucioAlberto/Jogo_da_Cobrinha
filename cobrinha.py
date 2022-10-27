class Cobra:
    def __init__(self, tam_tela=(300, 400),
                 posicao=[80, 50],
                 corpo=[[80, 50], [70, 50], [60, 50]],
                 direcao ='direita'):
        self.tam_tela=tam_tela
        self.posicao = posicao
        self.corpo = corpo
        self.direcao = direcao

    def mudar_direcao(self, nova_direcao):
        if nova_direcao == 'direita' and not self.direcao == 'esquerda':
            self.direcao = 'direita'
        if nova_direcao == 'esquerda' and not self.direcao == 'direita':
            self.direcao = 'esquerda'
        if nova_direcao == 'cima' and not self.direcao == 'baixo':
            self.direcao = 'cima'
        if nova_direcao == 'baixo' and not self.direcao == 'cima':
            self.direcao = 'baixo'


    def mover(self,posicao_comida):
        if self.direcao == 'direita':
            self.posicao[0] += 10
        if self.direcao == 'esquerda':
            self.posicao[0] -= 10
        if self.direcao == 'cima':
            self.posicao[1] -= 10
        if self.direcao == 'baixo':
            self.posicao[1] += 10


        self.corpo.insert(0, list(self.posicao))

        if self.posicao == posicao_comida:
            return True

        self.corpo.pop()
        return False

    def verifica_colisao(self):
        if self.posicao[0] > (self.tam_tela[0] - 10) or self.posicao[0] < 0:
            return True

        if self.posicao[1] > (self.tam_tela[1] - 10) or self.posicao[1] < 0:
            return True
        for parte_do_corpo in self.corpo[1:]:
            if self.posicao == parte_do_corpo:
                return True
