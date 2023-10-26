import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #发射子弹
    def __init__(self,ai_game):
        #创建对象
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        #在（0，0）处创造一个子弹，然后移到飞机的位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        #向上发射子弹
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        #绘制子弹
        pygame.draw.rect(self.screen,self.color,self.rect)