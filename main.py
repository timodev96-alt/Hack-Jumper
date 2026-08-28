#main.py
import pygame
import sys 
from renderer import calculate_render_rect
from camera import Camera
from terrain import Terrain
import debug
import constans
from player import Player
pygame.init()


screen = pygame.display.set_mode((constans.SCREEN_WIDTH,constans.SCREEN_HEIGHT), pygame.RESIZABLE)
canvas = pygame.Surface((constans.SCREEN_WIDTH,constans.SCREEN_HEIGHT))

pygame.display.set_caption(constans.TITLE)
clock = pygame.time.Clock()
camera = Camera()
terrain = Terrain()
player = Player()
render_rect = calculate_render_rect(constans.SCREEN_WIDTH,constans.SCREEN_HEIGHT)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.VIDEORESIZE: #When the User Change the window Size!
            render_rect = calculate_render_rect(event.w,event.h)

    debug.handel_debug_input(camera)
    player.moves(terrain)
    camera.y = player.player_rect.y - (constans.SCREEN_HEIGHT //2 )
    terrain.update(camera.y)

    canvas.fill((130,200,240))
    terrain.draw(canvas,camera)
    player.draw(canvas, camera)
    debug.draw_debug_info(canvas,camera)

    scaled_surface = pygame.transform.smoothscale(canvas,(render_rect.width,render_rect.height))
    screen.fill((0,0,0))
    screen.blit(scaled_surface,(render_rect.x, render_rect.y))

    pygame.display.flip()
    clock.tick(constans.FPS)
pygame.quit()
sys.exit()