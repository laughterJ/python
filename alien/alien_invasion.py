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
    aliens = Group()
    gf.create_aliens(screen, common_setting, aliens, ship)

    # 开始游戏主循环
    while True:
        gf.check_events(common_setting, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(aliens)
        gf.update_screen(common_setting, screen, ship, aliens, bullets)


run_game()
