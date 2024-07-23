from src.window import exit_window, display_on_window
from src.classes import Apple, Snake
import src.macro as macro
from src.check_flags import check_flags
import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

def drawGrid(screen):
    for x in range(0, macro.WIDTH, macro.BLOCK_SIZE):
        for y in range(0, macro.HEIGHT, macro.BLOCK_SIZE):
            rect = pygame.Rect(x, y, macro.BLOCK_SIZE, macro.BLOCK_SIZE)
            pygame.draw.rect(screen, "#3c3c3b", rect, 1)

def snake_game(level, name):
    pygame.init()
    FONT = pygame.font.Font("extra/font.ttf", macro.BLOCK_SIZE * 2)
    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    score = FONT.render("1", True, "white")
    snake = Snake()
    apple = Apple(snake.body)
    pygame.display.set_caption("Snake!")
    while True:
        score = FONT.render(f"{len(snake.body) + 1}", True, "white")
        exit_window(snake, level, name, screen)
        screen.fill('black')
        apple = snake.update_snake(apple)
        drawGrid(screen)
        display_on_window(screen, apple, snake, score)
        clock.tick(level)

def main():
    info_flags = [4, "No name", True]
    if len(sys.argv) >= 2:
        info_flags = check_flags(sys.argv, info_flags)
    try:
        if info_flags[2] == False:
            raise KeyboardInterrupt
        snake_game(info_flags[0], info_flags[1])
    except KeyboardInterrupt:
        exit(0)

if __name__ == "__main__":
    main()