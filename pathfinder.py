import pygame
import heapq

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define grid dimensions
GRID_WIDTH = 20
GRID_HEIGHT = 20
CELL_SIZE = 30

# Define the directions (up, down, left, right)
MOVES = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # (dx, dy)

# Node class for A* algorithm
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = 0  # Cost from start
        self.h = 0  # Heuristic to goal
        self.f = 0  # Total cost (f = g + h)
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

# Function to calculate the heuristic (Manhattan Distance)
def heuristic(node, goal):
    return abs(node.x - goal.x) + abs(node.y - goal.y)

# A* Search Algorithm
def a_star(grid, start, goal):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, (0, start))

    while open_list:
        _, current = heapq.heappop(open_list)

        if (current.x, current.y) == (goal.x, goal.y):
            path = []
            while current:
                path.append((current.x, current.y))
                current = current.parent
            return path[::-1]  # Return reversed path

        closed_list.add((current.x, current.y))

        for dx, dy in MOVES:
            nx, ny = current.x + dx, current.y + dy

            if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT and grid[ny][nx] == 0 and (nx, ny) not in closed_list:
                neighbor = Node(nx, ny)
                tentative_g = current.g + 1

                if (nx, ny) not in closed_list or tentative_g < neighbor.g:
                    neighbor.g = tentative_g
                    neighbor.h = heuristic(neighbor, goal)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.parent = current
                    heapq.heappush(open_list, (neighbor.f, neighbor))

    return None  # No path found

# Visualization using pygame
def draw_grid(screen, grid, path=None, start=None, goal=None):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if grid[y][x] == 1:
                pygame.draw.rect(screen, BLACK, rect)
            elif path and (x, y) in path:
                pygame.draw.rect(screen, GREEN, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, BLUE, rect, 1)

    if start:
        pygame.draw.rect(screen, BLUE, pygame.Rect(start.x * CELL_SIZE, start.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    if goal:
        pygame.draw.rect(screen, RED, pygame.Rect(goal.x * CELL_SIZE, goal.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
    pygame.display.set_caption('A* Pathfinding')
    clock = pygame.time.Clock()

    grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]  # 0 is empty space, 1 is obstacle
    start = None
    goal = None
    path = None

    first_click = True
    second_click = False

    running = True
    while running:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pygame.mouse.get_pressed()[0]:  # Left click to place barriers or set start/end points
                mx, my = pygame.mouse.get_pos()
                x, y = mx // CELL_SIZE, my // CELL_SIZE

                if first_click:
                    start = Node(x, y)
                    first_click = False
                    second_click = True
                elif second_click:
                    goal = Node(x, y)
                    second_click = False
                else:
                    grid[y][x] = 1  # Set barrier at clicked position

            if pygame.mouse.get_pressed()[2]:  # Right click to remove barriers
                mx, my = pygame.mouse.get_pos()
                x, y = mx // CELL_SIZE, my // CELL_SIZE
                grid[y][x] = 0

        # Run pathfinding when space key is pressed
        if pygame.key.get_pressed()[pygame.K_SPACE] and start and goal:
            path = a_star(grid, start, goal)

        # Draw the grid, barriers, and the path
        draw_grid(screen, grid, path, start, goal)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    main()
