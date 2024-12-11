import pyxel, random, time

class inimigo:
    def __init__(self, vida, velocidade):
        
        self.vida = vida
        self.velocidade = velocidade
        self.velocidade_ataque = 20
        self.lado = 'r'
        self.count = 0
        self.tipo = 'i'
        self.x = random.randint(64,100)
        self.y = random.randint(64,100)
        self.vivo = True

    def proximo_bloco(self, jogador_x, jogador_y):
        prox_x, prox_y = self.x, self.y  

        if jogador_x > self.x:
            prox_x += self.velocidade
        if jogador_x < self.x:
            prox_x -= self.velocidade
        if jogador_y > self.y:
            prox_y += self.velocidade
        if jogador_y < self.y:
            prox_y -= self.velocidade

        return [(prox_x, prox_y)]

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

        #time.sleep(1)

    def dar_dano(self, jogador_x, jogador_y):
        if (self.x, self.y) == (jogador_x, jogador_y):
            return True
        else:
            return False

    def calcular_matriz(self):
        matriz = []
        for i in range(8):
            matriz.append([self.x + i, self.y + i])
        
        return matriz
        #return [[self.x, self.y], [self.x + 8, self.y],
        #    [self.x, self.y + 8],[self.x + 8, self.y + 8]]



    def resetar(self):
        if (self.x < 0) or (self.y < 0):
            self.x, self.y = 100, 100
        if (self.x > 192) or (self.y > 144):
            self.x, self.y = 100, 100

        x_antigo, y_antigo = self.x, self.y

        self.x -= self.velocidade
        self.y -= self.velocidade
        
        return (x_antigo, y_antigo)
