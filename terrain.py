#terrain.py
import pygame
import random
import constans

class Terrain:
    def __init__(self):
        self.platforms = []
        self.last_x = constans.SCREEN_WIDTH
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
                max_offset = 150
                min_x = max(0, self.last_x - max_offset)
                max_x = min(constans.SCREEN_WIDTH - width, self.last_x + max_offset)
                if min_x > max_x:
                    min_x, max_x = 0, constans.SCREEN_WIDTH - width
                x= random.randint(min_x,max_x)

            new_plat = pygame.Rect(x,self.last_y,width,constans.PLATFORM_HEIGHT)
            self.platforms.append(new_plat)
            self.last_x = x+width // 2 

    def update(self, camera_y):
        if self.last_y > (camera_y-constans.SCREEN_HEIGHT):
            self.generate(10)

    def draw(self,surface,camera):
        for plat in self.platforms:
            pygame.draw.rect(surface, (50,150,50), camera.apply(plat))