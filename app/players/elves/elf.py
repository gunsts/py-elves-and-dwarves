from players.player import Player


class Elf(Player):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        self._musical_instrument = musical_instrument
        super().__init__(nickname)

    def get_rating(self) -> None:
        return super().get_rating()

    def player_info(self) -> None:
        super().player_info()

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the \
{self._musical_instrument}")
