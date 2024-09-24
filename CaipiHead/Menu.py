import pygame
import sys
import Constantes

pygame.init()

class BaseMenu:
    def __init__(self, titulo, fonte_arquivo, fonte_pequena_tamanho, fonte_grande_tamanho):
        self._tela = pygame.display.set_mode((Constantes.LARGURA_TELA, Constantes.ALTURA_TELA))
        pygame.display.set_caption(titulo)
        self._fonte_pequena = pygame.font.Font(fonte_arquivo, fonte_pequena_tamanho) 
        self._fonte = pygame.font.Font(fonte_arquivo, fonte_grande_tamanho)
        self._opcoes_menu = []
        self._opcao_selecionada = 0
        self._executando = True
        self._relogio = pygame.time.Clock()

    def desenhar_texto(self, texto, fonte, cor, superficie, x, y):
        objeto_texto = fonte.render(texto, True, cor)
        retangulo_texto = objeto_texto.get_rect()
        retangulo_texto.topleft = (x, y)
        superficie.blit(objeto_texto, retangulo_texto)

    def loop_principal(self):
        while self._executando:
            self._tela.blit(Constantes.MenuFundo, (0, 0))
            self.desenhar_texto("Caipihead", self._fonte, Constantes.PRETO, self._tela, 650, 50)

            for i, opcao in enumerate(self._opcoes_menu):
                cor = Constantes.VERDE if i == self._opcao_selecionada else Constantes.PRETO
                self.desenhar_texto(opcao, self._fonte_pequena, cor, self._tela, 650, 260 + i * 60)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        self._opcao_selecionada = (self._opcao_selecionada - 1) % len(self._opcoes_menu)
                    if evento.key == pygame.K_DOWN:
                        self._opcao_selecionada = (self._opcao_selecionada + 1) % len(self._opcoes_menu)
                    if evento.key == pygame.K_RETURN:
                        self.selecionar_opcao()

            pygame.display.update()

    @property
    def tela(self):
        return self._tela

    @property
    def fonte_pequena(self):
        return self._fonte_pequena

    @property
    def fonte(self):
        return self._fonte

    @property
    def opcoes_menu(self):
        return self._opcoes_menu

    @opcoes_menu.setter
    def opcoes_menu(self, opcoes):
        if isinstance(opcoes, list):
            self._opcoes_menu = opcoes
        else:
            raise ValueError("Opções de menu devem ser uma lista.")

    @property
    def opcao_selecionada(self):
        return self._opcao_selecionada

    @opcao_selecionada.setter
    def opcao_selecionada(self, opcao):
        if 0 <= opcao < len(self._opcoes_menu):
            self._opcao_selecionada = opcao
        else:
            raise ValueError("Índice de opção selecionada fora dos limites.")

    @property
    def executando(self):
        return self._executando

    @executando.setter
    def executando(self, estado):
        if isinstance(estado, bool):
            self._executando = estado
        else:
            raise ValueError("O estado deve ser um valor booleano.")

    @property
    def relogio(self):
        return self._relogio

    @relogio.setter
    def relogio(self, relogio):
        if isinstance(relogio, pygame.time.Clock):
            self._relogio = relogio
        else:
            raise ValueError("Relógio deve ser uma instância de pygame.time.Clock.")

class MenuPrincipal(BaseMenu):
    def __init__(self):
        super().__init__("Menu Principal", 'Fonte/Fonte.ttf', 80, 120)
        self.opcoes_menu = ["Iniciar Jogo", "Recordes", "Sair"]

    def iniciar_jogo(self):
        import Mapa
        load1 = Mapa.Mapa(416, 189,8)
        load1.loop_mapa()
        
    def carregar(self):
        import Tempos
        load2 = Tempos.MenuCarregar()
        load2.loop_principal()
        

    def selecionar_opcao(self):
        if self.opcao_selecionada == 0:
            self.iniciar_jogo()
            self.executando = False
        elif self.opcao_selecionada == 1:
    
            self.carregar()
            self.executando = False
        elif self.opcao_selecionada == 2:
            
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    menu = MenuPrincipal()
    menu.loop_principal()
