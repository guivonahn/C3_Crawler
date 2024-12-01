class projetil:
    def __init__(self, pos_x, pos_y, lado):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.lado = lado

    def trajeto(self):
        for _ in range(15):
            if self.lado == 'u':
                self.pos_y += 1
            if self.lado == 'd':
                self.pos_y -= 1
            if self.lado == 'l':
                self.pos_x -= 1
            if self.lado == 'r':
                self.pos_x += 1
        return False