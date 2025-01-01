import pyxel, random, time

class inimigo:
    def __init__(self, vida, velocidade, x, y):
        
        self.vida = vida
        self.modelo = random.randint(0,1)
        self.velocidade = velocidade
        self.velocidade_ataque = 10
        self.lado = 'r'
        self.count = 0
        self.tipo = 'i'
        self.x = x
        self.y = y
        self.vivo = True

    def proximo_bloco(self, jogador_x, jogador_y, inimigos_ativos):
        prox_x, prox_y = self.x, self.y

        if jogador_x > self.x:
            prox_x += self.velocidade
        if jogador_x < self.x:
            prox_x -= self.velocidade
        if jogador_y > self.y:
            prox_y += self.velocidade
        if jogador_y < self.y:
            prox_y -= self.velocidade

        for inimigo in inimigos_ativos:
            if inimigo != self:
                if self.colisao_inimigos(self, inimigo):
                    prox_x, prox_y = self.evitar_colisao(inimigos_ativos, prox_x, prox_y)

        return [(prox_x, prox_y)]

    def colisao_inimigos(self,inimigo1, inimigo2):
        matriz1 = inimigo1.calcular_matriz()
        matriz2 = inimigo2.calcular_matriz()

        return bool(matriz1 & matriz2)

    def evitar_colisao(self, inimigos, prox_x, prox_y):
       for outro in inimigos:
        if outro != self:
            dist_x = abs(outro.x - prox_x)
            dist_y = abs(outro.y - prox_y)

            if dist_x < 8 and dist_y < 8:
                if dist_x < dist_y:
                    if prox_x > outro.x:
                        prox_x += self.velocidade / 2
                    else:
                        prox_x -= self.velocidade / 2 
                else:
                    if prox_y > outro.y:
                        prox_y += self.velocidade / 2
                    else:
                        prox_y -= self.velocidade / 2
        return prox_x, prox_y

    def caçar(self, jogador_x, jogador_y):
        if jogador_x > self.x:
            self.x += self.velocidade
            self.lado = 'r'
        if jogador_x < self.x:
            self.x -= self.velocidade
            self.lado = 'l'
        if jogador_y > self.y:
            self.y += self.velocidade
            self.lado = 'u'
        if jogador_y < self.y:
            self.y -= self.velocidade
            self.lado = 'd'

    def dar_dano(self, jogador_x, jogador_y):
        if (self.x, self.y) == (jogador_x, jogador_y):
            return True
        else:
            return False

    def calcular_matriz(self):
        matriz = set()
        for i in range(8):
            for j in range(8):
                matriz.add((self.x + i, self.y + j))
        return matriz



    def resetar(self):
        if (self.x < 0) or (self.y < 0):
            self.x, self.y = 100, 100
        if (self.x > 192) or (self.y > 144):
            self.x, self.y = 100, 100

        x_antigo, y_antigo = self.x, self.y

        self.x -= self.velocidade
        self.y -= self.velocidade
        
        return (x_antigo, y_antigo)
