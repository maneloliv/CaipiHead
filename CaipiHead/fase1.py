import pygame
import random
import Constantes
from base_fase import BaseFase
import sys
import time
from datetime import datetime  

class Fase1(BaseFase):
    def __init__(self, pos_person_x, pos_person_y):
        super().__init__()
        self._pos_person_x = pos_person_x
        self._pos_person_y = pos_person_y
        self._naves = [{'pos_x': random.randint(1500, 1600), 'pos_y': random.randint(1, 720)} for _ in range(7)]
        self._vel_missil_x = 0
        self._frame = 0
        self._velocidade_boss = 1 
        self._y = 650
        self._x = 1200
        self._hab_y = 0
        self._hab_x = 0
        self._boss = [{'pos_x': self._x, 'pos_y': self._y}]
        self._explosao_duracao = 200

        
        self._start_time = None
        self._speed_run_file = 'speed_run_times.log'

        
        pygame.mixer.init()
        self._som_missil = pygame.mixer.Sound('sons/missil.wav')
        self._som_especial = pygame.mixer.Sound('sons/especial.wav')

       

    
    @property
    def pos_person_x(self):
        return self._pos_person_x

    @pos_person_x.setter
    def pos_person_x(self, value):
        self._pos_person_x = value

    @property
    def pos_person_y(self):
        return self._pos_person_y

    @pos_person_y.setter
    def pos_person_y(self, value):
        self._pos_person_y = value

    @property
    def naves(self):
        return self._naves

    @naves.setter
    def naves(self, value):
        self._naves = value

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, value):
        self._boss = value

    def respawn(self):
        x = 1350
        y = random.randint(1, 720)
        return {'pos_x': x, 'pos_y': y}

    def colisions(self):
        for nave in self._naves:
            nave_rect = Constantes.nave.get_rect(topleft=(nave['pos_x'], nave['pos_y']))
            if self._person_rect.colliderect(nave_rect):
                nave.update(self.respawn())
                self.vida -= 1
                break
            for bos in self._boss:                
                boss_rect = Constantes.boss.get_rect(topleft=(bos['pos_x'], nave['pos_y']))
                if self._person_rect.colliderect(boss_rect):
                    self.vida -= 1

    def misselcolision(self):
        for missil in self._misseis[:]:
            missil_rect = Constantes.missil.get_rect(topleft=(missil.x, missil.y))
            
            if missil.x > 1500:
                self._misseis.remove(missil)
                continue
            
            for nave in self._naves:
                nave_rect = Constantes.nave.get_rect(topleft=(nave['pos_x'], nave['pos_y']))
                
                if missil_rect.colliderect(nave_rect):
                    self.temp_especial += 1
                    self.verificaespecial()
                    self._misseis.remove(missil)
                    nave.update(self.respawn())
                    break

            for bos in self._boss:                
                boss_rect = Constantes.boss.get_rect(topleft=(bos['pos_x'], bos['pos_y']))
                if missil_rect.colliderect(boss_rect):
                    self._misseis.remove(missil)
                    self.boss_vida += 1
                    self.temp_especial += 1
                    self.verificaespecial()
                    
    def verificaespecial(self):
        if self.temp_especial % 10 == 0:
            if self.totalespecial < 5:
                self.totalespecial += 1 
            self.temp_especial = 0                    

    def especialcolision(self):
        
        for especial in self._especial_vet[:]:
            especial_rect = Constantes.especial.get_rect(topleft=(especial.x, especial.y))

            for nave in self._naves:
                nave_rect = Constantes.nave.get_rect(topleft=(nave['pos_x'], nave['pos_y']))
                if especial_rect.colliderect(nave_rect):
                    self._especial_vet.remove(especial)
                    nave.update(self.respawn())
                    self._explosoes.append({'pos': nave_rect.topleft, 'tempo': pygame.time.get_ticks()})

            for bos in self._boss:
                boss_rect = Constantes.boss.get_rect(topleft=(bos['pos_x'], bos['pos_y']))
                if especial_rect.colliderect(boss_rect):
                    self.boss_vida += 10 
                    self._especial_vet.remove(especial)
                    self._explosoes.append({'pos': boss_rect.topleft, 'tempo': pygame.time.get_ticks()})

    def atualizar_frame(self):
        current_time = pygame.time.get_ticks()
        if current_time - self._last_update >= self._cooldown:
            self._frame += 1
            self._last_update = current_time
            if self._frame >= len(self.sprite_fogo):
                self._frame = 0

    def move_boss(self):
        for bos in self._boss[:]:
            tempboss = pygame.time.get_ticks()
            if tempboss % self._velocidade_boss == 0:
                if self._y == 650:
                    self._hab_y = 1
                    
                    if self._start_time is None:
                        self._start_time = time.time()
                elif self._y == 50:
                    self._hab_y = 0 
                if self._hab_y == 1:
                    bos['pos_y'] = -1
                if self._hab_y == 0:
                    bos['pos_y'] = +1

                self._y += bos['pos_y'] * 1

                if self._x == 1300:
                    self._hab_x = 1
                elif self._x == 1200:
                    self._hab_x = 0 
                if self._hab_x == 1:
                    bos['pos_x'] = -1
                if self._hab_x == 0:
                    bos['pos_x'] = +1

                self._x += bos['pos_x'] * 1
                bos.update({'pos_x': self._x, 'pos_y': self._y})

    def carregar_sprites(self):
        self.sprite_fogo = []
        animation_steps = 3
        for x in range(animation_steps):
            self.sprite_fogo.append(Constantes.fogo_sprite1.get_image(x, 28, 65, 2, Constantes.PRETO))
        return self.sprite_fogo

    def salvar_tempo(self, tempo):
        agora = datetime.now()
        data_hora = agora.strftime("%d/%m/%Y %H:%M")

        with open(self._speed_run_file, 'a') as file:
            file.write(f"{data_hora} - Tempo: {tempo:.2f} segundos\n")
        
        print(f"Tempo registrado: {tempo:.2f} segundos em {data_hora}.")

    def fase1rodando(self):
        while self.rodando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rodando = False
                    pygame.quit()
                    sys.exit()

            self.colisions()
            self.atualizar_frame()
            self.carregar_sprites()
            
            Constantes.tela.blit(Constantes.fundo, (0, 0))
            
            rel_x = Constantes.LARGURA_TELA % Constantes.fundo.get_rect().width
            Constantes.tela.blit(Constantes.fundo, (rel_x - Constantes.fundo.get_rect().width, 0))
            if rel_x < 1280:
                Constantes.tela.blit(Constantes.fundo, (rel_x, 0))

            tecla = pygame.key.get_pressed()
            if tecla[pygame.K_UP] and self._pos_person_y > 1:
                self._pos_person_y -= 1

            if tecla[pygame.K_DOWN] and self._pos_person_y < 720:
                self._pos_person_y += 1

            if tecla[pygame.K_RIGHT] and self._pos_person_x < 1420:
                self._pos_person_x += 1

            if tecla[pygame.K_LEFT] and self._pos_person_x > 1:
                self._pos_person_x -= 1

            if tecla[pygame.K_SPACE]:
                self._som_missil.play()
                self.tempo = pygame.time.get_ticks()
                self._missil_rect = Constantes.missil.get_rect(center=(self._pos_person_x + 60, self._pos_person_y + random.randint(20, 70)))
                Constantes.tela.blit(self.sprite_fogo[self._frame], (self._pos_person_x + 75, self._pos_person_y - 35))
                if self.tempo - self._last_update >= self._cooldown:
                    
                    self._misseis.append(self._missil_rect)
                    self._last_update = self.tempo

            if tecla[pygame.K_x]:
                
                self.time1 = pygame.time.get_ticks()
                self._especial_rect = Constantes.especial.get_rect(center=(self._pos_person_x + 40, self._pos_person_y + 40))
                if self.totalespecial >= 1:
                    self._som_especial.play()
                    self._especial_vet.append(self._especial_rect)
                    self.totalespecial -= 1

            if self.boss_vida >= 500:
                if self._start_time:
                    elapsed_time = time.time() - self._start_time
                    self.salvar_tempo(elapsed_time)
                import GameOver
                loop = GameOver.GameOver()
                loop.loop_principal()
                pygame.quit()

            if self.vida <= 0:
                import GameOver
                loop = GameOver.GameOver()
                loop.loop_principal()
                pygame.quit()

            for nave in self._naves:
                nave['pos_x'] -= 1
                if nave['pos_x'] < 0:
                    nave.update(self.respawn())

            self._person_rect.y = self._pos_person_y
            self._person_rect.x = self._pos_person_x
            Constantes.tela.blit(Constantes.person, self._person_rect.topleft)
        

            for missil in self._misseis[:]:
                missil.x += 2
                self.misselcolision()
            
            for especial in self._especial_vet[:]:
                especial.x += 1
                
                self.especialcolision()
 
            for missil in self._misseis:
                Constantes.tela.blit(Constantes.missil, missil.topleft)
                
            for especial in self._especial_vet:
                Constantes.tela.blit(Constantes.especial, especial.topleft)

            tempo_atual = pygame.time.get_ticks()
            for explosao in self._explosoes[:]:
                if tempo_atual - explosao['tempo'] > self._explosao_duracao:
                    self._explosoes.remove(explosao)
                else:
                    Constantes.tela.blit(Constantes.explosao, explosao['pos'])

            Constantes.tela.blit(Constantes.person, (self._pos_person_x, self._pos_person_y))

            for nave in self._naves:
                nave_rect = Constantes.nave.get_rect(topleft=(nave['pos_x'], nave['pos_y']))
                Constantes.tela.blit(Constantes.nave, nave_rect.topleft)

            for bos in self._boss:
                self.move_boss()
                boss_rect = Constantes.boss.get_rect(topleft=(bos['pos_x'], bos['pos_y']))
                Constantes.tela.blit(Constantes.boss, boss_rect.topleft)

            Constantes.tela.blit(Constantes.hud_vida, (10, 0)) 
            
            x_vida = 85
            x_especial = 25

            for _ in range(self.vida):
                Constantes.tela.blit(Constantes.vida, (x_vida, 10))
                x_vida += 40

            for _ in range(self.totalespecial):
                Constantes.tela.blit(Constantes.hudEspecial, (x_especial, 80))
                x_especial += 40

            pygame.display.update()
