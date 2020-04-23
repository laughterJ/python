import sys
import pygame
from bullet import Bullet


def check_events(common_setting, screen, ship, bullets):
    """响应鼠标和键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, common_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, common_setting, screen, ship, bullets):
    """响应按键按下事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(screen, common_setting, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """响应按键松开事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(common_setting, screen, ship, bullets):
    screen.fill(common_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.draw()
    pygame.display.flip()
