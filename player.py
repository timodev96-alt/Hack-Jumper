import pygame

ongraoung = True
gravity = 0.5
velocity = 0
x = 50
y = 50
speed = 5
jump = -12
player_rect = pygame.Rect(x,y,50,50)
ground = pygame.Rect(0, 490, 900, 100)
left_wall = pygame.Rect(-90, 0 ,100, 900)
right_wall = pygame.Rect(690, 0 ,100, 900)
def moves():
   global x, y, velocity, ongraoung 
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
      velocity = 0
      ongraoung = True
   if player_rect.colliderect(right_wall) :
         player_rect.right = right_wall.left
         x -= 5
   if player_rect.colliderect(left_wall) :
         player_rect.left = left_wall.right
         x += 5      
   if keys[pygame.K_SPACE] and ongraoung == True:
      velocity = -10
      ongraoung = False

def draw(page):
   pygame.draw.rect(page,(255,0,0),player_rect)

