import pygame
from pygame.sprite import Sprite


class Wall(Sprite):
    def __init__(self, window):
        super(Wall, self).__init__()
        self.window = window
        self.p_width = 10
        self.rect = pygame.Rect(40, 40, 20, 20)

    def draw(self):
        pygame.draw.rect(self.window, (240, 140, 230), self.rect)
