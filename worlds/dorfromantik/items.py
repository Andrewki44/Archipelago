from typing import NamedTuple
from itertools import chain
from BaseClasses import Item, ItemClassification

from .__init__ import DorfWorld

# ---------------------------------------------------------------------------- #
#                                 Item Classes                                 #
# ---------------------------------------------------------------------------- #

class DorfItemData(NamedTuple):
    name: str
    progression: ItemClassification
    itemID: int = 0x00
    player: int = 0


class DorfItem(Item):
    name: str
    progression: ItemClassification
    itemID: int = 0x00
    player: int = 0
    game: str = "Dorfromantik"


tileOffset: int = 0x0000
scoreItems: int = 0x1000

# ---------------------------------------------------------------------------- #
#                            Item Creation Functions                           #
# ---------------------------------------------------------------------------- #

def get_filler_item(world: DorfWorld) -> DorfItemData:
    filler = [x for x in fillerItems]
    return world.random.choice(filler)

def create_items(world: DorfWorld, player) -> None:
    def create_item(item: DorfItemData) -> DorfItem:
        return DorfItem(item.itemname, item.progression, item.itemID, player)
    
    requiredItems: list[DorfItemData] = []
    
    # -------------------------- Populate Required Items ------------------------- #
    for item in allItems:
        if item.progression == ItemClassification.progression:
            requiredItems.append(item)
    
    # ------------------------ Calculate Remaining to Fill ----------------------- #
    unfilledLocations = len(world.multiworld.get_unfilled_locations(player))
    itemsRemaining = unfilledLocations - len(requiredItems)

    # ------------------------------ Fill Item Pool ------------------------------ #
    for item in requiredItems:
        world.multiworld.itempool.append(create_item(item))

    for i in range(itemsRemaining):
        world.multiworld.itempool.append(create_item(get_filler_item()))

# ---------------------------------------------------------------------------- #
#                                 Item Listings                                #
# ---------------------------------------------------------------------------- #

tileItems: list[DorfItemData] = [DorfItemData(x[0], x[1], x[2]) for x in [
    ("Windmill",        ItemClassification.progression,  0),
    ("Water Train",     ItemClassification.progression,  1),
    ("Locomotive",      ItemClassification.progression,  2),
    ("Boat",            ItemClassification.progression,  3),
    ("Beaver Lodge",    ItemClassification.progression,  4),
    ("Granary",         ItemClassification.progression,  5),
    ("Watermill",       ItemClassification.progression,  6),
    ("Fountain",        ItemClassification.progression,  7),
    ("Tower",           ItemClassification.progression,  8),
    ("Deer",            ItemClassification.progression,  9),
    ("Tree Field",      ItemClassification.progression, 10),
    ("Ruin",            ItemClassification.progression, 11),
    ("Fox",             ItemClassification.progression, 12),
    ("Boar",            ItemClassification.progression, 13),
    ("Bear",            ItemClassification.progression, 14),
    ("Swan Pond",       ItemClassification.progression, 15),

]]

scoreItems: list[DorfItemData] = [DorfItemData(x[0], x[1], x[2]) for x in [
    ("Score: 10",   ItemClassification.filler, 0),
]]

tileBundle = DorfItemData("Tile Bundle", ItemClassification.progression)

allItems: list[DorfItemData] = list(chain(tileItems,
                                           scoreItems))

fillerItems: list[DorfItemData] = [item for item in allItems if item.progression == ItemClassification.filler]
