import pygame
from pygame.sprite import Sprite


class Unit(Sprite):
    def __init__(self, window):
        super(Unit, self).__init__()
        self.window = window
        self.speed = 1
        self.p_width = 10
        self.rect = pygame.Rect(50, 50, self.p_width, self.p_width)
        self.left_hitbox = pygame.Rect(self.rect.x - 1, self.rect.y, 1, self.p_width)
        self.right_hitbox = pygame.Rect(self.rect.right, self.rect.y, 1, self.p_width)
        self.up_hitbox = pygame.Rect(self.rect.y - 1, self.rect.x, self.p_width, 1)
        self.right_hitbox = pygame.Rect(self.rect.right - 1, self.rect.y, self.p_width, 1)
        self.last_direction = 'r'
        self.last_position = (0, 0)
        self.weight = 0
        self.moves = []

    def draw(self):
        pygame.draw.rect(self.window, (240, 230, 140), self.rect)  # Draw player every frame

    def check_collision(self, maze):
        col = pygame.sprite.spritecollideany(self, maze)
        if col:
            if self.rect.right < col.rect.x + 3 * self.speed:
                self.rect.right = col.rect.x
            elif self.rect.x > col.rect.right - 3 * self.speed:
                self.rect.x = col.rect.right
            if self.rect.bottom < col.rect.y + 3 * self.speed:
                self.rect.bottom = col.rect.y
            elif self.rect.y > col.rect.bottom - 3 * self.speed:
                self.rect.y = col.rect.bottom
        self.weight = abs(self.rect.x - self.last_position[0]) + abs(self.rect.y - self.last_position[1])
        self.last_position = (self.rect.x, self.rect.y)
