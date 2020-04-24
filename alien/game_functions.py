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
        fire_bullet(screen, common_setting, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup_events(event, ship):
    """响应按键松开事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def fire_bullet(screen, common_setting, ship, bullets):
    """如果未达到子弹上限，就发射一颗子弹"""
    if len(bullets) < common_setting.bullet_limit:
        new_bullet = Bullet(screen, common_setting, ship)
        bullets.add(new_bullet)


def update_bullets(bullets):
    """更新子弹位置，并删除已消失子弹"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_screen(common_setting, screen, ship, alien, bullets):
    screen.fill(common_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.draw()
    alien.draw()
    pygame.display.flip()
