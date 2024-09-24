import Menu
import pygame
import Constantes

class MenuCarregar(Menu.BaseMenu):
    def __init__(self):
        super().__init__("Carregar Save", 'Fonte/Fonte.ttf', 40, 120)
        self._speed_run_file = 'speed_run_times.log'
        self._opcoes_menu = self.carregar_tempos() + ["Voltar"]

    def carregar_tempos(self):
        tempos = []
        try:
            with open(self._speed_run_file, 'r') as file:
                for line in file:
                    if 'Tempo: ' in line:
                        try:
                            tempo_str = line.split('Tempo: ')[1].split(' segundos')[0]
                            tempo = float(tempo_str)
                            tempos.append((tempo, line.strip()))
                        except (IndexError, ValueError):
                            continue 
            tempos.sort(key=lambda x: x[0])
            
            return [tempo[1] for tempo in tempos]
        except FileNotFoundError:
            return ["Nenhum tempo registrado"]

    def verifica_opcao(self):
        for i, opcao in enumerate(self._opcoes_menu):
            cor = Constantes.VERDE if i == self.opcao_selecionada else Constantes.BRANCO
            if opcao == "Nenhum tempo registrado":
                cor = Constantes.VERMELHO 
            self.desenhar_texto(opcao, self.fonte_pequena, cor, self.tela, 350, 200 + i * 60)

    def selecionar_opcao(self):
        if self.opcao_selecionada < len(self._opcoes_menu) - 1:
           pass 
        elif self.opcao_selecionada == len(self._opcoes_menu) - 1:
            voltar = Menu.MenuPrincipal()
            voltar.loop_principal()
            pygame.quit()

    @property
    def opcoes_menu(self):
        return self._opcoes_menu

    @opcoes_menu.setter
    def opcoes_menu(self, value):
        if isinstance(value, list):
            self._opcoes_menu = value
        else:
            raise ValueError("Opções de menu devem ser uma lista.")

if __name__ == "__main__":
    menu = MenuCarregar()
    menu.loop_principal()
