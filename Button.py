import pygame


class Button:
    def __init__(self, screen, msg, x, y):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.x = x
        self.y = y

        self.width, self.height = 200, 50
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.border_rect = pygame.Rect(0, 0, self.width + 4, self.height + 4)
        self.select_rect1 = pygame.Rect(0, 0, self.width, self.height)
        self.select_rect2 = pygame.Rect(0, 0, self.width + 2, self.height + 2)
        self.rect.center, self.border_rect.center, self.select_rect2.center = (x, y), (x, y), (x, y)
        self.select_rect1.center = (x - 1, y - 1)
        self.button_color = (127, 127, 127)
        self.border_color = (0, 0, 0)
        self.text_color = (0, 0, 0)
        self.select_color2 = (90, 90, 90)
        self.select_color1 = (190, 190, 190)
        self.font = pygame.font.SysFont(None, 36)

        self.pressed = False
        self.msg = msg
        self.msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.centerx = x
        self.msg_rect.centery = y

    def prep_msg(self):
        self.msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.centerx = self.x
        self.msg_rect.centery = self.y

    def prep_msg_highlight(self):
        self.msg_image = self.font.render(self.msg, True, self.button_color, self.text_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.centerx = self.x
        self.msg_rect.centery = self.y

    def draw(self):
        self.screen.fill(self.border_color, self.border_rect)
        if not self.pressed:
            self.screen.fill(self.select_color2, self.select_rect2)
            self.screen.fill(self.select_color1, self.select_rect1)
        else:
            self.screen.fill(self.select_color1, self.select_rect2)
            self.screen.fill(self.select_color2, self.select_rect1)
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_rect)
