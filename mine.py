import pygame
import pygame.draw as draw


class Mine():
    def __init__(self):
        self.totalMines = 0
        self.minesList = []
        self.window_w = 640
        self.window_h = 400
        self.screen = pygame.display.set_mode((self.window_w,self.window_h))
        
        self.mine_size = 20

        self.mineField_rows = 30
        self.mineField_cols = 30

        w = self.mineField_rows * self.mine_size
        h = self.mineField_cols * self.mine_size
        self.mineField = pygame.Surface((w,h))