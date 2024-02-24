from abc import ABC, abstractmethod
from functools import reduce

from constants import xo_dict


class ABCPlayer(ABC):
    _symbol_price = None
    _game = None

    @property
    def symbol_price(self) -> int:
        return self._symbol_price

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game) -> None:
        self._game = game

    @abstractmethod
    def _checkout_player(self) -> None:
        ...

    def input(self) -> None:
        x, y = self._input_coordinates()
        self.game.board[x][y] = self.symbol_price
        if self._is_winner():
            self.game._winner = xo_dict[self.symbol_price]
        self._checkout_player()

    def _input_coordinates(self) -> tuple[int, int]:
        is_valid_input = False
        x = y = None
        while not is_valid_input:
            x = int(input(f'Player {xo_dict[self.symbol_price]} Turn. OX coordinate is:'))
            y = int(input(f'Player {xo_dict[self.symbol_price]} Turn. OY coordinate is:'))
            is_valid_input = self._validate_coordinates(x, y)
        return x, y

    def _validate_coordinates(self, x: int, y: int) -> bool:
        if x >= 3 or y >= 3 or x < 0 or y < 0:
            return False
        if self.game.board[x][y] != 0:
            return False
        return True

    def _is_winner(self) -> bool:
        for ind, row in enumerate(self.game.board):
            if abs(reduce(lambda a, b: a + b, row)) == 3:
                return True
        if abs(self.game.board[0][0] + self.game.board[1][1] + self.game.board[2][2]) == 3 or \
                abs(self.game.board[0][2] + self.game.board[1][1] + self.game.board[2][0]) == 3:
            return True
        return False


class PlayerX(ABCPlayer):
    _symbol_price = 1

    def _checkout_player(self) -> None:
        self.game._checkout_player(PlayerO())


class PlayerO(ABCPlayer):
    symbol_price = -1

    def _checkout_player(self) -> None:
        self.game._checkout_player(PlayerX())
