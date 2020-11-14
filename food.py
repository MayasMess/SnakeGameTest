import pygame
import random
from snake import Snake


class Food(Snake):
    def __init__(self, surface, screen_width, screen_height, bg_rect_height):
        super().__init__(surface, screen_width, screen_height, bg_rect_height)
        self.color = pygame.Color('#81c784')
        self.food_x_position = random.randint(0, self.screen_width / self.head_size) * self.head_size
        self.food_y_position = random.randint(self.bg_rect_height / self.head_size,
                                              (self.screen_height - self.bg_rect_height) / self.head_size) * self.head_size
        self.rect_pos = (self.food_x_position, self.food_y_position, self.head_size, self.head_size)

    def draw(self):
        pygame.draw.rect(surface=self.surface, color=self.color, rect=self.rect_pos)

    def new_position(self):
        self.food_x_position = random.randint(0, self.screen_width / self.head_size) * self.head_size
        self.food_y_position = random.randint(self.bg_rect_height / self.head_size,
                                              (self.screen_height - self.head_size - self.bg_rect_height) /
                                              self.head_size) * self.head_size
        self.rect_pos = (self.food_x_position, self.food_y_position, self.head_size, self.head_size)
