from typing import NamedTuple, Optional
from itertools import chain
from BaseClasses import Location, Region

# ---------------------------------------------------------------------------- #
#                               Location Classes                               #
# ---------------------------------------------------------------------------- #

class DorfLocation(Location):
    game: str = "Final Fantasy X"

    def __init__(self, player: int, name: str = '', address: Optional[int] = None, parent: Optional[Region] = None):
        super().__init__(player, name, address, parent)


class DorfLocationData(NamedTuple):
    rom_address: int
    name: str
    location_id: int
    # missable: bool


scoreOffset: int     = 0x0000
questOffset: int     = 0x1000
challengeOffset: int = 0x2000

# ---------------------------------------------------------------------------- #
#                               Location Listings                              #
# ---------------------------------------------------------------------------- #

# scoreLocations: list[DorfLocationData] = [DorfLocationData(location[1]+ScoreOffset, *location) for location in [
#     ("Score: 100",  0),
# ]]

scoreLocations: list[DorfLocationData] = [DorfLocationData(i + scoreOffset, f"Score: {i}", (i-1000)/500) for i in range(1000, 10000, 500)]

questLocations: list[DorfLocationData] = [DorfLocationData(location[1]+QuestOffset, *location) for location in [
    ("Forest 5+",  0),
]]

challengeLocations: list[DorfLocationData] = [DorfLocationData(location[1]+ChallengeOffset, *location) for location in [
    ("Farmer 1",  0),
]]

allLocations = list(chain(scoreLocations,
                          questLocations,
                          challengeLocations))