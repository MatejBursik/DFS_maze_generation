# DFS (Depth First Search) maze generation
This repository covers a process of generating a maze. The process of involves treating the maze as a grid of cells and carving out paths between cells in a randomized manner which creates the maze has a single connected path with no cycles.

## Process explanation
The maze generation uses randomized DFS as the algorithm to create the maze. The algorithm is placed in a basic Pygame game loop for visualization and re-generation of the maze if it is not suitalbe. Lastly, after the application window is exited, I use CV2 the make and save an image out of the maze.

### Depth First Search (DFS)
Depth First Search (DFS) is an algorithm used in computer science for traversing or searching through data structures, for example trees and graphs. The algorithm starts at a root node and explores as far as possible along each branch before backtracking. It does this by storing the visited nodes in a stack as it is look for branches sprouting from the last node that was added to the stack. Once it finds a node with no branches, it removes the last node that was added to the stack. Then it looks for other branches sprouting from the new last node. This process is called backtracking.

In this case, if there are multiple branches sprouting from the last node, the DFS chooses the branch it wants to follow randomly. With this, the maze generated is lost likely unique (depending on the size of the maze).

### Visualization of the maze generation !!!
pygame game loop to show the process of generating the maze, press SPACE to re-generate the maze

### Exporting/saving the generated maze as an image (png) !!!
numpy array representing the image,
draw lines with cv2 based on walls of cells of the maze,
save as png with cv2

## How to use
1. Clone/Download this repository
2. Install Python (pip included)
3. Install necessary Python libraries
    - pygame
    - cv2
    - numpy
    - random
4. Run [main.py](main.py)
5. Extra: you can change the variables `rows`, `cols`, `size`, and `thickness` to affect the maze and its final image

