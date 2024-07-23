from random import randint
import src.macro as macro
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class Apple:
    def __init__(self, snake):
        self.rectangle = pygame.Rect(int(randint(0, macro.WIDTH) / macro.BLOCK_SIZE) * macro.BLOCK_SIZE,
                                    int(randint(0, macro.WIDTH) / macro.BLOCK_SIZE) * macro.BLOCK_SIZE,
                                    macro.BLOCK_SIZE, macro.BLOCK_SIZE)
        if self.rectangle in snake:
            for self.rectangle in snake:
                self.rectangle = pygame.Rect(int(randint(0, macro.WIDTH) / macro.BLOCK_SIZE) * macro.BLOCK_SIZE,
                                            int(randint(0, macro.WIDTH) / macro.BLOCK_SIZE) * macro.BLOCK_SIZE,
                                            macro.BLOCK_SIZE, macro.BLOCK_SIZE)

class Snake:
    def __init__(self):
        self.dir = 1
        self.nb_dead = 0
        self.head = pygame.Rect(macro.BLOCK_SIZE, macro.BLOCK_SIZE, macro.BLOCK_SIZE, macro.BLOCK_SIZE)
        self.body = [pygame.Rect(0, macro.BLOCK_SIZE, macro.BLOCK_SIZE, macro.BLOCK_SIZE)]

    def snake_dead(self):
        if self.head in self.body:
            self.nb_dead += 1
        if self.head.x < 0 or self.head.x > macro.WIDTH:
            self.nb_dead += 1
        if self.head.y < 0 or self.head.y > macro.WIDTH:
            self.nb_dead += 1
        return self

    def update_body(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x, self.body[i].y = self.body[i - 1].x, self.body[i - 1].y
        self.body[0] = pygame.Rect.copy(self.head)

    def snake_dir(self, rect):
        if self.dir == macro.DOWN:
            rect.y = rect.y + macro.BLOCK_SIZE
        elif self.dir == macro.UP:
            rect.y = rect.y - macro.BLOCK_SIZE
        elif self.dir == macro.RIGHT:
            rect.x = rect.x + macro.BLOCK_SIZE
        elif self.dir == macro.LEFT:
            rect.x = rect.x - macro.BLOCK_SIZE

    def update_snake(self, apple):
        self.update_body()
        if self.head == apple.rectangle:
            self.body.append(pygame.Rect(self.head.x, self.head.y, macro.BLOCK_SIZE, macro.BLOCK_SIZE))
            apple = Apple(self.body)
        self.snake_dir(self.head)
        self.snake_dead()
        return apple
