#main.py
import pygame
import sys 
from renderer import calculate_render_rect
from camera import Camera
from terrain import Terrain
import debug
import constans
import player
pygame.init()


screen = pygame.display.set_mode((constans.SCREEN_WIDTH,constans.SCREEN_HEIGHT), pygame.RESIZABLE)
canvas = pygame.Surface((constans.SCREEN_WIDTH,constans.SCREEN_HEIGHT))

pygame.display.set_caption(constans.TITLE)
clock = pygame.time.Clock()
camera = Camera()
terrain = Terrain()
render_rect = calculate_render_rect(constans.SCREEN_WIDTH,constans.SCREEN_HEIGHT)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.VIDEORESIZE: #When the User Change the window Size!
            render_rect = calculate_render_rect(event.w,event.h)

    debug.handel_debug_input(camera)
    terrain.update(camera.y)

    canvas.fill((130,200,240))
    terrain.draw(canvas,camera)
    debug.draw_debug_info(canvas,camera)

    scaled_surface = pygame.transform.smoothscale(canvas,(render_rect.width,render_rect.height))
    screen.fill((0,0,0))
    screen.blit(scaled_surface,(render_rect.x, render_rect.y))

    player.moves()

    pygame.draw.rect(screen,(0,0,0), player.ground)
    pygame.draw.rect(screen,(0,0,0,),player.right_wall)
    pygame.draw.rect(screen,(0,0,0,),player.left_wall)
    player.draw(screen)

    pygame.display.flip()
    clock.tick(constans.FPS)
pygame.quit()
sys.exit()