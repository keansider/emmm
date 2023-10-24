import pygame
import sys
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        #初始化
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        #设置背景色
        self.bg_color = (230,230,230)

        self.ship=Ship(self)

    def run_game(self):
        #开始游戏
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        # 按下
        if event.key == pygame.K_RIGHT:
            # 向右
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            # 向右
            self.ship.moving_left = True
            #按q退出
        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        # 抬起
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        # 刷新屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()



if __name__ == '__main__':
    #运行游戏
    ai = AlienInvasion()
    ai.run_game()