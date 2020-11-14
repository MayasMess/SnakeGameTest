import pygame


class Snake:
    def __init__(self, surface, screen_width, screen_height, bg_rect_height):
        self.surface = surface
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.bg_rect_height = bg_rect_height
        self.head_size = 20
        self.velocity = 20
        self.head_x_position = 400
        self.head_y_position = 300
        self.direction = None
        self.tail = []

    def get_direction(self, keys):
        if keys[pygame.K_LEFT] and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if keys[pygame.K_RIGHT] and self.direction != 'LEFT':
            self.direction = 'RIGHT'
        if keys[pygame.K_UP] and self.direction != 'DOWN':
            self.direction = 'UP'
        if keys[pygame.K_DOWN] and self.direction != 'UP':
            self.direction = 'DOWN'

    def move(self):
        if self.direction == 'LEFT':
            self.head_x_position -= self.head_size
        if self.direction == 'RIGHT':
            self.head_x_position += self.head_size
        if self.direction == 'UP':
            self.head_y_position -= self.head_size
        if self.direction == 'DOWN':
            self.head_y_position += self.head_size
        if self.head_x_position > self.screen_width - self.head_size:
            self.head_x_position = 0
        if self.head_x_position < 0:
            self.head_x_position = self.screen_width - self.head_size
        if self.head_y_position < self.bg_rect_height:
            self.head_y_position = self.bg_rect_height
        if self.head_y_position > self.screen_height - self.head_size - self.bg_rect_height:
            self.head_y_position = self.screen_height - self.head_size - self.bg_rect_height

    def draw(self):
        pygame.draw.rect(surface=self.surface, color=pygame.Color('#42a5f5'),
                         rect=(self.head_x_position, self.head_y_position,
                               self.head_size, self.head_size))
        for pos in self.tail:
            pygame.draw.rect(surface=self.surface, color=pygame.Color('#42a5f5'),
                             rect=pos)

    def update_positions(self):
        new_tail = []
        if len(self.tail) != 0:
            for index in range(len(self.tail)):
                if index == 0:
                    new_tail.append((self.head_x_position, self.head_y_position, self.head_size, self.head_size))
                else:
                    new_tail.append(self.tail[index - 1])
            self.tail = new_tail
            print(new_tail)
