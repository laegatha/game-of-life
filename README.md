# game-of-life

The goal of this project is to reproduce Conway's Game of Life in Python.

![game_of_life](https://user-images.githubusercontent.com/99142342/176142339-5177a940-0f37-432c-8471-a8f0e32f43b6.gif)

The universe of the game is a two dimensional grid containing a defined number of cells.
The game state changes on each generation, which can be dynamically set.

There are 4 rules to be respected for this game:
  1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
  2. Any live cell with two or three live neighbors lives on to the next generation.
  3. Any live cell with more than three live neighbors dies.
  4. Any dead cell with exactly three live neighbors becomes a live cell.
