class Setting:
    """通用设置类"""

    def __init__(self):
        # 屏幕 相关设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship 相关设置
        self.ship_speed = 18

        # bullet 相关设置
        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_limit = 8

        # 外星人相关设置
        self.alien_speed = 10
        self.fleet_drop_speed = 10
        # fleet_direction 为 1 表示右移，为 0 表示左移
        self.fleet_direction = 1
