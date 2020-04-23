import pygame
from pygame.sprite import Group
from settings import Setting
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    common_setting = Setting()
    screen = pygame.display.set_mode((common_setting.screen_width, common_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen, common_setting)
    bullets = Group()

    # 开始游戏主循环
    while True:
        gf.check_events(common_setting, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(common_setting, screen, ship, bullets)


run_game()
