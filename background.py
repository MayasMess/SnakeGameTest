import pygame


class Background:
    def __init__(self, surface, screen_width, screen_height):
        self.surface = surface
        self.rect_height = 60
        self.top_rect_pos = (0, 0, screen_width, self.rect_height)
        self.bot_rect_pos = (0, screen_height - self.rect_height, screen_width, self.rect_height)
        self.bg_color = pygame.Color('#ffcdd2')

    def draw(self):
        pygame.draw.rect(surface=self.surface, color=self.bg_color, rect=self.top_rect_pos)
        pygame.draw.rect(surface=self.surface, color=self.bg_color, rect=self.bot_rect_pos)
