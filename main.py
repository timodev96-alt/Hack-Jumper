import pygame
import sys 
import player
pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Hack Jumper")
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            
    screen.fill((130,200,240))   
    player.moves()
    pygame.draw.rect(screen,(0,0,0), player.ground)
    pygame.draw.rect(screen,(0,0,0,),player.right_wall)
    pygame.draw.rect(screen,(0,0,0,),player.left_wall)
    player.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    

pygame.quit()
sys.exit()