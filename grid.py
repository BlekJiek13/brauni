import random
from cell import Cell
from config import *

class Grid:
    def __init__(self):
        self.grid = []
        self.iteration = 0
        self.changes_last_round = 1.0
        self.init_grid()

    def init_grid(self):
        total = GRID_SIZE * GRID_SIZE
        counts = {k: int(v * total) for k, v in INITIAL_DISTRIBUTION.items()}
        states = [s for s, count in counts.items() for _ in range(count)]
        random.shuffle(states)

        self.grid = [[Cell(x, y, states[y * GRID_SIZE + x]) for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]

    def draw(self, surface):
        for row in self.grid:
            for cell in row:
                cell.draw(surface)

    def get_neighbors(self, x, y):
        neighbors = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                    neighbors.append(self.grid[ny][nx])
        return neighbors

    def step(self):
        changes = 0
        for row in self.grid:
            for cell in row:
                neighbors = self.get_neighbors(cell.x, cell.y)
                counts = {NEUTRAL: 0, PARTY_A: 0, PARTY_B: 0, PARTY_C: 0}
                for n in neighbors:
                    counts[n.state] += 1

                # Правила
                if cell.state == NEUTRAL:
                    max_party = max((PARTY_A, PARTY_B, PARTY_C), key=lambda p: counts[p])
                    if counts[max_party] >= 4:
                        cell.next_state = max_party
                    elif random.random() < RANDOM_FLIP_PROBABILITY:
                        cell.random_flip()
                else:
                    if counts[cell.state] <= 1:
                        other_parties = [p for p in [PARTY_A, PARTY_B, PARTY_C] if p != cell.state]
                        cell.next_state = random.choice(other_parties)

        for row in self.grid:
            for cell in row:
                if cell.state != cell.next_state:
                    changes += 1
                cell.update_state()

        self.iteration += 1
        total = GRID_SIZE * GRID_SIZE
        self.changes_last_round = changes / total

    def get_statistics(self):
        counts = {NEUTRAL: 0, PARTY_A: 0, PARTY_B: 0, PARTY_C: 0}
        for row in self.grid:
            for cell in row:
                counts[cell.state] += 1
        total = GRID_SIZE * GRID_SIZE
        return {k: round(v / total * 100, 2) for k, v in counts.items()}