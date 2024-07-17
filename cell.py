import pygame
from random import choice

class Cell:
    def __init__(self, x, y, size, thickness):
        self.x = x
        self.y = y
        self.visited = False
        self.walls = {
            'up' : True,
            'down' : True,
            'left' : True,
            'right' : True
        }
        self.size = size
        self.thickness = thickness

    def draw(self, screen):
        x = self.x * self.size
        y = self.y * self.size

        if self.visited:
            pygame.draw.rect(screen, (0,0,100), (self.x * self.size, self.y * self.size, self.size, self.size))

        if self.walls['up']:
            pygame.draw.line(screen, (0,0,0), (x, y), (x + self.size, y), self.thickness)
        if self.walls['down']:
            pygame.draw.line(screen, (0,0,0), (x, y + self.size - self.thickness), (x + self.size, y + self.size - self.thickness), self.thickness)
        if self.walls['left']:
            pygame.draw.line(screen, (0,0,0), (x, y), (x, y + self.size), self.thickness)
        if self.walls['right']:
            pygame.draw.line(screen, (0,0,0), (x + self.size - self.thickness, y), (x + self.size - self.thickness, y + self.size), self.thickness)

    def draw_current_cell(self, screen):
        pygame.draw.rect(screen, (255,0,0), (self.x * self.size + self.thickness, self.y * self.size + self.thickness, self.size - self.thickness, self.size - self.thickness))
    
    def check(self, x, y, _grid, _cr): # _cr = (cols, rows)
        find_index = lambda x, y: x + y * _cr[0]
        if x < 0 or x > _cr[0] - 1 or y < 0 or y > _cr[1] - 1:
            return False
        return _grid[find_index(x, y)]
    
    def check_neighbors(self, _grid, _cr): # _cr = (cols, rows)
        neighbors = []
        up = self.check(self.x, self.y - 1, _grid, _cr)
        down = self.check(self.x, self.y + 1, _grid, _cr)
        left = self.check(self.x - 1, self.y, _grid, _cr)
        right = self.check(self.x + 1, self.y, _grid, _cr)

        if up and not up.visited:
            neighbors.append(up)
        if down and not down.visited:
            neighbors.append(down)
        if left and not left.visited:
            neighbors.append(left)
        if right and not right.visited:
            neighbors.append(right)
        
        if neighbors:
            return choice(neighbors)
        return False

def remove_walls(current, next):
    dx = current.x - next.x
    if dx == 1:
        current.walls['left'] = False
        next.walls['right'] = False
    elif dx == -1:
        current.walls['right'] = False
        next.walls['left'] = False
    dy = current.y - next.y
    if dy == 1:
        current.walls['up'] = False
        next.walls['down'] = False
    elif dy == -1:
        current.walls['down'] = False
        next.walls['up'] = False