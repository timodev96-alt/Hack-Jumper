#main.py
import pygame

import menu
import sys 
from renderer import calculate_render_rect
from camera import Camera
from terrain import Terrain
import debug
import constans
from player import Player
pygame.init()
pygame.font.init()
score_font = pygame.font.SysFont("Arial", 45)
screen = pygame.display.set_mode((constans.SCREEN_WIDTH,constans.SCREEN_HEIGHT), pygame.RESIZABLE)
canvas = pygame.Surface((constans.SCREEN_WIDTH,constans.SCREEN_HEIGHT))

pygame.display.set_caption(constans.TITLE)
clock = pygame.time.Clock()
camera = Camera()
terrain = Terrain()
player = Player()
menu_rect = pygame.Rect(680, 20 , 100, 50)
menu_font = pygame.font.Font(None, 40)
menu_txt = menu_font.render("Menu", True, (0,0,0))
render_rect = calculate_render_rect(constans.SCREEN_WIDTH,constans.SCREEN_HEIGHT)
text_rect = menu_txt.get_rect(center=menu_rect.center)
menu_status = 0


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

    score_text = score_font.render(f"{player.score}", True,(255,255,255))
    score_rect = score_text.get_rect(center=(constans.SCREEN_WIDTH//2, 30))
    canvas.blit(score_text,score_rect)
    pygame.draw.rect(canvas, (0, 150, 0), menu_rect, border_radius=15)
    pygame.draw.rect(canvas, (0, 0, 0), menu_rect, 3, border_radius=15)
    canvas.blit(menu_txt, text_rect)
    scaled_surface = pygame.transform.smoothscale(canvas,(render_rect.width,render_rect.height))
    screen.fill((0,0,0))
    screen.blit(scaled_surface,(render_rect.x, render_rect.y))

    pygame.display.flip()
    clock.tick(constans.FPS)
pygame.quit()
sys.exit()