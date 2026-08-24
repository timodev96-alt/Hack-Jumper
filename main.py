#main.py
import pygame
import sys 

from renderer import calculate_render_rect
import constans

pygame.init()


screen = pygame.display.set_mode((constans.SCREEN_WIDTH,constans.SCREEN_HEIGHT), pygame.RESIZABLE)
canvas = pygame.Surface((constans.SCREEN_WIDTH,constans.SCREEN_HEIGHT))

pygame.display.set_caption("Hack Jumper")

clock = pygame.time.Clock()
running = True
render_rect = calculate_render_rect(constans.SCREEN_WIDTH,constans.SCREEN_HEIGHT)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        elif event.type == pygame.VIDEORESIZE: #When the User Change the window Size!
            render_rect = calculate_render_rect(event.w,event.h)

    canvas.fill((130,200,240))
    scaled_surface = pygame.transform.smoothscale(canvas,(render_rect.width,render_rect.height))
    screen.blit(scaled_surface,(render_rect.x, render_rect.y))
    
    pygame.display.flip()
    clock.tick(constans.FPS)
pygame.quit()
sys.exit()