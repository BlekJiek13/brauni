import pygame
import os
import matplotlib.pyplot as plt
from datetime import datetime

EXPORT_DIR = "exports"
os.makedirs(EXPORT_DIR, exist_ok=True)

def save_grid_image(surface):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(EXPORT_DIR, f"grid_{now}.png")
    pygame.image.save(surface, path)
    print(f"Изображение сохранено: {path}")
    return path

def save_report(stats_history):
    if not stats_history:
        print("Нет данных для построения отчёта.")
        return

    iterations = list(range(len(stats_history)))
    neutral = [stats[0] for stats in stats_history]
    party_a = [stats[1] for stats in stats_history]
    party_b = [stats[2] for stats in stats_history]
    party_c = [stats[3] for stats in stats_history]

    plt.figure(figsize=(10, 6))
    plt.plot(iterations, neutral, label="Нейтральные", color="gray")
    plt.plot(iterations, party_a, label="Партия А", color="red")
    plt.plot(iterations, party_b, label="Партия Б", color="blue")
    plt.plot(iterations, party_c, label="Партия В", color="green")

    plt.xlabel("Итерации")
    plt.ylabel("Процент избирателей")
    plt.title("Динамика электоральных предпочтений")
    plt.legend()
    plt.grid(True)

    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(EXPORT_DIR, f"report_{now}.png")
    plt.savefig(path)
    plt.close()
    print(f"Отчётный график сохранён: {path}")
    return path