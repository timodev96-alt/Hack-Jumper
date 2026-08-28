#player.py
import pygame
import terrain
import constans

class Player:
      def __init__(self):
            self.ongraoung = True
            self.gravity = 0.5
            self.velocity = 0
            self.x = 50
            self.y = 50
            self.speed = 5
            self.jump = -12
            self.player_rect = pygame.Rect(self.x,self.y,50,50)

      def moves(self , terrain):
            self.keys = pygame.key.get_pressed()
            if self.keys[pygame.K_RIGHT]:
                  self.x = self.x + self.speed
                  self.player_rect.x = self.x

            if self.keys[pygame.K_LEFT]:
                  self.x = self.x - self.speed
                  self.player_rect.x = self.x

            self.velocity += self.gravity
            if self.velocity > 15:
                  self.velocity = 15
            self.player_rect.y += self.velocity
            self.ongraoung = False

            if self.velocity >= 0:
                  for plat in terrain.platforms:
                        if self.player_rect.colliderect(plat):
                              prev_bottom = self.player_rect.bottom - self.velocity
                              if prev_bottom <= plat.top:
                                    self.player_rect.bottom = plat.top
                                    self.velocity = 0
                                    self.ongraoung = True
            self.y = self.player_rect.y
                  
            if self.keys[pygame.K_SPACE] and self.ongraoung == True:
                  self.velocity = self.jump
                  self.ongraoung = False

      def draw(self,page,camera):
            pygame.draw.rect(page,(255,0,0),camera.apply(self.player_rect))

