# pathfinding-algorithm
A* Pathfinding Algorithm Visualizer
This project visualizes the A* Pathfinding Algorithm using Pygame. It allows users to interact with a grid, set start and end points, place obstacles, and visualize the algorithm finding the shortest path.

Features
Interactive grid to set start/end points and place/remove barriers.

A* algorithm to calculate the shortest path while avoiding obstacles.

Real-time visualization using Pygame.

Installation
Clone the repository:

git clone https://github.com/ishan-puri/pathfinding-algorithm.git
cd pathfinding-algorithm
Install dependencies:

pip install pygame
Run the project:

python pathfinding.py
Usage
Set start and end points:

Left-click to set the start (blue) and end (red) points.

Draw obstacles:

Left-click to place barriers (black).

Right-click to remove them.

Run A Pathfinding*:

Press the spacebar to run the A* algorithm and see the pathfinding in action.

How It Works
The A* algorithm finds the shortest path from the start point to the end point, using a combination of cost from the start (G-score) and heuristic to the goal (H-score). The algorithm expands nodes based on the F-score (G + H) and backtracks to find the optimal path.
