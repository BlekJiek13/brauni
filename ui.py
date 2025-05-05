import pygame
from config import *

pygame.font.init()
FONT = pygame.font.SysFont("Arial", 16)

class UIButton:
    def __init__(self, text, x, y, width=160, height=30):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (180, 180, 180)
        self.text_color = COLORS["text"]

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, self.text_color, self.rect, 2)
        text_surf = FONT.render(self.text, True, self.text_color)
        surface.blit(text_surf, (self.rect.x + 10, self.rect.y + 5))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

class UIManager:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        labels = ["Старт", "Пауза", "Шаг", "Сброс", "Режим"]
        start_y = SCREEN_HEIGHT - 200
        for i, label in enumerate(labels):
            btn = UIButton(label, GRID_SIZE * CELL_SIZE + 20, start_y + i * 40)
            self.buttons.append(btn)

    def draw(self):
        for btn in self.buttons:
            btn.draw(self.screen)

    def get_clicked(self, pos):
        for btn in self.buttons:
            if btn.is_clicked(pos):
                return btn.text
        return None

def draw_legend(surface, stats, iteration):
    legend_x = GRID_SIZE * CELL_SIZE + 10
    pygame.draw.rect(surface, (245, 245, 245), (GRID_SIZE * CELL_SIZE, 0, 200, SCREEN_HEIGHT))

    y = 10
    surface.blit(FONT.render(f"Итерация: {iteration}", True, COLORS["text"]), (legend_x, y))
    y += 25
    surface.blit(FONT.render(f"Изм. в итерации: {round(stats['changes'], 2)}%", True, COLORS["text"]), (legend_x, y))

    y += 30
    surface.blit(FONT.render("Легенда:", True, COLORS["text"]), (legend_x, y))
    y += 20
    for state, label in [(NEUTRAL, "Нейтральные"), (PARTY_A, "Партия А"), (PARTY_B, "Партия Б"), (PARTY_C, "Партия В")]:
        pygame.draw.rect(surface, COLORS[state], (legend_x, y, 20, 20))
        surface.blit(FONT.render(f"{label} ({stats[state]}%)", True, COLORS["text"]), (legend_x + 30, y))
        y += 30
