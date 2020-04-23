import pygame


class Ship:
    def __init__(self, screen, common_setting):
        self.screen = screen

        self.common_setting = common_setting
        self.image = pygame.image.load("images/iron.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.center += self.common_setting.ship_speed
        if self.moving_left and self.rect.left >= 0:
            self.center -= self.common_setting.ship_speed
        self.rect.centerx = self.center

    def draw(self):
        self.screen.blit(self.image, self.rect)
