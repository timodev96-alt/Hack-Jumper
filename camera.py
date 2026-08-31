#camera.py
import pygame

class Camera:
    def __init__(self):
        self.y = 0
        self.min_y = 49

    def apply(self,rect):
        return rect.move(0, -self.y)

    def move(self, amount):
        self.y += amount
        if self.y > self.min_y:
            self.y = self.min_y

    def follow(self, target_y , offset):
        new_y = target_y - offset
        if new_y> self.min_y:
            new_y = self.min_y
        self.y = new_y