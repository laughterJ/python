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
