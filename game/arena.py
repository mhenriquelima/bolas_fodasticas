import pygame

ARENA_WIDTH = 600
ARENA_HEIGHT = 600

class Arena:
    def __init__(self, width=ARENA_WIDTH, height=ARENA_HEIGHT, screen=None):
        self.width = width
        self.height = height
        self.screen = screen if screen is not None else pygame.display.set_mode((width, height))
        self.x = (self.screen.get_width() - self.width) // 2
        self.y = (self.screen.get_height() - self.height) // 2
        pygame.display.set_caption("Arena de Batalha")

    def draw(self):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, (200, 200, 200), rect, 3)

    