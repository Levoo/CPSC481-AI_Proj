import pygame
from pygame.sprite import Sprite
import math
import random


class Unit(Sprite):
    def __init__(self, window, width, node, no, color, visited_nodes):
        super(Unit, self).__init__()
        self.window = window
        self.speed = 1
        self.p_width = width
        self.id_no = no
        self.color = color

        # Visited node = genes, visited_nodes = chromosome
        self.direction = None
        self.current_node = node
        self.next_node = None
        self.visited_nodes = visited_nodes[:]
        self.move_count = 0
        self.finished = False

        self.rect = pygame.Rect(self.current_node.y * self.p_width + self.p_width,
                                self.current_node.x * self.p_width + self.p_width, self.p_width, self.p_width)

        # Uses for calculating amount moved since last position and adds to weight,
        # then changes last position to current position. Weight = Fitness
        self.last_position = (self.rect.x, self.rect.y)
        self.weight = 0

        for key, value in self.current_node.neighbors.items():
            if value is not None:
                self.current_node.check_out[self.id_no][key] = True
                self.next_node = value
                self.direction = key

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)  # Draw player every frame

    def ai(self, parents):
        if not self.finished:
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
                    self.rect.x == self.next_node.y * self.p_width * 2 + self.p_width:
                if self.move_count >= len(self.visited_nodes) - 1 and self.next_node.isMazeEndNode is not True:
                    self.visited_nodes.append((self.next_node, self.direction))
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
                    self.weight += math.sqrt(math.pow(self.rect.y - self.last_position[1], 2) +
                                             math.pow(self.rect.x - self.last_position[0], 2))
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

                    if len(viable_moves) > 0:
                        select = random.randint(0, len(viable_moves) - 1)
                    else:
                        viable_moves.append(last_resort)
                        select = 0

                    self.next_node = viable_moves[select][1]
                    self.direction = viable_moves[select][0]
                    self.current_node.check_out[self.id_no][self.direction] = True
                elif self.next_node.isMazeEndNode is not True:
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
                    self.next_node = self.visited_nodes[self.move_count][0]
                    self.direction = self.visited_nodes[self.move_count][1]
                    self.current_node.check_out[self.id_no][self.direction] = True
                    self.weight += math.sqrt(math.pow(self.rect.y - self.last_position[1], 2) +
                                             math.pow(self.rect.x - self.last_position[0], 2))
                    self.last_position = (self.rect.x, self.rect.y)
                    if self.move_count >= len(self.visited_nodes) - 1:
                        self.visited_nodes.pop()

                else:
                    self.finished = True
                    self.visited_nodes.append((self.next_node, self.direction))
                    self.move_count += 1
                    self.weight += math.sqrt(math.pow(self.rect.y - self.last_position[1], 2) +
                                             math.pow(self.rect.x - self.last_position[0], 2))
                    parents.append(self)

    def reset(self, node):
        self.finished = False
        self.direction = None
        self.current_node = node
        self.next_node = None
        self.move_count = 0
        self.rect.topleft = (self.current_node.y * self.p_width + self.p_width, self.current_node.x * self.p_width + self.p_width)
        self.weight = 0
        self.last_position = (self.rect.x, self.rect.y)

        for key, value in self.current_node.neighbors.items():
            if value is not None:
                self.current_node.check_out[self.id_no][key] = True
                self.next_node = value
                self.direction = key
