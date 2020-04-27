import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, screen, commom_setting):
        """初始化外星人，并设置其起始位置"""
        super().__init__()
        self.screen = screen
        self.common_setting = commom_setting

        # 加载外星人图像，并设置其 rect 属性
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width * 0.1
        self.rect.y = self.rect.height * 0.1

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def draw(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)
