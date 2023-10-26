import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('C:/Users/路小/PycharmProjects/emmm/game/master.png')
        self.rect = self.image.get_rect()

        #在左上角刷新怪兽
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.rect.x = float(self.rect.x)