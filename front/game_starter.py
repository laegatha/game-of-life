

class GameStarter:
    def __init__(self):
        pass

    def n_col_choice() -> int:
        n_col_input = input('Number of columns: ')
        try:
            n_col = int(n_col_input)
            print(f"{n_col} columns")
        except ValueError:
            print("This is not a valid number. Try the integer format")

        return n_col

    def n_row_choice() -> int:
        n_row_input = input('Number of rows: ')
        try:
            n_row = int(n_row_input)
            print(f"{n_row} columns")
        except ValueError:
            print("This is not a valid number. Try the integer format")

        return n_row