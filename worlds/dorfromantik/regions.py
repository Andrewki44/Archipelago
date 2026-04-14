from BaseClasses import Region
from rule_builder.rules import Has

from .__init__  import DorfWorld
from .items     import DorfItem
from .locations import DorfLocation, DorfLocationData, allLocations


def create_regions(world: DorfWorld, player) -> None:
    def add_locations(region: Region, location_data: list[DorfLocationData]):
        for location in location_data:
            new_location = DorfLocation(player, location.name, location.rom_address, region)
            region.locations.append(new_location)

    menu_region = Region("Menu", player, world.multiworld)
    world.multiworld.regions.append(menu_region)

    add_locations(menu_region, allLocations)
    
    menu_region.add_event("Goal", "Victory", location_type=DorfLocation, item_type=DorfItem)
    world.set_completion_rule(Has("Victory"))