import pygame


gravity = 0.5
velocity = 0
x = 50
y = 50
speed = 5
player_rect = pygame.Rect(x,y,50,50)
ground = pygame.Rect(0, 490, 900, 100)
def moves():
   global x, y, velocity
   keys = pygame.key.get_pressed()
   if keys[pygame.K_RIGHT]:
     x = x + speed
     player_rect.x = x
   if keys[pygame.K_LEFT]:
     x = x - speed
     player_rect.x = x
   velocity += gravity
   player_rect.y += velocity  
   if player_rect.colliderect(ground) :
      player_rect.bottom = ground.top
   
def draw(page):
   pygame.draw.rect(page,(255,0,0),player_rect)

