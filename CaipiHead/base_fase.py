import pygame
import Constantes

class BaseFase:
    def __init__(self):
        self._rodando = True
        self._vida = 4
        self._boss_vida = 1
        self._explosoes = []
        self._last_update = pygame.time.get_ticks()
        self._cooldown = 90
        self._totalespecial = 0
        self._temp_especial = 0
        self._misseis = []
        self._especial_vet = []
        self._person_rect = Constantes.person.get_rect()
        self._missil_rect = Constantes.missil.get_rect()
        self._especial_rect = Constantes.especial.get_rect()
        self._explosao_rect = Constantes.explosao.get_rect()
        self._boss_rect = Constantes.boss.get_rect()
        self._vida_rect = Constantes.vida.get_rect()

    
    @property
    def rodando(self):
        return self._rodando

    @rodando.setter
    def rodando(self, value):
        self._rodando = value

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, value):
        self._vida = value

    @property
    def boss_vida(self):
        return self._boss_vida

    @boss_vida.setter
    def boss_vida(self, value):
        self._boss_vida = value

    @property
    def misseis(self):
        return self._misseis

    @misseis.setter
    def misseis(self, value):
        self._misseis = value

    @property
    def especial_vet(self):
        return self._especial_vet

    @especial_vet.setter
    def especial_vet(self, value):
        self._especial_vet = value

    @property
    def totalespecial(self):
        return self._totalespecial

    @totalespecial.setter
    def totalespecial(self, value):
        self._totalespecial = value

    @property
    def temp_especial(self):
        return self._temp_especial

    @temp_especial.setter
    def temp_especial(self, value):
        self._temp_especial = value
