from app.players.player import Player


class Dwarf(Player):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        self._favourite_dish = favourite_dish
        super().__init__(nickname)

    def get_rating(self) -> None:
        return super().get_rating()

    def player_info(self) -> None:
        super().player_info()

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")
