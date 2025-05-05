GRID_SIZE = 40
CELL_SIZE = 15
SCREEN_WIDTH = GRID_SIZE * CELL_SIZE + 200  # Доп. место для легенды
SCREEN_HEIGHT = GRID_SIZE * CELL_SIZE
FPS = 10

# Состояния ячеек
NEUTRAL = 0
PARTY_A = 1
PARTY_B = 2
PARTY_C = 3

# Цвета
COLORS = {
    NEUTRAL: (255, 255, 255),   # белый
    PARTY_A: (0, 102, 204),     # синий
    PARTY_B: (204, 0, 0),       # красный
    PARTY_C: (0, 153, 0),       # зелёный
    "grid": (200, 200, 200),
    "text": (0, 0, 0)
}

# Начальные проценты
INITIAL_DISTRIBUTION = {
    NEUTRAL: 0.4,
    PARTY_A: 0.3,
    PARTY_B: 0.2,
    PARTY_C: 0.1
}

# Вероятность случайной смены мнения
RANDOM_FLIP_PROBABILITY = 0.01

# Порог минимальных изменений для остановки
MIN_CHANGE_THRESHOLD = 0.01
