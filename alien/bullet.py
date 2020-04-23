import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """子弹管理类"""

    def __init__(self, screen, common_setting, ship):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, common_setting.bullet_width, common_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = common_setting.bullet_color
        self.speed = common_setting.bullet_speed

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
