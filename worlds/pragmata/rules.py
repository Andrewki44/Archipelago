import typing
from dataclasses import dataclass
from typing_extensions import override

from rule_builder.rules import Rule, Has
from .data.locations import escapeHatchOffset, treasureBoxOffset, remOffset, storageExpanderOffset, trainingDataOffset, \
    miniCabinOffset, pureLunumOffset

if typing.TYPE_CHECKING:
    from .__init__ import PragmataWorld
else:
    PragmataWorld = object

# ---------------------------------------------------------------------------- #
#                               Rule Dictionaries                              #
# ---------------------------------------------------------------------------- #

missionRuleDict: dict[str, Rule] = {
    "Solar Power Plant":        Has("Progressive Mission Unlock", 1),
    "Mass Production Array":    Has("Progressive Mission Unlock", 2),
    "Terra Dome":               Has("Progressive Mission Unlock", 3),
    "Lunum Mines":              Has("Progressive Mission Unlock", 4),
    "Central Port":             Has("Progressive Mission Unlock", 5),
}

escapeHatchRuleDict: dict[str, Rule] = {
    
}

# ---------------------------------------------------------------------------- #
#                                   Set Rules                                  #
# ---------------------------------------------------------------------------- #
def set_rules(world: PragmataWorld) -> None:
    
    # -------------------------------- Lim Eraser -------------------------------- #
    storageExpanderEraserLocations: list[int] = [
        0,  # Solar Power Plant: Entrance - Storage Expander 1
    ]
    safeBoxEraserLocations: list[int] = [
        1,  # Solar Power Plant: Sealed Sector Gate - Safe Box 2
        3,  # Mass Production Array: Test Site Entrance - Safe Box 1
        4,  # Mass Production Array: Test Site Entrance - Safe Box 2
        7,  # Mass Production Array: Shopping District - Safe Box 2
        16, # Mass Production Array: Office Space - Safe Box 5
    ]
    pureLunumEraserLocations: list[int] = [
        0, # Solar Power Plant: Sealed Sector Gate - Pure Lunum 1
    ]

    for location_id in storageExpanderEraserLocations:
        location = world.get_location(world.location_id_to_name[location_id | storageExpanderOffset])
        world.set_rule(location, Has("Lim Eraser"))
    for location_id in safeBoxEraserLocations:
        location = world.get_location(world.location_id_to_name[location_id | treasureBoxOffset])
        world.set_rule(location, Has("Lim Eraser"))
    for location_id in pureLunumEraserLocations:
        location = world.get_location(world.location_id_to_name[location_id | pureLunumOffset])
        world.set_rule(location, Has("Lim Eraser"))

    # --------------------------------- Cleanser --------------------------------- #
    safeBoxCleansingLocations: list[int] = [
        13, # Mass Production Array: Office Space - Safe Box 2
        14, # Mass Production Array: Office Space - Safe Box 3
    ]

    for location_id in safeBoxCleansingLocations:
        location = world.get_location(world.location_id_to_name[location_id | treasureBoxOffset])
        world.set_rule(location, Has("Cleansing"))