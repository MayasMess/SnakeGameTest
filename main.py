import pygame
import sys
from snake import Snake
from background import Background
from food import Food

pygame.init()
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
white = (255, 255, 255)
background = Background(surface=screen, screen_width=screen_width, screen_height=screen_height)
snake = Snake(surface=screen, screen_width=screen_width, screen_height=screen_height,
              bg_rect_height=background.rect_height)
food = Food(surface=screen, screen_width=screen_width, screen_height=screen_height,
            bg_rect_height=background.rect_height)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    snake.get_direction(keys=keys)
    snake.move()

    if snake.head_x_position == food.food_x_position and snake.head_y_position == food.food_y_position:
        snake.tail.append((snake.head_x_position, snake.head_y_position, snake.head_size, snake.head_size))
        food.new_position()

    # fill the screen and draw all elements
    screen.fill(white)
    background.draw()
    snake.draw()
    food.draw()
    snake.update_positions()

    pygame.display.update()
    clock.tick(15)
