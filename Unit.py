import pygame
from pygame.sprite import Sprite
import math
import random


class Unit(Sprite):
    def __init__(self, window, width, node, no):
        super(Unit, self).__init__()
        self.window = window
        self.speed = 1
        self.p_width = width
        self.id_no = no

        # Visited node = genes, visited_nodes = chromosome
        self.direction = None
        self.current_node = node
        self.next_node = None
        self.visited_nodes = []
        self.move_count = 0

        self.rect = pygame.Rect(self.current_node.y * self.p_width + self.p_width,
                                self.current_node.x * self.p_width + self.p_width, self.p_width, self.p_width)

        # Uses for calculating amount moved since last position and adds to weight,
        # then changes last position to current position. Weight = Fitness
        self.last_position = (0, 0)
        self.weight = 0

        for key, value in self.current_node.neighbors.items():
            if value is not None:
                self.current_node.check_out[self.id_no][key] = True
                self.next_node = value
                self.direction = key
                print(self.current_node.x * self.p_width, " ", self.current_node.y * self.p_width)
                print(self.next_node.x * self.p_width, " ", self.next_node.y * self.p_width)

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
        if self.rect.y == self.next_node.x * self.p_width * 2 + self.p_width and \
                self.rect.x == self.next_node.y * self.p_width * 2ing  + self.p_width:
            self.visited_nodes.append(self.next_node)
            self.current_node = self.next_node
            if self.current_node.beenVisited[self.id_no][0] is False:
                if self.direction is "left":
                    self.current_node.beenVisited[self.id_no] = (True, "right")
                elif self.direction is "right":
                    self.current_node.beenVisited[self.id_no] = (True, "left")
                elif self.direction is "up":
                    self.current_node.beenVisited[self.id_no] = (True, "down")
                elif self.direction is "down":
                    self.current_node.beenVisited[self.id_no] = (True, "up")
            self.move_count += 1
            self.weight += math.sqrt(math.pow(self.rect.y - self.last_position[0], 2) +
                                     math.pow(self.rect.x - self.last_position[1], 2))
            self.last_position = (self.rect.x, self.rect.y)
            viable_moves = []
            last_resort = None

            for key, value in self.current_node.neighbors.items():
                if value is not None and self.current_node.check_out[self.id_no][key] is False:
                    if ((key is "up" and self.direction is not "down") or
                       (key is "down" and self.direction is not "up") or
                       (key is "left" and self.direction is not "right") or
                       (key is "right" and self.direction is not "left")) and \
                       key is not self.current_node.beenVisited[self.id_no][1]:
                        viable_moves.append((key, value))
                    else:
                        last_resort = (key, value)

            if len(viable_moves) > 1:
                select = random.randrange(len(viable_moves) - 1)
            elif len(viable_moves) is 1:
                select = 0
            else:
                viable_moves.append(last_resort)
                select = 0

            self.next_node = viable_moves[select][1]
            self.direction = viable_moves[select][0]
            self.current_node.check_out[self.id_no][self.direction] = True

            for key, value in self.current_node.neighbors.items():
                print(self.direction, " ", key, " ", value, " ", self.current_node.check_out[self.id_no][key])

