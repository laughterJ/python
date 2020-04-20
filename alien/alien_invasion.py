import pygame

from settings import Setting
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    common_setting = Setting()
    screen = pygame.display.set_mode((common_setting.screen_width, common_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    # 开始游戏主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(common_setting, screen, ship)


run_game()
