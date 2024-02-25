from abc import ABC, abstractmethod


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


class PlayerX(ABCPlayer):
    _symbol_price = 1

    def _checkout_player(self) -> None:
        self.game._checkout_player(PlayerO())


class PlayerO(ABCPlayer):
    symbol_price = -1

    def _checkout_player(self) -> None:
        self.game._checkout_player(PlayerX())
