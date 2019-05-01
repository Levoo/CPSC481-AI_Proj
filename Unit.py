import pygame
from pygame.sprite import Sprite
import math
import random


class Unit(Sprite):
    def __init__(self, window, node):
        super(Unit, self).__init__()
        self.window = window
        self.speed = 1
        self.p_width = 20
        self.rect = pygame.Rect(0, 20, self.p_width, self.p_width)

        # Visited node = genes, visited_nodes = chromosome
        self.direction = None
        self.current_node = node
        self.next_node = None
        self.visited_nodes = []
        self.move_count = 0

        # Uses for calculating amount moved since last position and adds to weight,
        # then changes last position to current position. Weight = Fitness
        self.last_position = (0, 0)
        self.weight = 0

    def draw(self):
        pygame.draw.rect(self.window, (240, 230, 140), self.rect)  # Draw player every frame

    def ai(self):
        if self.direction == "up":
            self.rect = self.rect.move(0, -self.speed)
        elif self.direction == "down":
            self.rect = self.rect.move(0, self.speed)
        elif self.direction == "left":
            self.rect = self.rect.move(-self.speed, 0)
        elif self.direction == "right":
            self.rect = self.rect.move(self.speed, 0)

        # Next move if node is hit
        if self.rect.x == self.next_node.location_x and self.rect.y == self.next_node.location_y:
            self.current_node = self.next_node
            self.visited_nodes.append(self.next_node)
            self.move_count += 1
            self.weight += math.sqrt(math.pow(self.rect.x - self.last_position[0], 2) +
                                     math.pow(self.rect.y - self.last_position[1], 2))
            self.last_position = (self.rect.x, self.rect.y)
            viable_moves = []
            count = 0
            for key, value in self.current_node.neighbors:
                if value is not None and self.current_node.visits[count] is False:
                    viable_moves.append(value)
            self.next_node = viable_moves[random.randrange(len(viable_moves) - 1)]
