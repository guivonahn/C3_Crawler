import pyxel
import random

tamanho_tile = 8
banco_sprite = 0
tamanho_hud = 16

class worldItem:

    parede1 = (0,0)
    parede2 = (1,0)
    chao = (0,1)
    portal = (2,0)
    hud = (2,1)
    janela = (6,1)
    chao2 = (6,2)
    tapete0 = (2,2)
    tapete1 = (3,2)
    tapete2 = (2,3)
    tapete3 = (3,3)

    andaveis = [chao, chao2, portal, tapete0, tapete1, tapete2, tapete3]
    solidos = [parede1,parede2, hud, janela]

class world:

    altura = 16
    largura = 24

    def __init__(self,tilemap):
        self.tilemap = tilemap
        self.mapa_mundo = []

        for _ in range(tamanho_hud // tamanho_tile):
            self.mapa_mundo.append([worldItem.hud] * self.largura)

        for y in range(self.altura + tamanho_hud):
            self.mapa_mundo.append([])
            for x in range(self.largura):
                if self.tilemap.pget(x,y) == worldItem.parede1:
                    self.mapa_mundo[-1].append(worldItem.parede1)
                elif self.tilemap.pget(x,y) == worldItem.parede2:
                    self.mapa_mundo[-1].append(worldItem.parede2)
                elif self.tilemap.pget(x,y) == worldItem.portal:
                    self.mapa_mundo[-1].append(worldItem.portal)
                elif self.tilemap.pget(x,y) ==worldItem.janela:
                    self.mapa_mundo[-1].append(worldItem.janela)

                elif self.tilemap.pget(x,y) == worldItem.chao2:
                    self.mapa_mundo[-1].append(worldItem.chao2)

                elif self.tilemap.pget(x,y) == worldItem.tapete0:
                    self.mapa_mundo[-1].append(worldItem.tapete0)

                elif self.tilemap.pget(x,y) == worldItem.tapete1:
                    self.mapa_mundo[-1].append(worldItem.tapete1)

                elif self.tilemap.pget(x,y) == worldItem.tapete2:
                    self.mapa_mundo[-1].append(worldItem.tapete2)

                elif self.tilemap.pget(x,y) == worldItem.tapete3:
                    self.mapa_mundo[-1].append(worldItem.tapete3)

                else:
                    self.mapa_mundo[-1].append(worldItem.chao)

def desenhar_mundo(pyxel,x,y, world_item):
    pyxel.blt(
        x * tamanho_tile,
        y * tamanho_tile,
        banco_sprite,
        world_item[0] * tamanho_tile,
        world_item[1] * tamanho_tile,
        tamanho_tile,
        tamanho_tile
    )
