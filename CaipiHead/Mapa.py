import Menu
import Constantes
import pygame

class Mapa(Menu.BaseMenu):
    def __init__(self, x, y, vel):
        super().__init__("Mapa", 'Fonte/Fonte.ttf', 80, 120)
        self._x = x
        self._y = y
        self._vel = vel
        self._teclas = None

    
                   
              
    def colisao_retangulo(self):
        if self._x < 410:
            self._x = 410
        if self._y < 190: 
            self._y = 190
        if self._x > 925:
            self._x = 925
        if self._y > 625:
            self._y = 625

    def fase1(self):
        if self._x < 925 and self._y > 190 and self._x > 775 and self._y < 300:
            import Fase_aviao
            loop = Fase_aviao.Fase1(200, 300)
            loop.fase1rodando()

  
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def vel(self):
        return self._vel

    @vel.setter
    def vel(self, value):
        self._vel = value

    @property
    def teclas(self):
        return self._teclas

    @teclas.setter
    def teclas(self, value):
        self._teclas = value

    def loop_mapa(self):
  
        while self.executando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    self.executando = False

            self.teclas = pygame.key.get_pressed()

         
            if self.teclas[pygame.K_LEFT]:
                self._x -= self._vel
            if self.teclas[pygame.K_RIGHT]:
                self._x += self._vel
            if self.teclas[pygame.K_UP]:
                self._y -= self._vel
            if self.teclas[pygame.K_DOWN]:
                self._y += self._vel

         
            if self.teclas[pygame.K_RETURN]:
                self.fase1()

         
            self.tela.blit(Constantes.Mapa, (0, 0))  
            self.tela.blit(Constantes.Icon_mapa, (self._x, self._y)) 
            self.colisao_retangulo()   
            pygame.display.update()

            


mapa = Mapa(416, 189, 6)
mapa.loop_mapa()
