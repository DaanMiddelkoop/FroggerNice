import pygame

HEIGHT = 10
WIDTH = 10
X_OFFSET = 450
Y_OFFSET = 200

class Tiles:
    color = None
    memory = None
    solid = None

    def __init__(self, file_index):
        img = pygame.image.load("world" + str(file_index) + ".png")

        self.grid = [[img.get_at((y, x)) for x in range(WIDTH)] for y in range(HEIGHT)]
        self.memory = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
        self.solid = [[0 if img.get_at((y, x)) == (255, 255, 255) else 1 for x in range(WIDTH)] for y in range(HEIGHT)]

    def draw(self, offset, screen):
        for y in range(HEIGHT):
            for x in range(WIDTH):
                pygame.draw.rect(screen, self.grid[x][y], (X_OFFSET + x * 32, Y_OFFSET + y * 32 + (HEIGHT * offset * 32), 32, 32))



