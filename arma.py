class projetil:
    def __init__(self,x,y, lado, id):
        self.x = x
        self.y = y
        self.id = id
        self.lado = lado
        self.ativo = True
        self.alcance = 10
        self.cont = 0
        self.velocidade = 0.2
        self.proj_x, self.proj_y = self.x, self.y

    def update(self):

        for _ in range(self.alcance):
            if self.lado == 'u':
                self.proj_y -= self.velocidade
            if self.lado == 'd':
                self.proj_y += self.velocidade
            if self.lado == 'r':
                self.proj_x += self.velocidade
            if self.lado == 'l':
                self.proj_x -= self.velocidade

        self.cont += 1
    

    def calcular_matriz(self):
        matriz = set()
        for i in range(8):
            for j in range(8):
                matriz.add((self.x + i, self.y + j))
        return matriz

    

