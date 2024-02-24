from typing import Type

from constants import xo_dict
from states import ABCPlayer, PlayerX


class Game:
    def __init__(self) -> None:
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self._winner = ''
        self._checkout_player(PlayerX)

    def _checkout_player(self, player: Type[ABCPlayer]) -> None:
        self._player = player
        self._player.game = self

    def _player_input(self) -> None:
        self._player.input()

    def _print_board(self) -> None:
        for row_ind, row in enumerate(self.board):
            for ind, value in enumerate(row):
                print(f'{xo_dict[value]}', end=' ')
            print('', end='\n')

    def play(self) -> None:
        while self._winner == '':
            self._print_board()
            self._player_input()
        print(f'Winner is {self._winner}')
