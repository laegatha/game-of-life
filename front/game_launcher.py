import time
import skia
import glfw
from OpenGL import GL

from back.neighbors_searcher import NeighborsSearcher
from back.cell_state_calculator import CellStateCalculator

from front.cell_caracteristics import CELL_SIZE
from front.window_manager import glfw_window, skia_surface

class GameLauncher:
    def __init__(self):
        pass

    @staticmethod
    def n_iter_choice() -> int:
        n_iter_input = input('Number of iterations: ')

        try:
            n_iter = int(n_iter_input)
            print(f"{n_iter} iterations")
        except ValueError:
            print("This is not a valid number. Try the integer format")

        return n_iter

    @staticmethod
    def compute_next_state_table(n_row: int, n_col: int, actual_state: list) -> list:
        next_state_table = []
        for i in range(n_row):
            l_row = []
            for j in range(n_col):
                neighbors = NeighborsSearcher().get_neighbors(n_row=n_row, n_col=n_col, table=actual_state, x=i, y=j)
                next_state_cell = CellStateCalculator().compute_next_state_cell(actual_state=actual_state[i][j],
                                                                                neighbors=neighbors)
                l_row.append(next_state_cell)

            next_state_table.append(l_row)

        return next_state_table

    @staticmethod
    def draw_one_cell(row: int, col: int, color: str):
        rect = skia.Rect(col * CELL_SIZE, row * CELL_SIZE, (col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE)
        paint = skia.Paint(
            Color=eval('skia.Color' + color.upper()),
            Style=skia.Paint.kFill_Style)

        return rect, paint

    def draw_table(self, window, surface, table: list, n_row: int, n_col: int):
        with surface as canvas:
            for i in range(n_row):
                for j in range(n_col):
                    if table[i][j] == 1:
                        rect, paint = self.draw_one_cell(row=i, col=j, color='white')
                    else:
                        rect, paint = self.draw_one_cell(row=i, col=j, color='black')
                    canvas.drawRect(rect, paint)

    def launch_game(self, n_row: int, n_col: int, height: int, width: int, initial_state: list):
        n_iter = self.n_iter_choice()
        with glfw_window(height, width) as window:
            GL.glClear(GL.GL_COLOR_BUFFER_BIT)

            with skia_surface(window) as surface:
                print("Initial state")
                self.draw_table(window=window, surface=surface, table=initial_state, n_row=n_row, n_col=n_col)
                surface.flushAndSubmit()
                glfw.swap_buffers(window)
                next_table = self.compute_next_state_table(n_row=n_row, n_col=n_col, actual_state=initial_state)
                time.sleep(2)

                for i in range(n_iter):
                    print(f"State {i+1}")
                    self.draw_table(window=window, surface=surface, table=next_table, n_row=n_row, n_col=n_col)
                    surface.flushAndSubmit()
                    glfw.swap_buffers(window)
                    next_table = self.compute_next_state_table(n_row=n_row, n_col=n_col, actual_state=next_table)
                    time.sleep(2)

            while (glfw.get_key(window, glfw.KEY_ESCAPE) != glfw.PRESS
                   and not glfw.window_should_close(window)):
                glfw.wait_events()
