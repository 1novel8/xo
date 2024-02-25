from functools import reduce

from constants import xo_dict
from states import ABCPlayer, PlayerX


class Game:
    def __init__(self) -> None:
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self._winner = ''
        self._checkout_player(PlayerX())

    def _checkout_player(self, player: ABCPlayer) -> None:
        self._player = player
        self._player.game = self

    def _player_input(self) -> None:
        x, y = self._input_coordinates()
        self.board[x][y] = self._player.symbol_price

    def _print_board(self) -> None:
        for row in self.board:
            for value in row:
                print(f'{xo_dict[value]}', end=' ')
            print()

    def _input_coordinates(self) -> tuple[int, int]:
        is_valid_input = False
        x = y = None
        while not is_valid_input:
            x = int(input(f'Player {xo_dict[self._player.symbol_price]} Turn. OX coordinate is:'))
            y = int(input(f'Player {xo_dict[self._player.symbol_price]} Turn. OY coordinate is:'))
            is_valid_input = self._validate_coordinates(x, y)
        return x, y

    def _validate_coordinates(self, x: int, y: int) -> bool:
        if x >= 3 or y >= 3 or x < 0 or y < 0:
            return False
        if self.board[x][y] != 0:
            return False
        return True

    def _is_game_over(self) -> bool:
        filled_rows = 0
        for ind_i, row in enumerate(self.board):
            row_sum = abs(reduce(lambda a, b: a + b, row))
            if row_sum == 3:
                self._winner = xo_dict[self._player.symbol_price]
                return True
            if 0 not in row == 1:
                filled_rows += 1
            column_sum = 0
            for ind_j, _ in enumerate(row):
                column_sum += self.board[ind_j][ind_i]
            if abs(column_sum) == 3:
                self._winner = xo_dict[self._player.symbol_price]
                return True
        if filled_rows == 3:
            self._winner = 'no one'
            return True
        if abs(self.board[0][0] + self.board[1][1] + self.board[2][2]) == 3 or \
                abs(self.board[0][2] + self.board[1][1] + self.board[2][0]) == 3:
            self._winner = xo_dict[self._player.symbol_price]
            return True
        return False

    def play(self) -> None:
        while not self._is_game_over():
            self._player_input()
            self._print_board()
            self._player._checkout_player()
        print(f'Winner is {self._winner}')
