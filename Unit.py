import pygame
from pygame.sprite import Sprite
import random


class Unit(Sprite):
    def __init__(self, window):
        super(Unit, self).__init__()
        self.window = window
        self.speed = 1
        self.p_width = 20
        self.rect = pygame.Rect(20, 20, self.p_width, self.p_width)

        # Hitboxes for checking cardinal directions
        self.left_hitbox = LeftHitbox(self.rect.x - 1, self.rect.y, 1, self.p_width)
        self.right_hitbox = RightHitbox(self.rect.right, self.rect.y, 1, self.p_width)
        self.up_hitbox = UpHitbox(self.rect.x, self.rect.y - 1, self.p_width, 1)
        self.down_hitbox = DownHitbox(self.rect.x, self.rect.bottom, self.p_width, 1)

        # For choosing the next direction, direction = x, y vector
        # Stores last_direction in moves, directions = genes, moves = chromosome
        self.last_direction = (1 * self.speed, 0)
        self.moves = []
        self.move_count = 0

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
        return col

    def ai(self, maze):
        self.rect = self.rect.move(self.last_direction[0], self.last_direction[1])
        collision = self.check_collision(maze)

        # Next move if wall is hit
        if collision and self.move_count + 1 < len(self.moves):
            self.last_direction = self.moves[self.move_count]
            self.move_count += 1
        elif collision:
            self.left_hitbox.rect.x, self.left_hitbox.rect.y = self.rect.x - 1, self.rect.y
            self.right_hitbox.rect.x, self.right_hitbox.rect.y = self.rect.right, self.rect.y
            self.up_hitbox.rect.x, self.up_hitbox.rect.y = self.rect.x, self.rect.y - 1
            self.down_hitbox.rect.x, self.down_hitbox.rect.y = self.rect.x, self.rect.bottom
            if self.last_direction[0]:
                choices = []
                if not pygame.sprite.spritecollideany(self.up_hitbox, maze):
                    choices.append(-1)
                if not pygame.sprite.spritecollideany(self.down_hitbox, maze):
                    choices.append(1)
                self.last_direction = (0, random.choice(choices) * self.speed)
            elif self.last_direction[1]:
                choices = []
                if not pygame.sprite.spritecollideany(self.left_hitbox, maze):
                    choices.append(-1)
                if not pygame.sprite.spritecollideany(self.right_hitbox, maze):
                    choices.append(1)
                self.last_direction = (random.choice(choices) * self.speed, 0)
            self.moves.append(self.last_direction)
            self.move_count += 1


class LeftHitbox(Sprite):
    def __init__(self, x, y, width, height):
        super(LeftHitbox, self).__init__()
        self.rect = pygame.Rect(x, y, width, height)


class RightHitbox(Sprite):
    def __init__(self, x, y, width, height):
        super(RightHitbox, self).__init__()
        self.rect = pygame.Rect(x, y, width, height)


class UpHitbox(Sprite):
    def __init__(self, x, y, width, height):
        super(UpHitbox, self).__init__()
        self.rect = pygame.Rect(x, y, width, height)


class DownHitbox(Sprite):
    def __init__(self, x, y, width, height):
        super(DownHitbox, self).__init__()
        self.rect = pygame.Rect(x, y, width, height)
