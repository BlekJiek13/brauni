import pygame
import sys
from config import *
from grid import Grid
from exporter import save_grid_image, save_report

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Моделирование электорального процесса")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 16)

grid = Grid()

running = True
paused = True
step_mode = False

def draw_legend(surface, stats):
    legend_x = GRID_SIZE * CELL_SIZE + 10
    pygame.draw.rect(surface, (245, 245, 245), (GRID_SIZE * CELL_SIZE, 0, 200, SCREEN_HEIGHT))

    y = 10
    surface.blit(font.render(f"Итерация: {grid.iteration}", True, COLORS["text"]), (legend_x, y))
    y += 25
    surface.blit(font.render(f"Изм. в итерации: {round(grid.changes_last_round * 100, 2)}%", True, COLORS["text"]), (legend_x, y))

    y += 30
    surface.blit(font.render("", True, COLORS["text"]), (legend_x, y))
    y += 20
    for state, label in [(NEUTRAL, "Нейтральные"), (PARTY_A, "Партия А"), (PARTY_B, "Партия Б"), (PARTY_C, "Партия В")]:
        pygame.draw.rect(surface, COLORS[state], (legend_x, y, 20, 20))
        surface.blit(font.render(f"{label} ({stats[state]}%)", True, COLORS["text"]), (legend_x + 30, y))
        y += 30

def draw_buttons():
    button_labels = ["Старт", "Пауза", "Шаг", "Сброс", "Сохранить"]
    buttons = []
    start_y = SCREEN_HEIGHT - 200
    for i, label in enumerate(button_labels):
        rect = pygame.Rect(GRID_SIZE * CELL_SIZE + 20, start_y + i * 40, 160, 30)
        pygame.draw.rect(screen, (180, 180, 180), rect)
        pygame.draw.rect(screen, COLORS["text"], rect, 2)
        text_surf = font.render(label, True, COLORS["text"])
        screen.blit(text_surf, (rect.x + 10, rect.y + 5))
        buttons.append((label, rect))
    return buttons

# В начале файла, после создания grid добавьте:
stats_history = []

def handle_button_click(pos, buttons):
    global paused, step_mode, grid, stats_history
    for label, rect in buttons:
        if rect.collidepoint(pos):
            if label == "Старт":
                paused = False
                step_mode = False
            elif label == "Пауза":
                paused = True
            elif label == "Шаг":
                step_mode = True
                paused = False
            elif label == "Сброс":
                grid = Grid()
                stats_history = []  # Очищаем историю
                paused = True
            elif label == "Сохранить":  # Обрабатываем сохранение
                update_screen()
                save_grid_image(screen)  # Сохраняем изображение
                save_report(stats_history)  # Сохраняем отчёт

def update_screen():
    screen.fill((255, 255, 255))
    stats = grid.get_statistics()
    grid.draw(screen)
    draw_legend(screen, stats)
    draw_buttons()
    pygame.display.flip()

def check_termination():
    if grid.changes_last_round < MIN_CHANGE_THRESHOLD:
        return True
    return False

# Главный цикл
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_button_click(event.pos, draw_buttons())

    if not paused:
        grid.step()
        stats_history.append(list(grid.get_statistics().values()))  # Сохраняем статистику
        if step_mode:
            paused = True

    stats = grid.get_statistics()
    grid.draw(screen)
    draw_legend(screen, stats)
    draw_buttons()

    if check_termination():
        paused = True

    pygame.display.flip()
    
    update_screen()
    clock.tick(FPS)

pygame.quit()
sys.exit()