import pygame

class Ship:
    def __init__(self,ai_game):
        # 初始化飞机位置
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # 加载图像
        self.image = pygame.image.load('C:/Users/路小/PycharmProjects/emmm/game/plant.png')
        self.rect = self.image.get_rect()


        self.settings = ai_game.settings
        # 放在底部中央
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False


    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right and self.rect.x<1000:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.x>=0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x