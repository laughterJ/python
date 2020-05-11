import sys
import pygame
from bullet import Bullet
from alien import Alien


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


def create_aliens(screen, common_setting, aliens, ship):
    """创建外星人群"""
    # 创建一个Alien对象，获取它的宽高
    alien = Alien(screen, common_setting)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    # 计算一行可容纳的外星人数量
    number_alien_x = get_aliens_number_x(screen, common_setting, alien_width)
    # 计算可容纳外星人行数
    number_alien_y = get_aliens_number_y(screen, common_setting, alien_height, ship.rect.height)

    # 创建第一行外星人
    for row_number in range(number_alien_y):
        for alien_number in range(number_alien_x):
            create_alien(screen, common_setting, aliens, alien_number, row_number)


def get_aliens_number_x(screen, common_setting, alien_width):
    # 计算一行中可以用来绘制外星人的宽度
    available_space_x = common_setting.screen_width - alien_width
    # 根据行宽计算可以绘制的外星人数量
    number_alien_x = int(available_space_x / (1.6 * alien_width))
    return number_alien_x


def get_aliens_number_y(screen, common_setting, alien_height, ship_height):
    # 计算可用来绘制外星人的高度
    available_space_y = common_setting.screen_height - ship_height - 2 * alien_height
    # 根据高度计算可绘制外星人行数
    number_alien_y = int(available_space_y / (1.6 * alien_height))
    return number_alien_y


def create_alien(screen, common_setting, aliens, alien_number, row_number):
    alien = Alien(screen, common_setting)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.rect.x = alien_width + 1.6 * alien_width * alien_number
    alien.rect.y = 0.2 * alien_height + 1.6 * alien_height * row_number
    aliens.add(alien)


def update_bullets(bullets):
    """更新子弹位置，并删除已消失子弹"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_screen(common_setting, screen, ship, aliens, bullets):
    screen.fill(common_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.draw()
    aliens.draw(screen)
    pygame.display.flip()


def update_aliens(aliens):
    """更新外星人位置"""
    aliens.update()
