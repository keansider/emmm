import pygame
import sys
from settings import Settings
from bullet import Bullet
from ship import Ship
from alien import Alien

class AlienInvasion:
    def __init__(self):
        #初始化
        pygame.init()
        #导入设置
        self.settings = Settings()
        #屏幕
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        #设置背景色
        self.bg_color = (230,230,230)

        self.ship=Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()


    def run_game(self):
        #开始游戏
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #按下按键
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            #抬起按键
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        # 按下
        # 向右
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        # 向左
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        #按q退出
        if event.key == pygame.K_q:
            sys.exit()
        #按空格开火
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _update_bullets(self):
        # 删除子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

    def _fire_bullet(self):
        #开火
        if len(self.bullets)<self.settings.bullet_allowed:
            #有最大子弹开火限制
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

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
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()



if __name__ == '__main__':
    #运行游戏
    ai = AlienInvasion()
    ai.run_game()