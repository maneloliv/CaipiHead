import Menu


class GameOver(Menu.BaseMenu):
    def __init__(self):
        super().__init__("GameOver", 'Fonte/Fonte.ttf', 80, 120)
        self.opcoes_menu = ["Reiniciar", "Mapa", "Inicio"]

    def selecionar_opcao(self):
        if self.opcao_selecionada == 0:
            import Fase_aviao
            volta1 = Fase_aviao.Fase1(200, 300)
            volta1.fase1rodando()
            
        elif self.opcao_selecionada == 1:
            import Mapa
            volta2 = Mapa.Mapa(416, 189, 8)
            volta2.loop_mapa()
          
        elif self.opcao_selecionada == 2:
            import Menu
            volta3 = Menu.MenuPrincipal()
            volta3.loop_principal()
           


gameover = GameOver()
gameover.loop_principal()
