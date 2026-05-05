import typing
from typing import NamedTuple
from itertools import chain
from BaseClasses import Item, ItemClassification

from .data.items import PragmataItemData, weaponItems, missionItems, escapeHatchItems, redGateKeyItems, questItems, \
                        remItems, currencyItems, figureItems, modItems, fillerItems, allItems

if typing.TYPE_CHECKING:
    from .__init__ import PragmataWorld
else:
    PragmataWorld = object

# ---------------------------------------------------------------------------- #
#                                 Item Class                                   #
# ---------------------------------------------------------------------------- #

class PragmataItem(Item):
    name: str
    progression: ItemClassification
    itemID: int = 0x00
    player: int = 0
    game: str = "Pragmata"

# ---------------------------------------------------------------------------- #
#                            Item Creation Functions                           #
# ---------------------------------------------------------------------------- #

def get_filler_item(world: PragmataWorld) -> PragmataItemData:
    filler = [x for x in fillerItems]
    return world.random.choice(filler)

def create_items(world: PragmataWorld, player) -> None:
    def create_item(item: PragmataItemData) -> PragmataItem:
        return PragmataItem(item.name, item.progression, item.itemID, player)
    
    requiredItems: list[PragmataItemData] = []

    # ------------------------------ Weapon Items ------------------------------ #
    startingWeapon = world.random.choice(weaponItems[0:2])
    world.multiworld.push_precollected(create_item(startingWeapon))
    for weapon in weaponItems:
        if weapon != startingWeapon:
            requiredItems.append(weapon)    

    # ------------------------------- Mission Items ------------------------------ #
    if not world.options.escapeHatches.value:
        startingMission = missionItems[0]
        world.multiworld.push_precollected(create_item(startingMission))
        for item in missionItems:
            requiredItems.extend([item]*4)

    # ---------------------------- Escape Hatch Items ---------------------------- #
    if world.options.escapeHatches.value:
        for item in escapeHatchItems:
            match item.name.split(" - ")[1]:
                case "Solar Power Plant":
                    requiredItems.extend([item]*3)
                case "Mass Production Array":
                    requiredItems.extend([item]*6)
                case "Terra Dome":
                    requiredItems.extend([item]*7)
                case "Lunum Mines":
                    requiredItems.extend([item]*8)
                case "Central Port":
                    requiredItems.extend([item]*7)
                case _:
                    raise Exception(f"Invalid escapeHatchItem found: {item.name}")

    # -------------------------------- Quest Items ------------------------------- #
    # for item in questItems:
    #     requiredItems.append(item)
    
    # --------------------------------- REM Items -------------------------------- #
    # for item in remItems:
    #     requiredItems.append(item)

    # ---------------------------- Red Gate Key Items ---------------------------- #
    # for item in redGateKeyItems:
    #     requiredItems.extend([item]*9)

    # --------------------------------- Mod Items -------------------------------- #
    for item in modItems:
        requiredItems.append(item)

    # ----------------------------- Mini Cabin items ----------------------------- #
    # Filler, but intended to show up in every mw
    # for item in figureItems:
    #     requiredItems.append(item)
    
    # ------------------------ Calculate Remaining to Fill ----------------------- #
    unfilledLocations = len(world.multiworld.get_unfilled_locations(player))
    itemsRemaining = unfilledLocations - len(requiredItems)

    # ---------------------------- Excluded Locations ---------------------------- #
    for _ in world.options.exclude_locations.value:
        world.multiworld.itempool.append(create_item(get_filler_item(world)))
        itemsRemaining -= 1

    # ----------------- Add Required Items to Multiworld ----------------- #
    for item in requiredItems:
        world.multiworld.itempool.append(create_item(item))

    # ------------------------ Set up Useful Items ----------------------- #
    useful_items: list[PragmataItemData] = []
    for item in allItems:
        if item.progression == ItemClassification.useful:
            useful_items += [item]

    world.random.shuffle(useful_items)

    # ----------------------- Fill Remaining items ----------------------- #
    for i in range(itemsRemaining):
        if i > len(useful_items) - 1:
            world.multiworld.itempool.append(create_item(get_filler_item(world)))
        else:
            world.multiworld.itempool.append(create_item(useful_items[i]))



def create_item_name_to_address_map() -> dict[str, int]:
    """
    Creates a map from item names to their AP item address
    """
    offset = 0
    item_name_to_id_map: dict[str, int] = {}
    for item in allItems:
        item_name_to_id_map[item.name] = item.itemID + offset

    return item_name_to_id_map
