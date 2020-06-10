import pygame as pg
import numpy as np

LENGTH = 1000
STEPS = 100
HEIGHT = LENGTH
WIDTH = LENGTH
BGCOLOR = (136, 184, 176)
BLACK = (0, 0, 0)


def get_grid_input(file_path):
    grid = np.zeros((WIDTH, HEIGHT), dtype='int8')

    with open(file_path, 'r') as f:
        for row, line in enumerate(f):
            for col, char in enumerate(line):
                if char == '.':
                    grid[row, col] = 0
                if char == '#':
                    grid[row, col] = 1

    return grid


def update_grid(grid: np.ndarray):
    next_gen = np.zeros(grid.shape, dtype='int8')
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            neighbors_count = count_neighbors(row, col, grid)
            if grid[row, col] == 1:
                if neighbors_count == 2 or neighbors_count == 3:
                    next_gen[row, col] = 1
                else:
                    next_gen[row, col] = 0
            else:
                if neighbors_count == 3:
                    next_gen[row, col] = 1
                else:
                    next_gen[row, col] = 0
    return next_gen


def count_neighbors(row, col, grid):
    neighbors_count = 0

    if row - 1 >= 0 and col - 1 >= 0 and grid[row - 1, col - 1] == 1:
        neighbors_count += 1
    if col - 1 >= 0 and grid[row, col - 1] == 1:
        neighbors_count += 1
    if row + 1 < grid.shape[0] and col - 1 >= 0 and grid[row + 1, col - 1] == 1:
        neighbors_count += 1

    if row - 1 >= 0 and grid[row - 1, col] == 1:
        neighbors_count += 1
    if row + 1 < grid.shape[0] and grid[row + 1, col] == 1:
        neighbors_count += 1

    if row - 1 >= 0 and col + 1 < grid.shape[1] and grid[row - 1, col + 1] == 1:
        neighbors_count += 1
    if col + 1 < grid.shape[1] and grid[row, col + 1] == 1:
        neighbors_count += 1
    if row + 1 < grid.shape[0] and col + 1 < grid.shape[1] and grid[row + 1, col + 1] == 1:
        neighbors_count += 1

    return neighbors_count


def main():
    print('Advent of Code 2015')
    grid = get_grid_input('../input.txt')

    for i in range(STEPS):
        grid = update_grid(grid)
        print(i)
    print(grid)


class GridDisplay(object):
    def __init__(self, grid):
        pg.init()
        self.display = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Advent of Code 2015 - Level 18')
        self.animating = False

        if grid.shape != (WIDTH, HEIGHT):
            raise ValueError('Invalid grid')

        self.grid = grid

    def animate(self):
        self.animating = True

        while self.animating:
            self.handle_input()
            self.draw_screen()
        pg.quit()

    def draw_screen(self):
        self.display.fill(BGCOLOR)
        surf = pg.surfarray.make_surface(self.grid)
        surf = pg.transform.scale(surf, (WIDTH * 10, HEIGHT * 10))
        self.display.blit(surf, (0, 0))
        pg.display.update()

    def handle_input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.animating = False


if __name__ == '__main__':
    main()