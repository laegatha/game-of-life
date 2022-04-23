from front.cell_caracteristics import CELL_SIZE

class TableStarter:
    def __init__(self):
        pass

    @staticmethod
    def n_col_choice() -> int:
        n_col_input = input('Number of columns: ')
        try:
            n_col = int(n_col_input)
            print(f"{n_col} columns")
        except ValueError:
            print("This is not a valid number. Try the integer format")

        return n_col

    @staticmethod
    def n_row_choice() -> int:
        n_row_input = input('Number of rows: ')
        try:
            n_row = int(n_row_input)
            print(f"{n_row} rows")
        except ValueError:
            print("This is not a valid number. Try the integer format")

        return n_row

    @staticmethod
    def compute_height(n_row: int) -> int:
        return n_row * CELL_SIZE

    @staticmethod
    def compute_width(n_col: int) -> int:
        return n_col * CELL_SIZE

    def start_table(self) -> list:
        n_row = self.n_row_choice()
        n_col = self.n_col_choice()
        height = self.compute_height(n_row=n_row)
        width = self.compute_width(n_col=n_col)
        print(f"Table surface: height = {height} ; width = {width}")

        return n_row, n_col, height, width
