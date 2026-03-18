from players.elves.elf import Elf


class Druid(Elf):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            favourite_spell: str
    ) -> None:
        self._favourite_spell = favourite_spell
        super().__init__(nickname, musical_instrument)

    def player_info(self) -> None:
        print(f"Druid {self.nickname}. {self.nickname} has a favourite spell: \
{self._favourite_spell}")

    def get_rating(self) -> str:
        return len(self._favourite_spell)
