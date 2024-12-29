import pyxel
import random

tamanho_tile = 8
banco_sprite = 0
tamanho_hud = 16

class worldItem:
    parede1 = (0, 0)
    parede2 = (1, 0)
    chao = (0, 1)
    portal = (2, 0)
    hud = (2, 1)
    janela = (6, 1)
    chao2 = (6, 2)
    tapete0 = (2, 2)
    tapete1 = (3, 2)
    tapete2 = (2, 3)
    tapete3 = (3, 3)
    parede3 = (6, 3)
    chao21 = (4, 2)
    chao22 = (5, 2)
    chao23 = (4, 3)
    chao24 = (5, 3)

    andaveis = [chao, chao2, portal, tapete0, tapete1, tapete2, tapete3, chao21, chao22, chao23, chao24]
    solidos = [parede1, parede2, hud, janela, parede3]

class world:
    altura = 16
    largura = 24

    def __init__(self, tilemap):
        self.tilemap = tilemap
        self.mapa_mundo = []

        # Preenche a área do HUD
        for _ in range(tamanho_hud // tamanho_tile):
            self.mapa_mundo.append([worldItem.hud] * self.largura)

        # Criação do mapa usando dicionário para simplificação
        tile_map = {
            worldItem.parede1: worldItem.parede1,
            worldItem.parede2: worldItem.parede2,
            worldItem.portal: worldItem.portal,
            worldItem.janela: worldItem.janela,
            worldItem.chao: worldItem.chao,
            worldItem.chao2: worldItem.chao2,
            
            worldItem.chao21 : worldItem.chao21,
            worldItem.chao22 : worldItem.chao22,
            worldItem.chao23 : worldItem.chao23,
            worldItem.chao24 : worldItem.chao24,
            
            worldItem.tapete0: worldItem.tapete0,
            worldItem.tapete1: worldItem.tapete1,
            worldItem.tapete2: worldItem.tapete2,
            worldItem.tapete3: worldItem.tapete3,
            worldItem.parede3: worldItem.parede3
        }

        for y in range(self.altura + tamanho_hud):
            self.mapa_mundo.append([])  # Cria uma nova linha no mapa
            for x in range(self.largura):
                tile = self.tilemap.pget(x, y)  # Obtém o tile atual
                self.mapa_mundo[-1].append(tile_map.get(tile, worldItem.hud))

def desenhar_mundo(pyxel, x, y, world_item):
    pyxel.blt(
        x * tamanho_tile,
        y * tamanho_tile,
        banco_sprite,
        world_item[0] * tamanho_tile,
        world_item[1] * tamanho_tile,
        tamanho_tile,
        tamanho_tile
    )
