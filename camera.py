#camera.py
import pygame

class Camera:
    def __init__(self):
        self.y = 0

    def apply(self,rect):
        return rect.move(0, -self.y)

    def move(self, amount):
        self.y += amount