
class NeighborsSearcher:
    def __init__(self):
        pass

    # classic cell
    # 1 2 3
    # 4 c 5
    # 6 7 8
    # 8 neighbors

    # corner cell
    # c 1
    # 2 3
    # 3 neighbors

    # border cell
    # 1 c 2
    # 3 4 5
    # 5 neighbors

    @staticmethod
    def get_start_x(x: int) -> int:
        if x == 0:
            start_x = x
        else:
            start_x = x - 1

        return start_x

    @staticmethod
    def get_end_x(n_row: int, x: int) -> int:
        if x == n_row - 1:
            end_x = n_row - 1
        else:
            end_x = x + 1

        return end_x

    @staticmethod
    def get_start_y(y: int) -> int:
        if y == 0:
            start_y = y
        else:
            start_y = y - 1

        return start_y

    @staticmethod
    def get_end_y(n_col: int, y: int) -> int:
        if y == n_col - 1:
            end_y = n_col - 1
        else:
            end_y = y + 1

        return end_y

    # i, j are cells coordinates : i for rows and j for columns
    def get_neighbors(self, n_row: int, n_col: int, table: list, x: int, y: int) -> list:
        l_neighbors = []

        start_x = self.get_start_x(x)
        end_x = self.get_end_x(n_row, x)

        start_y = self.get_start_y(y)
        end_y = self.get_end_y(n_col, y)

        for i in range(start_x, end_x + 1):
            for j in range(start_y, end_y + 1):
                if i != x or j != y:
                    l_neighbors.append(table[i][j])

        return l_neighbors