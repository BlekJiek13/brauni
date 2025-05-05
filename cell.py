import random
import pygame
from config import *

class Cell:
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state
        self.next_state = state

    def draw(self, surface):
       
        rect = pygame.Rect(self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, COLORS[self.state], rect)
        pygame.draw.rect(surface, COLORS["grid"], rect, 1)

    def update_state(self):
        self.state = self.next_state

    def random_flip(self):
        if self.state == NEUTRAL and random.random() < RANDOM_FLIP_PROBABILITY:
            self.next_state = random.choices([PARTY_A, PARTY_B, PARTY_C], [0.4, 0.3, 0.3])[0]