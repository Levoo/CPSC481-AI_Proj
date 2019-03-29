import pygame
from pygame.sprite import Sprite


class Wall(Sprite):
    def __init__(self, window, x, y, width, height, color):
        super(Wall, self).__init__()
        self.window = window
<<<<<<< HEAD
        self.p_width = 5
        self.rect = pygame.Rect(0, 0, self.p_width, 720)
        #self.rect = pygame.Rect(0, 0, 20, 20) og cube 
        self.wallColor = (240, 140, 230)

    def draw(self, newWall=None):
        if newWall is None:
            newWall = self.rect
        else:
            self.rect = newWall
        #for wall in self.rect:
        pygame.draw.rect(self.window, self.wallColor, self.rect)
=======
        self.p_width = width
        self.p_height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)
>>>>>>> e96b04733c8cec87c44cad3480f5d55b1c47b69f
