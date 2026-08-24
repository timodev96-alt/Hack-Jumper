#debug.py
import pygame
import constans

import camera

pygame.font.init()
font = pygame.font.SysFont("Arial", 24)

def draw_debugger(surface, camera_y):
    if constans.DEBUG_MODE == True:
        text_surf = font.render(f"Y: {int(camera_y)}",True, (255,255,255))
        surface.blit(text_surf, (10,10))

def handel_debug_input(camera):
    if constans.DEBUG_MODE == True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]: camera.move(-7)
        if keys[pygame.K_DOWN] : camera.move(6)

def draw_debug_info(surface,camera):
    if constans.DEBUG_MODE == True:
        debug_text = f"Y:{int(camera.y)}"
        text_surface = font.render(debug_text,True,(255,255,255))
        surface.blit(text_surface, (10,10))