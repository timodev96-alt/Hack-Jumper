#player.py
import pygame
import terrain
import constans
class Player:
      def __init__(self):
            self.ongraoung = True
            self.gravity = 0.5
            self.velocity = 0
            self.x = 50.0
            self.y = 630.0
            self.speed = 5
            self.jump = -12
            self.player_rect = pygame.Rect(self.x,self.y,50,50)

      def moves(self , terrain):
            self.keys = pygame.key.get_pressed()
            if self.keys[pygame.K_RIGHT]:
                  self.x += self.speed
            if self.keys[pygame.K_LEFT]:
                  self.x -= self.speed

            self.velocity += self.gravity
            if self.velocity > 15:
                  self.velocity = 15

            prev_bottom = self.y + self.player_rect.height
            self.y += self.velocity
            self.player_rect.x = int(self.x)
            self.player_rect.y = int(self.y)
            
            self.ongraoung = False

            if self.velocity >= 0:
                  for plat in terrain.platforms:
                        if self.player_rect.right > plat.left and self.player_rect.left < plat.right:
                              if prev_bottom <= plat.top and self.player_rect.bottom >= plat.top:
                                    self.y = plat.top - self.player_rect.height
                                    self.player_rect.y = int(self.y)
                                    self.velocity = 0
                                    self.ongraoung = True
                                    break
                  
            if self.keys[pygame.K_SPACE] and self.ongraoung == True:
                  self.velocity = self.jump
                  self.ongraoung = False

      def draw(self,page,camera):
            pygame.draw.rect(page,(255,0,0),camera.apply(self.player_rect))

