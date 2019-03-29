import pygame
from pygame.sprite import Sprite


class Wall(Sprite):
    def __init__(self, window, x, y, width, height, color):
        super(Wall, self).__init__()
        self.window = window
        self.p_width = width
        self.p_height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)
