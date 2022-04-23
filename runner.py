from front.table_starter import TableStarter
from back.table_builder import TableBuilder
from front.game_launcher import GameLauncher


class Runner:
    def __init__(self):
        pass

    def run():
        n_row, n_col, height, width = TableStarter().start_table()
        initial_state = TableBuilder().build_table(n_row=n_row, n_col=n_col)
        GameLauncher().launch_game(n_row=n_row, n_col=n_col, height=height, width=width, initial_state=initial_state)
