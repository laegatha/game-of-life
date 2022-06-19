import os
import skia
import glob
from PIL import Image

from back.cell_state_calculator import CellStateCalculator
from front.cell_caracteristics import CELL_SIZE

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
    def draw_one_cell(row: int, col: int, color: str):
        rect = skia.Rect(col * CELL_SIZE, row * CELL_SIZE, (col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE)
        paint = skia.Paint(
            Color=eval('skia.Color' + color.upper()),
            Style=skia.Paint.kFill_Style)

        return rect, paint

    def draw_table(self, surface, table: list, n_row: int, n_col: int):
        with surface as canvas:
            for i in range(n_row):
                for j in range(n_col):
                    if table[i][j] == 1:
                        rect, paint = self.draw_one_cell(row=i, col=j, color='white')
                    else:
                        rect, paint = self.draw_one_cell(row=i, col=j, color='black')
                    canvas.drawRect(rect, paint)
        return surface.makeImageSnapshot()

    @staticmethod
    def create_gif(images_path):
        fp_in = images_path + "\\state*.png"
        fp_out = images_path + "\\game_of_life.gif"
        imgs = (Image.open(f) for f in sorted(glob.glob(fp_in)))
        img = next(imgs)  # extract first image from iterator
        img.save(fp=fp_out, format='GIF', append_images=imgs,
                 save_all=True, duration=200, loop=0)

    def launch_game(self, n_row: int, n_col: int, height: int, width: int, initial_state: list):
        n_iter = self.n_iter_choice()
        images_path = os.path.dirname(os.getcwd()) + "\\output\\images"
        for f in os.listdir(images_path):
            os.remove(os.path.join(images_path, f))
        surface = skia.Surface(height=height, width=width)

        print("Initial state")
        table = self.draw_table(surface=surface, table=initial_state, n_row=n_row, n_col=n_col)
        display(table)
        table.save(images_path + "\\state1.png")

        next_table = CellStateCalculator().compute_next_state_table(n_row=n_row, n_col=n_col,
                                                                    actual_state=initial_state)

        for i in range(1, n_iter):
            print(f"State {i+1}")
            table = self.draw_table(surface=surface, table=next_table, n_row=n_row, n_col=n_col)
            display(table)
            table.save(images_path + f"\\state{i+1}.png")

            next_table = CellStateCalculator().compute_next_state_table(n_row=n_row, n_col=n_col,
                                                                        actual_state=next_table)

        self.create_gif(images_path=images_path)
