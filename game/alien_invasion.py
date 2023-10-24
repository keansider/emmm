import pygame
import sys


class AlienInvasion:
    def __init__(self):
        #初始化
        pygame.init()

        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        #设置背景色
        self.bg_color=(230,230,230)

    def run_game(self):
        #开始游戏
        while True:
            #监听键盘和鼠标事件
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    sys.exit()
            #刷新屏幕
            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__=='__main__':
    #运行游戏
    ai=AlienInvasion()
    ai.run_game()