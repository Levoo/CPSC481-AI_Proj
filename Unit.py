import pygame
from pygame.sprite import Sprite


class Unit(Sprite):
    def __init__(self, window):
        super(Unit, self).__init__()
        self.window = window
        self.speed = 1
        self.p_width = 20
        self.rect = pygame.Rect(0, 0, self.p_width, self.p_width)

        # Hitboxes for checking cardinal directions
        self.left_hitbox = pygame.Rect(self.rect.x - 1, self.rect.y, 1, self.p_width)
        self.right_hitbox = pygame.Rect(self.rect.right, self.rect.y, 1, self.p_width)
        self.up_hitbox = pygame.Rect(self.rect.y - 1, self.rect.x, self.p_width, 1)
        self.right_hitbox = pygame.Rect(self.rect.right - 1, self.rect.y, self.p_width, 1)

        # For choosing the next direction(l = left, r = right, u = up, d = down
        # Stores last_direction in moves, directions = genes, moves = chromosome
        self.last_direction = 'r'
        self.moves = []

        # Uses for calculating amount moved since last position and adds to weight,
        # then changes last position to current position. Weight = Fitness
        self.last_position = (0, 0)
        self.weight = 0

    def draw(self):
        pygame.draw.rect(self.window, (240, 230, 140), self.rect)  # Draw player every frame

    def check_collision(self, maze):
        # Checks whether the unit collides with any of the maze walls, if so, returns wall it collided with.
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

        # Equation measuring distance moved since last position, after colliding with a wall.
        # Updates the last_position as current position
        self.weight = abs(self.rect.x - self.last_position[0]) + abs(self.rect.y - self.last_position[1])
        self.last_position = (self.rect.x, self.rect.y)
