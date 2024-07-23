import src.macro as macro
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

def pause(screen):
    loop = 1
    font = pygame.font.SysFont("extra/font.ttf", macro.BLOCK_SIZE * 2)
    img = font.render('PAUSED', True, "white")
    screen.blit(img, ((macro.WIDTH / 2) - macro.BLOCK_SIZE * (len("PAUSED") / 2),
                    (macro.WIDTH / 2) - macro.BLOCK_SIZE * 2))
    font = pygame.font.SysFont("extra/font.ttf", macro.BLOCK_SIZE)
    img = font.render('Press Space or Escape to continue', True, "white")
    screen.blit(img, ((macro.WIDTH / 2) - macro.BLOCK_SIZE * 6,
                    (macro.WIDTH / 2)))
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = 0
                if event.key == pygame.K_SPACE:
                    screen.fill((0, 0, 0))
                    loop = 0
        pygame.display.update()