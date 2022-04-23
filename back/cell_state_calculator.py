

class CellStateCalculator:
    def __init__(self):
        pass

    @staticmethod
    def get_next_state_live_cell(nb_neighbors: int) -> int:
        if nb_neighbors < 2 or nb_neighbors > 3:
            next_state = 0
        else:
            next_state = 1

        return next_state

    @staticmethod
    def get_next_state_dead_cell(nb_neighbors: int) -> int:
        if nb_neighbors == 3:
            next_state = 1
        else:
            next_state = 0

        return next_state

    def compute_next_state_cell(self, actual_state: int, neighbors: list) -> int:
        nb_neighbors = sum(neighbors)

        if actual_state == 1:
            next_state = self.get_next_state_live_cell(nb_neighbors)
        else:
            next_state = self.get_next_state_dead_cell(nb_neighbors)

        return next_state