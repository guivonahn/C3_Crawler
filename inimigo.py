import pyxel, random, time

class inimigo:
    def __init__(self, vida, velocidade):
        
        self.vida = vida
        self.velocidade = velocidade
        self.velocidade_ataque = 10
        self.lado = 'r'
        self.count = 0
        self.x = random.randint(64,100)
        self.y = random.randint(64,100)

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

        if (self.x, self.y) == (jogador_x, jogador_y):
            if self.count == self.velocidade_ataque: 
                self.count = 0
                print('atacando rrrrrr')
            self.count += 1
        #time.sleep(1)
    
    def resetar(self):
        if (self.x < 0) or (self.y < 0):
            self.x, self.y = 100, 100
        if (self.x > 192) or (self.y > 144):
            self.x, self.y = 100, 100

        x_antigo, y_antigo = self.x, self.y

        self.x -= self.velocidade
        self.y -= self.velocidade
        
        return (x_antigo, y_antigo)
