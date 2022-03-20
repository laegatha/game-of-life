from random import randint

class TableBuilder:
    def __init__(self):
        pass

    @staticmethod
    def build_one_list(n_col: int) -> list:
        return [randint(0, 1) for i in range(n_col)]

    def build_table(self, n_row: int, n_col: int) -> list:
        l = []
        for i in range(n_row):
            l.append(self.build_one_list(n_col))

        return l