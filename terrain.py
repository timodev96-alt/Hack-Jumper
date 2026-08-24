#terrain.py
import pygame
import random
import constans

class Terrain:
    def __init__(self):
        self.platforms = []
        self.last_y = constans.SCREEN_HEIGHT

        floor = pygame.Rect(0, constans.SCREEN_HEIGHT - 20, constans.SCREEN_WIDTH, 20)
        self.platforms.append(floor)

        self.generate(20)

    def generate(self,count):
        for i in range(count):
            self.last_y -= constans.VERTICAL_GAP
            if self.last_y %1500 == 0 and self.last_y != 0:
                width = constans.SCREEN_WIDTH
                x=0
            else:
                width = random.randint(120,200)
                x= random.randint(0, constans.SCREEN_WIDTH-width)

            new_plat = pygame.Rect(x,self.last_y,width,constans.PLATFORM_HEIGHT)
            self.platforms.append(new_plat)

    def update(self, camera_y):
        if self.last_y > (camera_y-constans.SCREEN_HEIGHT):
            self.generate(10)
        self.platforms = [p for p in self.platforms if p.y < camera_y + constans.SCREEN_HEIGHT + 500]

    def draw(self,surface,camera):
        for plat in self.platforms:
            pygame.draw.rect(surface, (50,150,50), camera.apply(plat))