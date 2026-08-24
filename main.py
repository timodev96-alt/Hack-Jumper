import pygame
import sys 

import renderer

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
TARGET_RATIO = SCREEN_WIDTH/SCREEN_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.RESIZABLE)
canvas = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("Hack Jumper")

clock = pygame.time.Clock()
running = True
render_rect = renderer.calculate_render_rect(SCREEN_WIDTH,SCREEN_HEIGHT)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        elif event.type == pygame.VIDEORESIZE: #When the User Change the window Size!
            render_rect = renderer.calculate_render_rect(event.w,event.h)

    canvas.fill((130,200,240))
    scaled_surface = pygame.transform.smoothscale(canvas,(render_rect.width,render_rect.height))
    screen.blit(scaled_surface,(render_rect.x, render_rect.y))
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()