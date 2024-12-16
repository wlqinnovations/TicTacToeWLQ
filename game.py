import numpy as np


class GameBrain:
    def __init__(self):
        self.reset()

    def computer_turn(self, player_symbol: bool) -> tuple:
        """Computer selects an available cell."""
        available_positions = np.argwhere(np.isnan(self.available))
        if available_positions.size > 0:
            choice = available_positions[np.random.choice(len(available_positions))]
            row, col = choice
            self.available[row, col] = not player_symbol
            return row, col
        return -1, -1  # No valid moves left

    def check_result(self, value: bool) -> bool:
        """Checks if the given player has won."""
        board = self.available == value
        return (
            np.any(np.all(board, axis=0))  # Check columns
            or np.any(np.all(board, axis=1))  # Check rows
            or np.all(np.diag(board))  # Check main diagonal
            or np.all(np.diag(np.fliplr(board)))  # Check anti-diagonal
        )

    def is_draw(self) -> bool:
        """Checks if the game is a draw."""
        return not np.isnan(self.available).any()

    def reset(self):
        """Resets the game board."""
        self.available = np.full((3, 3), np.nan)
