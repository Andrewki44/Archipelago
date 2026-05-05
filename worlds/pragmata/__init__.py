from typing import ClassVar

from worlds.AutoWorld import WebWorld, World
from BaseClasses import Tutorial
from Utils import visualize_regions

from .options   import PragmataOptions, create_option_groups
from .regions   import create_regions
from .items     import create_items, create_item_name_to_address_map, get_filler_item
from .locations import create_location_name_to_address_map


class PragmataWebWorld(WebWorld):
    """
    Webhost info for Pragmata
    """
    theme = "grass"
    option_groups = create_option_groups()
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing Pragmata with Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Andrewki"]
    )

    tutorials = [setup_en]


class PragmataWorld(World):
    game = "Pragmata"
    web = PragmataWebWorld()
    topology_present = False
    origin_region_name = "The Shelter"

    # settings_key = "Pragmata_options"
    # settings = ClassVar[PragmataSettings]

    options_dataclass = PragmataOptions
    options = PragmataOptions

    item_name_to_id = create_item_name_to_address_map()
    location_name_to_id = create_location_name_to_address_map()
    explicit_indirect_conditions = False

    def generate_early(self) -> None:
        pass

    def get_filler_item_name(self) -> str:
        return get_filler_item(self)
    
    def create_regions(self) -> None:
        create_regions(self, self.player)

    def create_items(self) -> None:
        create_items(self, self.player)

    def set_rules(self) -> None:
        pass

    def generate_output(self, output_directory: str) -> None:
        visualize_regions(self.multiworld.get_region("The Shelter", self.player), 
                          f"Pragmata_{self.multiworld.seed}_{self.player}.puml", 
                          show_entrance_names=True, auto_assign_colors=True)

