import pygame

from Tiles import X_OFFSET, Y_OFFSET

class Frog:
    field = None
    x = 0
    y = 0

    def __init__(self, x, y, field):
        self.x = x
        self.y = y
        self.field = field

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x * 32 + X_OFFSET, Y_OFFSET + 9*32, 32, 32))


