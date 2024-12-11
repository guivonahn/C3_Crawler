#ALGORITMOS E ESTRUTURAS DE DADOS 1 - 3 AVALIAÇÃO
#GUILHERME V. A. AVILA
#FERNANDO C. MELLO


import pyxel, time, random
import world, inimigo, arma
from world import world, worldItem, desenhar_mundo

tamanho_tile = 8
banco_sprite = 0
tamanho_hud = 16

class jogo:
    def __init__(self):
        pyxel.init(192,144, title='Dungeon do C3')
        pyxel.load('recursos.pyxres')
        pyxel.playm(0, loop=True)

        self.jogador_x = 64
        self.jogador_y = 64
        self.jogador_vida = 3
        self.jogador_score = 0
        self.jogador_tipo = 'p'
        self.lado_visao = 'r'
        #self.arma = arma.projetil(self.jogador_x, self.jogador_y, self.lado_visao)
        self.projeteis_ativos = []
        
        self.bit_sprites = [[40,0], [48,0]]
        self.jogador_sprites = [[8,8], [0,16], [8,16]]
        self.jogador_sprite = self.jogador_sprites[0]


        self.velocidade_movimento = 2
        self.velocidade_ataque = 4 # MENOR = MAIS RAPIDO
        self.velocidade_ataque_cont = 0

        self.inimigos_ativos = []
        self.inimigo1 = inimigo.inimigo(3, 1)
        self.timer_ataque = 0
        self.inimigos_ativos.append(self.inimigo1)

        self.world = world(pyxel.tilemap(0))
        self.autores = ['G.V.A.A','F.C.M']

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_UP):
            self.jogador_sprite = self.jogador_sprites[2]
            self.lado_visao = 'u'
            if self.colisao(self.jogador_x,self.jogador_y,self.velocidade_movimento,self.lado_visao, self.jogador_tipo):
                self.jogador_y -= self.velocidade_movimento
                #self.arma.y = self.jogador_y
                #print(f"{self.lado_visao}, {(self.jogador_x,self.jogador_y)}")

        if pyxel.btn(pyxel.KEY_DOWN):
            self.jogador_sprite = self.jogador_sprites[0]
            self.lado_visao = 'd'
            if self.colisao(self.jogador_x,self.jogador_y,self.velocidade_movimento,self.lado_visao, self.jogador_tipo):
                self.jogador_y += self.velocidade_movimento
                #self.arma.y = self.jogador_y
                #print(f"{self.lado_visao}, {(self.jogador_x,self.jogador_y)}")

        if pyxel.btn(pyxel.KEY_LEFT):
            self.jogador_sprite = self.jogador_sprites[1]
            self.lado_visao = 'l'
            if self.colisao(self.jogador_x,self.jogador_y,self.velocidade_movimento,self.lado_visao, self.jogador_tipo):
                self.jogador_x -= self.velocidade_movimento
                #self.arma.x = self.jogador_x
            3   #print(f"{self.lado_visao}, {(self.jogador_x,self.jogador_y)}")
      
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.jogador_sprite = self.jogador_sprites[1]
            self.lado_visao = 'r'
            if self.colisao(self.jogador_x,self.jogador_y,self.velocidade_movimento,self.lado_visao, self.jogador_tipo):
                self.jogador_x += self.velocidade_movimento
                #self.arma.x = self.jogador_x
                #print(f"{self.lado_visao}, {(self.jogador_x,self.jogador_y)}")
        
        if pyxel.btn(pyxel.KEY_SPACE):
            self.velocidade_ataque_cont += 1
            if self.velocidade_ataque_cont == self.velocidade_ataque:
                self.projeteis_ativos.append(arma.projetil(self.jogador_x, self.jogador_y, self.lado_visao, len(self.projeteis_ativos)))
                print(len(self.projeteis_ativos))
                self.velocidade_ataque_cont = 0

        if pyxel.btnp(pyxel.KEY_J):
            self.jogador_vida -= 1 
            self.jogador_score -= 1

        if pyxel.btnp(pyxel.KEY_K):
            self.jogador_vida += 1
            self.jogador_score += 1
            self.inimigo1.resetar()

        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        for projetil in self.projeteis_ativos:
            if projetil.cont > projetil.alcance:
                self.projeteis_ativos.remove(projetil) 
            for inimigo in self.inimigos_ativos:
                pos_inimigo = inimigo.calcular_matriz()
                for pos in pos_inimigo:
                    if pos in (projetil.calcular_matriz()):
                        if inimigo.vida != 0:
                            inimigo.vida -= 1

        for inimigo in self.inimigos_ativos:
            if inimigo.vida == 0 and inimigo.vivo:
                inimigo.vivo = False
                self.inimigos_ativos.remove(inimigo)

        print(len(self.inimigos_ativos))

        prox = self.inimigo1.proximo_bloco(self.jogador_x, self.jogador_y)
        if self.colisao(prox[0][0], prox[0][1], self.inimigo1.velocidade, self.inimigo1.lado, self.inimigo1.tipo):
            self.inimigo1.caçar(self.jogador_x, self.jogador_y)

            self.timer_ataque += 1

            if self.timer_ataque == self.inimigo1.velocidade_ataque:
                if self.inimigo1.dar_dano(self.jogador_x, self.jogador_y) and self.jogador_vida > 0:
                    self.jogador_vida -= 1
                self.timer_ataque = 0



    def draw(self):
        pyxel.cls(1) # cor do fundo

        for y in range(self.world.altura + tamanho_hud): # desenha o mundo
            for x in range(self.world.largura):
                world_item = self.world.mapa_mundo[y][x]
                desenhar_mundo(pyxel,x,y, world_item)
        
        for projetil in self.projeteis_ativos:
            bit_sprite = random.choice(self.bit_sprites)
            projetil.update()
            pyxel.blt(projetil.proj_x, projetil.proj_y, 0, bit_sprite[0],bit_sprite[1],8,8,4)

        pyxel.blt(self.inimigo1.x,self.inimigo1.y,0,24,8,8,8,4) # desenha inimigo

        pyxel.blt(self.jogador_x,self.jogador_y,0,self.jogador_sprite[0],self.jogador_sprite[1],8,8,4) #desenha o jogador


        pyxel.rect(6,2,30,12,0)
        pyxel.rect(7,3,28,10,7)
        for vida in range(self.jogador_vida):
            
            pyxel.blt(8 + (8 * vida) + (vida * 1),4,0,24,0,8,8,4) # desenha as vidas
        
        pyxel.rect(39,2,24,12,0)
        pyxel.rect(40,3,22,10,7)
        pyxel.blt(40,4,0,32,0,8,8,4) # desenha a moedas da hud
        pyxel.text(50,6, f'{self.jogador_score}x', 0)

       
        pyxel.rect(127,4,63,9,0)
        pyxel.rect(128,5, 61, 7, 7)
        pyxel.text(129, 6, f'{self.autores[1]} e {self.autores[0]}', random.randint(0,15))

                    
    def colisao(self,pos_x,pos_y,velocidade,lado, tipo):
        if lado == 'u':
            x = pos_x
            y = pos_y - velocidade
        if lado == 'd':
            x = pos_x
            y = pos_y + velocidade
        if lado == 'l':
            x = pos_x - velocidade
            y = pos_y
        if lado == 'r':
            x = pos_x + velocidade
            y = pos_y

        constante_misteriosa = 6 # PERGUNTAR PARA O CLEO OU BICHO
        tamanho_tile = 8
        if tipo == 'p':
            posicoes = [
                [x // tamanho_tile, y // tamanho_tile],
                [(x + 5) // tamanho_tile, y // tamanho_tile],
                [x // tamanho_tile, (y + 5) // tamanho_tile],
                [(x + 5) // tamanho_tile, (y + 5) // tamanho_tile],
            ] #possui as 4 vertices do sprite
        else:
            posicoes = [
                [x // tamanho_tile, y // tamanho_tile],
                [(x+7) // tamanho_tile, y // tamanho_tile],
                [x // tamanho_tile, (y+7) // tamanho_tile],
                [(x+7)// tamanho_tile, (y+7)// tamanho_tile],
            ]

        try:
            for posicao in posicoes:
                if self.world.mapa_mundo[posicao[1]][posicao[0]] not in worldItem.andaveis:
                    return False
            return True
        except Exception as e:
            print(e) 


jogo()
