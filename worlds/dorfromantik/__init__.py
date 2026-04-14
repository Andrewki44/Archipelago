from typing import ClassVar

from worlds.AutoWorld import WebWorld, World
from BaseClasses import Tutorial

from . import options as DorfOptions
from . import regions as DorfRegions
from . import items as DorfItems


class DorfWebWorld(WebWorld):
    """
    Webhost info for Dorfromantik
    """
    theme = "grass"
    option_groups = DorfOptions.create_option_groups()
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing Dorfromantik with Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Andrewki"]
    )

    tutorials = [setup_en]


class DorfWorld(World):
    game = "Dorfromantik"
    web = DorfWebWorld()
    topology_present = False

    # settings_key = "dorf_options"
    # settings = ClassVar[DorfSettings]

    options_dataclass = DorfOptions.DorfOptions
    options = DorfOptions.DorfOptions

    def generate_early(self) -> None:
        pass

    def get_filler_item_name(self) -> str:
        return DorfItems.get_filler_item_name(self)
    
    def create_regions(self) -> None:
        DorfRegions.create_regions(self, self.player)

    def create_items(self) -> None:
        DorfItems.create_items(self, self.player)

    def set_rules(self) -> None:
        pass

