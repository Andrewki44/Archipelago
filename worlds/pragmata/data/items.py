import typing
from typing import NamedTuple
from itertools import chain
from BaseClasses import Item, ItemClassification

# ---------------------------------------------------------------------------- #
#                                Item Data Class                               #
# ---------------------------------------------------------------------------- #

class PragmataItemData(NamedTuple):
    name: str
    progression: ItemClassification
    itemID: int = 0x00
    player: int = 0


missionOffset: int      = 0x0000
weaponOffset: int       = 0x1000
keyOffset: int          = 0x2000
remOffset: int          = 0x3000
currencyOffset: int     = 0x4000
redGateKeyOffset: int   = 0x5000
figureOffset: int       = 0x6000
modOffset: int          = 0x7000
trainingDataOffset: int = 0x8000
questOffset: int        = 0x9000
upgradeOffset: int      = 0xA000

# ---------------------------------------------------------------------------- #
#                                 Item Listings                                #
# ---------------------------------------------------------------------------- #

weaponItems: list[PragmataItemData] = [PragmataItemData(x[0], x[1], x[2] | weaponOffset) for x in [
    ("Grip Gun",            ItemClassification.progression,  0x00),
    ("Pulse Carbine",       ItemClassification.progression,  0x01),
    ("Shockwave Gun",       ItemClassification.progression,  0x02),
    ("Charge Piercer",      ItemClassification.progression,  0x03),
    ("Photon Laser",        ItemClassification.progression,  0x04),
    ("Homing Missiles",     ItemClassification.progression,  0x05),
    ("Jackhammer",          ItemClassification.progression,  0x06),
    ("Lim Cannon",          ItemClassification.progression,  0x07),
    ("Stasis Net",          ItemClassification.progression,  0x08),
    ("Riot Blaster",        ItemClassification.progression,  0x09),
    ("Sticky Bombs",        ItemClassification.progression,  0x0A),
    ("Code Generator",      ItemClassification.progression,  0x0B),
    ("Hacking Mines",       ItemClassification.progression,  0x0C),
    ("Decoy Generator",     ItemClassification.progression,  0x0D),
    ("Impact Barrier",      ItemClassification.progression,  0x0E),
    ("Drone Hive",          ItemClassification.progression,  0x0F),
]]

# missionItems: list[PragmataItemData] = [PragmataItemData(x[0], x[1], x[2] | missionOffset) for x in [
#     ("Mission Unlock - Solar Power Plant",      ItemClassification.progression, 0x00),
#     ("Mission Unlock - Mass Production Array",  ItemClassification.progression, 0x01),
#     ("Mission Unlock - Terra Dome",             ItemClassification.progression, 0x02),
#     ("Mission Unlock - Lunum Mines",            ItemClassification.progression, 0x03),
#     ("Mission Unlock - Central Port",           ItemClassification.progression, 0x04),
# ]]

missionItems: list[PragmataItemData] = [PragmataItemData(x[0], x[1], x[2] | missionOffset) for x in [
    ("Progressive Mission Unlock",      ItemClassification.progression, 0x00),
]]

escapeHatchItems: list[PragmataItemData] = [PragmataItemData(x[0], x[1], x[2] | missionOffset) for x in [
    ("Progressive Escape Hatch: Solar Power Plant",        ItemClassification.progression,  0x00),
    ("Progressive Escape Hatch: Mass Production Array",    ItemClassification.progression,  0x01),
    ("Progressive Escape Hatch: Terra Dome",               ItemClassification.progression,  0x02),
    ("Progressive Escape Hatch: Lunum Mines",              ItemClassification.progression,  0x03),
    ("Progressive Escape Hatch: Central Port",             ItemClassification.progression,  0x04),
]]

trainingDataItems: list[PragmataItemData] = [PragmataItemData(x[0], x[1], x[2] | trainingDataOffset) for x in [
    ("Training Data: Terra Dome Entrance",  ItemClassification.progression,  0x00),
    ("Training Data: Soil Research",        ItemClassification.progression,  0x01),
    ("Training Data: Warehouse",            ItemClassification.progression,  0x02),
    ("Training Data: Nexus Tower",          ItemClassification.progression,  0x03),
    ("Training Data: Research Sector",      ItemClassification.progression,  0x04),
    ("Training Data: Lunafilament Lab",     ItemClassification.progression,  0x05),
]]

redGateKeyItems: list[PragmataItemData] = [PragmataItemData(x[0], x[1], x[2] | keyOffset) for x in [
    ("Red Gate Key",    ItemClassification.progression, 0x00)
]]

remItems: list[PragmataItemData] = [PragmataItemData(x[0], x[1], x[2] | remOffset) for x in [
    ("REM: Globe",       ItemClassification.progression,   0x00),
    ("REM: Crayons",     ItemClassification.progression,   0x01),
    ("REM: CRT TV",      ItemClassification.progression,   0x02),
    ("REM: Slide",       ItemClassification.progression,   0x03),
    ("REM: Balloons",    ItemClassification.progression,   0x04),
    ("REM: Basketball",  ItemClassification.progression,   0x05),
    ("REM: RC Car",      ItemClassification.progression,   0x06),
    ("REM: Skateboard",  ItemClassification.progression,   0x07),
    ("REM: Flowers",     ItemClassification.progression,   0x08),
    ("REM: Swing",       ItemClassification.progression,   0x09),
    ("REM: Campfire",    ItemClassification.progression,   0x0A),
    ("REM: Bug Net",     ItemClassification.progression,   0x0B),
    ("REM: Tent",        ItemClassification.progression,   0x0C),
    ("REM: Parasol",     ItemClassification.progression,   0x0D),
    ("REM: Water Gun",   ItemClassification.progression,   0x0E),
    ("REM: Sandcastle",  ItemClassification.progression,   0x0F),
]]

currencyItems: list[PragmataItemData] = [PragmataItemData(x[0], x[1], x[2] | currencyOffset) for x in [
    ("Lunafilament x100",       ItemClassification.filler,       0x00),
    ("Upgrade Component x2",    ItemClassification.useful,       0x01),
    ("Pure Lunum",              ItemClassification.useful,       0x02),
    ("Cabin Coins",             ItemClassification.progression,  0x03),
]]

# Excluded from allItems, so that additional copies aren't given, but garuntees 1 of each, even though filler.
figureItems: list[PragmataItemData] = [PragmataItemData(x[0], x[1], x[2] | figureOffset) for x in [
    ("Mini Cabin 1",    ItemClassification.filler, 0x00),
    ("Mini Cabin 2",    ItemClassification.filler, 0x01),
    ("Mini Cabin 3",    ItemClassification.filler, 0x02),
    ("Mini Cabin 4",    ItemClassification.filler, 0x03),
    ("Mini Cabin 5",    ItemClassification.filler, 0x04),
    ("Mini Cabin 6",    ItemClassification.filler, 0x05),
    ("Mini Cabin 7",    ItemClassification.filler, 0x06),
    ("Mini Cabin 8",    ItemClassification.filler, 0x07),
    ("Mini Cabin 9",    ItemClassification.filler, 0x08),
    ("Mini Cabin 10",   ItemClassification.filler, 0x09),
    ("Mini Cabin 11",   ItemClassification.filler, 0x0A),
    ("Mini Cabin 12",   ItemClassification.filler, 0x0B),
    ("Mini Cabin 13",   ItemClassification.filler, 0x0C),
    ("Mini Cabin 14",   ItemClassification.filler, 0x0D),
    ("Mini Cabin 15",   ItemClassification.filler, 0x0E),
]]

modItems: list[PragmataItemData] = [PragmataItemData(x[0], x[1], x[2] | modOffset) for x in [
    ("Mod: Hardened Suit",          ItemClassification.useful,  0x00),
    ("Mod: Pocket Refinery",        ItemClassification.useful,  0x01),
    ("Mod: Extended Breach",        ItemClassification.useful,  0x02),
    ("Mod: Close Quarters",         ItemClassification.useful,  0x03),
    ("Mod: Long-Range Targeting",   ItemClassification.useful,  0x04),
    ("Mod: Relay Amplifier",        ItemClassification.useful,  0x05),
    ("Mod: Overclocked Weaponry",   ItemClassification.useful,  0x06),
    ("Mod: Self-Defense Response",  ItemClassification.useful,  0x07),
    ("Mod: Skirmisher",             ItemClassification.useful,  0x08),
    ("Mod: Collateral Damage",      ItemClassification.useful,  0x09),
    ("Mod: Recursive Learning",     ItemClassification.useful,  0x0A),
    ("Mod: Aggressive Defense",     ItemClassification.useful,  0x0B),
    ("Mod: Cheap Shot",             ItemClassification.useful,  0x0C),
    ("Mod: Precision Shot",         ItemClassification.useful,  0x0D),
    ("Mod: Quick Fix",              ItemClassification.useful,  0x0E),
    ("Mod: Hyperfocus",             ItemClassification.useful,  0x0F),
    ("Mod: Optimal Performance",    ItemClassification.useful,  0x10),
    ("Mod: Performance Boost",      ItemClassification.useful,  0x11),
    ("Mod: Equilibrium",            ItemClassification.useful,  0x12),
    ("Mod: Analog Aggression",      ItemClassification.useful,  0x13),
    ("Mod: Digital Dominance",      ItemClassification.useful,  0x14),
    ("Mod: Nice Nodes",             ItemClassification.useful,  0x15),
    ("Mod: Eagle Eye",              ItemClassification.useful,  0x16),
    ("Mod: Synaptic Response",      ItemClassification.useful,  0x17),
    ("Mod: Economize",              ItemClassification.useful,  0x18),
    ("Mod: Last Resort",            ItemClassification.useful,  0x19),
    ("Mod: Reinforced Casing",      ItemClassification.useful,  0x1A),
    ("Mod: Untapped Potential",     ItemClassification.useful,  0x1B),
    ("Mod: Heat transfer",          ItemClassification.useful,  0x1C),
    ("Mod: Cursed",                 ItemClassification.useful,  0x1D),
    ("Mod: Adrenaline Flood",       ItemClassification.useful,  0x1E),
    ("Mod: Faster Moves",           ItemClassification.useful,  0x1F),
    ("Mod: Target Weakness",        ItemClassification.useful,  0x20),
    ("Mod: Critical Response",      ItemClassification.useful,  0x21),
    ("Mod: Sympathetic Hacking",    ItemClassification.useful,  0x22),
    ("Mod: Better Lucky",           ItemClassification.useful,  0x23),
    ("Mod: Cyber Thief",            ItemClassification.useful,  0x24),
    ("Mod: Grace",                  ItemClassification.useful,  0x25),
    ("Mod: Slowdown",               ItemClassification.useful,  0x26),
    ("Mod: Black Box",              ItemClassification.useful,  0x27),
]]

questItems: list[PragmataItemData] = [PragmataItemData(x[0], x[1], x[2] | questOffset) for x in [
    ("Lim Eraser",      ItemClassification.progression,  0x00),
    ("Cleansing",       ItemClassification.progression,  0x01),
]]

upgradeItems: list[PragmataItemData] = [PragmataItemData(x[0], x[1], x[2] | upgradeOffset) for x in [
    ("Cartridge Holder",    ItemClassification.progression,  0x00),
    ("Storage Expander",    ItemClassification.progression,  0x01),
]]

allItems: list[PragmataItemData] = list(chain(weaponItems,
                                              missionItems,
                                              redGateKeyItems,
                                              remItems,
                                              currencyItems,
                                              figureItems,
                                              modItems,
                                              questItems
                                              ))

fillerItems: list[PragmataItemData] = [item for item in allItems 
                                       if item.progression == ItemClassification.filler 
                                       and item not in figureItems]