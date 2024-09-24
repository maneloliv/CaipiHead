import pygame
import spritesheet

#Dimensões
LARGURA_TELA = 1500 
ALTURA_TELA = 800

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
relogio = pygame.time.Clock()
time = pygame.time.get_ticks()
#Cores RGB
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)
AZUL = (0, 255, 255)
CINZA= (50, 50, 50)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)

#Imagem
MapaFundo = pygame.image.load('imagens/Mapa.png')
Mapa = pygame.transform.scale(MapaFundo, (LARGURA_TELA, ALTURA_TELA))

#Menu
MenuBackground = pygame.image.load('imagens/Summer4.png')
MenuFundo = pygame.transform.scale(MenuBackground, (1500, 800))

Icon = pygame.image.load('imagens/Icon_caipihead.png')
Icon_mapa = pygame.transform.scale(Icon, (50,50))

fundo = pygame.image.load('imagens/fundo3.png').convert_alpha()
fundo = pygame.transform.scale(fundo,(LARGURA_TELA, ALTURA_TELA))

nave= pygame.image.load('imagens/nave.png').convert_alpha()
nave= pygame.transform.scale(nave, (70,70))

missil = pygame.image.load('imagens/principal.png').convert_alpha()
missil = pygame.transform.scale(missil, (30,30))
missil = pygame.transform.rotate(missil, -45)

person = pygame.image.load('imagens/espacial.png').convert_alpha()
person = pygame.transform.scale(person, (80,80))
person = pygame.transform.rotate(person, -90)

especial = pygame.image.load('imagens/especial.png').convert_alpha()
especial = pygame.transform.scale(especial, (70,70))
especial = pygame.transform.rotate(especial, -90)

explosao = pygame.image.load('imagens/explosão.png').convert_alpha()
explosao = pygame.transform.scale(explosao, (100,100))

fogo_sprite = pygame.image.load('imagens/tirofogo1.png').convert_alpha()
fogo_sprite = pygame.transform.scale(fogo_sprite, (80, 80))
fogo_sprite1 = spritesheet.SpriteSheet(fogo_sprite)

boss = pygame.image.load('imagens/bosszin.png').convert_alpha()
boss = pygame.transform.scale(boss, (150, 150))

hud_vida = pygame.image.load('imagens/hud_vida.png').convert_alpha()
hud_vida = pygame.transform.scale(hud_vida,(250, 70)) 

vida = pygame.image.load('imagens/vida.png').convert_alpha()
vida = pygame.transform.scale(vida, (40, 40))

hudEspecial = pygame.image.load('imagens/CartaEspecial.png').convert_alpha()
hudEspecial = pygame.transform.scale(hudEspecial, (30,30))