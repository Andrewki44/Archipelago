import typing
from typing import NamedTuple, Optional
from itertools import chain
from BaseClasses import Location, Region

from .data.locations import PragmataLocationData, escapeHatchLocations, treasureBoxLocations, \
    remLocations, storageExpanderLocations, trainingDataLocations, miniCabinLocations, \
    componentLocations, cartridgeHolderLocations, allLocations

if typing.TYPE_CHECKING:
    from .regions import PragmataRegionData
else:
    PragmataRegionData = object

# ---------------------------------------------------------------------------- #
#                               Location Class                                 #
# ---------------------------------------------------------------------------- #

class PragmataLocation(Location):
    game: str = "Pragmata"

    def __init__(self, player: int, name: str = '', address: Optional[int] = None, parent: Optional[Region] = None):
        super().__init__(player, name, address, parent)


def create_locations(player: int, region: Region, regionData: PragmataRegionData):
    def add_locations(region: Region, locationIds: list[int], locationData: list[PragmataLocationData]):
        for id in locationIds:
            location = [x for x in locationData if x.id == id][0]
            new_location = PragmataLocation(player, location.name, location.address, region)
            region.locations.append(new_location)
    
    if regionData.escapeHatches:
        add_locations(region, regionData.escapeHatches, escapeHatchLocations)
    if regionData.treasureBoxes:
        add_locations(region, regionData.treasureBoxes, treasureBoxLocations)
    if regionData.components:
        add_locations(region, regionData.components, componentLocations)
    if regionData.rem:
        add_locations(region, regionData.rem, remLocations)
    if regionData.storageExpanders:
        add_locations(region, regionData.storageExpanders, storageExpanderLocations)
    if regionData.trainingData:
        add_locations(region, regionData.trainingData, trainingDataLocations)
    if regionData.miniCabin:
        add_locations(region, regionData.miniCabin, miniCabinLocations)
    if regionData.cartridgeHolders:
        add_locations(region, regionData.cartridgeHolders, cartridgeHolderLocations)


def create_location_name_to_address_map() -> dict[str, int]:
    """
    Creates a map from location names to their AP location address
    """
    name_to_id_map: dict[str, int] = {}
    for location in allLocations:
        name_to_id_map[location.name] = location.address

    return name_to_id_map
