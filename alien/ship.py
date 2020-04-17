import pygame


class Ship:
    def __init__(self, screen):
        """初始化飞船"""
        self.screen = screen
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def draw(self):
        self.screen.blit(self.image, self.rect)
