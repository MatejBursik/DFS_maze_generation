import pygame, cv2, numpy as np
from cell import *

rows = 25
cols = 25
size = 20
thickness = 1

stack = []
grid = [Cell(col, row, size, thickness) for row in range(rows) for col in range(cols)]
current_cell = grid[0]
current_cell.visited = True

# enterence and exit of the maze
grid[0].walls['left'] = False
grid[len(grid)-1].walls['right'] = False

# visualization of the DFS maze generation 
pygame.init()
winX = cols * size
winY = rows * size
window = pygame.display.set_mode((winX, winY))
clock = pygame.time.Clock()
FPS = 60
run = True

while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False

        # reset to generate new maze
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                stack = []
                grid = [Cell(col, row, size, thickness) for row in range(rows) for col in range(cols)]
                grid[0].walls['left'] = False
                grid[len(grid)-1].walls['right'] = False
                current_cell = grid[0]
                current_cell.visited = True

    # grid exploration through DFS
    next_cell = current_cell.check_neighbors(grid, (cols, rows))
    if next_cell:
        next_cell.visited = True
        stack.append(current_cell)
        remove_walls(current_cell, next_cell)
        current_cell = next_cell
    elif len(stack) > 0:
        current_cell = stack.pop()

    # draw
    window.fill((0,0,255))

    for cell in grid:
        cell.draw(window)
    
    current_cell.draw_current_cell(window)

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()

# export the generated maze as an image
img = np.zeros((winY, winX, 3), np.uint8)
color = (255,255,255)

for cell in grid:
    x = cell.x * cell.size
    y = cell.y * cell.size
    
    if cell.walls['up']:
        cv2.line(img, (x, y), (x + cell.size, y), color, cell.thickness)
    if cell.walls['down']:
        cv2.line(img, (x, y + cell.size - cell.thickness), (x + cell.size, y + cell.size - cell.thickness), color, cell.thickness)
    if cell.walls['left']:
        cv2.line(img, (x, y), (x, y + cell.size), color, cell.thickness)
    if cell.walls['right']:
        cv2.line(img, (x + cell.size - cell.thickness, y), (x + cell.size - cell.thickness, y + cell.size), color, cell.thickness)

# invert color
img = cv2.bitwise_not(img)

# save image
cv2.imwrite('test.png', img)
