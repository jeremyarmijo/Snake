import src.macro as macro
import sys
from src.ascii_art import print_ascii_art
from src.pause import pause
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

def p_score_and_save(score, level, name):
    with open('scoreboard/scoreboard.csv', "a") as f:
        f.write(str(level - 3) + "," + name + "," + str(score) + "\n")
    print_ascii_art("Good Game", "slant")
    print("Your score is", score)

def check_moves(event, snake, screen):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            pause(screen)
        if event.key == pygame.K_DOWN and snake.dir != macro.UP:
            snake.dir = macro.DOWN
        elif event.key == pygame.K_UP and snake.dir != macro.DOWN:
            snake.dir = macro.UP
        elif event.key == pygame.K_RIGHT and snake.dir != macro.LEFT:
            snake.dir = macro.RIGHT
        elif event.key == pygame.K_LEFT and snake.dir != macro.RIGHT:
            snake.dir = macro.LEFT

def exit_window(snake, level, name, screen):
    for event in pygame.event.get():
        check_moves(event, snake, screen)
        if event.type == pygame.QUIT:
            p_score_and_save(len(snake.body) + 1, level, name)
            pygame.quit()
            sys.exit()
    if snake.nb_dead != 0:
        p_score_and_save(len(snake.body) + 1, level, name)
        pygame.quit()
        sys.exit()

def display_on_window(screen, apple, snake, score):
    pygame.draw.rect(screen, "red", apple.rectangle)
    pygame.draw.rect(screen, "green", snake.head)
    for square in snake.body:
        pygame.draw.rect(screen, "green", square)
    screen.blit(score, score.get_rect(center=(macro.WIDTH / 2, macro.HEIGHT / 20)))
    pygame.display.update()
