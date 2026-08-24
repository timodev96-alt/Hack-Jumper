import pygame



x = 50
y = 50
speed = 5
def moves():
   global x
   keys = pygame.key.get_pressed()
   if keys[pygame.K_RIGHT]:
     x = x + speed

   if keys[pygame.K_LEFT]:
     x = x - speed 
def draw(page):
   pygame.draw.rect(page,(255,0,0),(x,y,50,50))