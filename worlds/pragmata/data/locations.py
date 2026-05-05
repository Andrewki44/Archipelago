from typing import NamedTuple, Optional
from itertools import chain

# ---------------------------------------------------------------------------- #
#                              Location Data Class                             #
# ---------------------------------------------------------------------------- #

class PragmataLocationData(NamedTuple):
    address: int
    name: str
    id: int
    # missable: bool


escapeHatchOffset: int     = 0x0000
treasureBoxOffset: int     = 0x1000
componentOffset: int       = 0x2000
remOffset: int             = 0x3000
storageExpanderOffset: int = 0x4000
trainingDataOffset: int    = 0x5000
miniCabinOffset: int       = 0x6000
pureLunumOffset: int       = 0x7000
modOffset: int             = 0x8000
cartridgeHolderOffset: int = 0x9000

# ---------------------------------------------------------------------------- #
#                               Location Listings                              #
# ---------------------------------------------------------------------------- #

escapeHatchLocations: list[PragmataLocationData] = [PragmataLocationData(location[1] | escapeHatchOffset, *location) for location in [
    ("Solar Power Plant: Escape Hatch - Sealed Sector Gate",             0),
    ("Solar Power Plant: Escape Hatch - Main Control Lobby",             1),
    ("Mass Production Array: Escape Hatch - Shopping District",          2),
    ("Mass Production Array: Escape Hatch - Interconnecting Passage",    3),
    ("Mass Production Array: Escape Hatch - Office Space",               4),
    ("Mass Production Array: Escape Hatch - Recycling Control",          5),
    ("Mass Production Array: Escape Hatch - Comms Tower Plaza",          6),
    ("Terra Dome: Escape Hatch - Central Lift",                          7),
    ("Terra Dome: Escape Hatch - Envirolytics Lab",                      8),
    ("Terra Dome: Escape Hatch - Meteorology Sim Lab",                   9),
    ("Terra Dome: Escape Hatch - Central Lift Upper Floor",             10),
    ("Terra Dome: Escape Hatch - GeoScience Lab",                       11),
    ("Terra Dome: Escape Hatch - Cultivation Lab",                      12),
    ("Lunum Mines: Escape Hatch - Crane Control Room",                  13),
    ("Lunum Mines: Escape Hatch - Warehouse Entrance",                  14),
    ("Lunum Mines: Escape Hatch - Warehouse Exit",                      15),
    ("Lunum Mines: Escape Hatch - Mining Control Room",                 16),
    ("Lunum Mines: Escape Hatch - Logistics Management",                17),
    ("Lunum Mines: Escape Hatch - Tower Access Point",                  18),
    ("Lunum Mines: Escape Hatch - Mainframe Access",                    19),
    ("Central Port: Escape Hatch - Cargo Terminal",                     20),
    ("Central Port: Escape Hatch - Research Sector Gate",               21),
    ("Central Port: Escape Hatch - Research Sector Lobby",              22),
    ("Central Port: Escape Hatch - Connect Center",                     23),
    ("Central Port: Escape Hatch - Labratory Main Entrance",            24),
    ("Central Port: Escape Hatch - Orbital Elevator Access",            25),
]]


treasureBoxLocations: list[PragmataLocationData] = [PragmataLocationData(location[1] | treasureBoxOffset, *location) for location in [
    ("SPP: Sealed Sector Gate - Behind laser grid with a walker (Safe Box)",                                    0),
    ("SPP: Sealed Sector Gate - Black ground with moving platforms (Safe Box)",                                 1),
    ("SPP: Sealed Sector Gate - Behind Filament Mass (Safe Box)",                                               2),
    ("SPP: Sealed Sector Gate - Behind Filament Mass (Pure Lunum)",                                             3),
    ("SPP: Main Control Lobby - Next to shelter checkpoint (Mod: Hardened Suit)",                               4),
    ("MPA: Test Site Platform - Restaurant Filament Mass (Safe Box)",                                           5),
    ("MPA: Test Site Platform - Nouvelle Filament Mass (Safe Box)",                                             6),
    ("MPA: Shopping District - Entrance - Red Zone (Pure Lunum)",                                               7),
    ("MPA: Shopping District - Entrance - Moving laser grids, opposite mannequins (Mod: Extended Breach)",      8),
    ("MPA: Shopping District - Entrance - Behind 3 walkers, 1st multihack drop (Safe Box)",                     9),
    ("MPA: Shopping District - Entrance - Door behind Beacon2 (Safe Box)",                                     10),
    ("MPA: Shopping District - Entrance - Door behind Beacon2 (Pure Lunum)",                                   11),
    ("MPA: Shopping District - Entrance - Holo Wall (Safe Box)",                                               12),
    ("MPA: Shopping District - Entrance - Behind laser wall next to mannequins + walker (Safe Box)",           13),
    ("MPA: Shopping District - Entrance - Before Bridge (Mod: Close Quaters)",                                 14),
    ("MPA: Shopping District - Entrance - Filament Mass near Beacon2 (Safe Box)",                              15),
    ("MPA: Interconnecting Passage - Above 1st door, 1st Executor Enemy (Mod: Relay Amplfier)",                16),
    ("MPA: Interconnecting Passage - Below Beacon3 (Mod: Long Range Targeting)",                               17),
    ("MPA: Interconnecting Passage - Halfway up zipline after Beacon3 (Safe Box)",                             18),
    ("MPA: Office Space - Next to Shelter Checkpoint (Pure Lunum)",                                            19),
    ("MPA: Office Space - Red Zone (Pure Lunum)",                                                              20),
    ("MPA: Office Space - Red Zone (Mod: Pocket Refinery)",                                                    21),
    ("MPA: Office Space - Left of Red Zone (Safe Box)",                                                        22),
    ("MPA: Office Space - Area under Shelter Checkpoint (Safe Box)",                                           23),
    ("MPA: Office Space - Left of upper Filament Mass (Safe Box)",                                             24),
    ("MPA: Office Space - Upper Filament Mass (Safe Box)",                                                     25),
    ("MPA: Office Space - Dead Filament Mass right of Red Zone 1 (Safe Box)",                                  26),
    ("MPA: Office Space - Dead Filament Mass right of Red Zone 2 (Safe Box)",                                  27),
    ("MPA: Recycling Control - Holo Wall before spinning laser room (Safe Box)",                               28),
    ("MPA: Recycling Control - Above Lim Eraser with 4 walkers (Safe Box)",                                    29),
    ("MPA: Recycling Control - Behind laser wall (Safe Box)",                                                  30),
]]

componentLocations: list[PragmataLocationData] = [PragmataLocationData(location[1] | componentOffset, *location) for location in [
    ("SPP: Power Plant Platform - Left of spawn (Upgrade Material)",                                        0),
    ("SPP: Power Plant Platform - Opposite Lock 1 (Upgrade Material)",                                      1),
    ("SPP: Sealed Sector Gate - Middle of laser grid opposite main locked door (Upgrade Material)",         2),
    ("SPP: Sealed Sector Gate - On roof above shelter checkpoint (Upgrade Material)",                       3),
    ("SPP: Sealed Sector Gate - Behind a locked door opposite shelter checkpoint (Upgrade Material)",       4),
    ("SPP: Sealed Sector Gate - Next to Mini Cabin near Filament Mass (Upgrade Material)",                  5),
    ("SPP: Sealed Sector Gate - Above hack above the main locked door (Upgrade Material)",                  6),
    ("SPP: Sealed Sector Gate - Near moving platform with 2 Watchers and 1 Crusher (Upgrade Material)",     7),
    ("SPP: Sealed Sector Gate - Directly behind main locked door (Upgrade Material)",                       8),
    ("SPP: Sealed Sector Gate - Behind Filament Mass, right of entrance to room (Upgrade Material)",        9),
    ("SPP: Main Control Lobby - Behind door, right of shelter checkpoint (Upgrade Material)",              10),
    ("SPP: Main Control Lobby - Up zipline (Upgrade Material)",                                            11),
    ("MPA: Test Site Platform - Right of spawn (Upgrade Material)",                                        12),
    ("MPA: Test Site Platform - Back corner behind Spider (Upgrade Material)",                             13),
    ("MPA: Test Site Platform - Through door walker comes out of (Upgrade Material)",                      14),
    ("MPA: Test Site Platform - Back right corner of main area, under sideways bus (Upgrade Material)",    15),
    ("MPA: Test Site Platform - Alley next to Yolo Boutique (Upgrade Material)",                           16),
    ("MPA: Test Site Platform - Above-right of main locked gate (Upgrade Material)",                       17),
    ("MPA: Test Site Platform - Filament Mass above Yolo Boutique (Upgrade Material)",                     18),
    ("MPA: Shopping District - Entrance - Above Stardust shop, moving platform (Upgrade Material)",        19),
    ("MPA: Shopping District - Entrance - Opposite Mannequins (Upgrade Material)",                         20),
    ("MPA: Shopping District - Entrance - Drop left before drop to Beacon 2 (Upgrade Material)",           21),
    ("MPA: Shopping District - Entrance - Under Diana's Donuts billboard (Upgrade Material)",              22),
    ("MPA: Shopping District - Entrance - Above Spicy BBQ Burger (Upgrade Material)",                      23),
    ("MPA: Shopping District - Entrance - Next to laser wall with a chest (Upgrade Material)",             24),
    ("MPA: Interconnecting Passage - Next to zipline after Beacon3 (Upgrade Material)",                    25),
    ("MPA: Interconnecting Passage - Before Beacon4 Arena (Upgrade Material)",                             26),
    ("MPA: Office Space - Back-left of room with Shelter Checkpoint (Upgrade Material)",                   27),
    ("MPA: Office Space - Left of Red Zone (From above chest) (Upgrade Material)",                         28),
    ("MPA: Office Space - Left of upper Filament Mass (From above chest) (Upgrade Material)",              29),
    ("MPA: Office Space - Lower Filament Mass right of Red Zone (Upgrade Material)",                       30),
    ("MPA: Recycling Control - Above Shelter Checkpoint (Upgrade Material)",                               31),
    ("MPA: Recycling Control - Left of Lim Eraser upgrade (Upgrade Material)",                             32),
    ("MPA: Recycling Control - Right of Beacon6 (Upgrade Material)",                                       33),
]]

remLocations: list[PragmataLocationData] = [PragmataLocationData(location[1] | remOffset, *location) for location in [
    ("Solar Power Plant: Sealed Sector Gate - REM (Globe)", 0),
    ("Solar Power Plant: Main Control Lobby - REM (Crayons)", 1),
    ("Mass Production Array: Shopping District - REM (Basketball)", 2),
    ("Mass Production Array: Interconnecting Passage - REM (Slide)", 3),
    ("Mass Production Array: Interconnecting Passage - REM (Skateboard)", 4),
    ("Mass Production Array: Interconnecting Passage - REM (CRT TV)", 5),
]]

storageExpanderLocations: list[PragmataLocationData] = [PragmataLocationData(location[1] | storageExpanderOffset, *location) for location in [
    ("Solar Power Plant: Generator Entrance - Storage Expander 1",   0),
]]

trainingDataLocations: list[PragmataLocationData] = [PragmataLocationData(location[1] | trainingDataOffset, *location) for location in [
    ("Solar Power Plant: ",             0),
]]

miniCabinLocations: list[PragmataLocationData] = [PragmataLocationData(location[1] | miniCabinOffset, *location) for location in [
    ("Solar Power Plant: Sealed Sector Gate - Mini Cabin 1",    0),
    ("Solar Power Plant: Sealed Sector Gate - Mini Cabin 2",    1),
    ("Solar Power Plant: Main Control Lobby - Mini Cabin 3",    2),
    ("Mass Production Array: Shopping District - Mini Cabin 1", 3),
    ("Mass Production Array: Interconnecting Passage - Mini Cabin 1", 4),
    ("Mass Production Array: Recycling Control - Mini Cabin 1", 5),
]]

pureLunumLocations: list[PragmataLocationData] = [PragmataLocationData(location[1] | pureLunumOffset, *location) for location in [
    ("Solar Power Plant: Sealed Sector Gate - Pure Lunum 1",    0),
    ("Mass Production Array: Shopping District - Pure Lunum 1",    1),
    ("Mass Production Array: Shopping District - Pure Lunum 2",    2),
    ("Mass Production Array: Office Space - Pure Lunum 1",    3),
    ("Mass Production Array: Office Space - Pure Lunum 2",    4),
]]

modLocations: list[PragmataLocationData] = [PragmataLocationData(location[1] | modOffset, *location) for location in [
    ("Solar Power Plant: Sealed Sector Gate - Mod (Hardened Suit)",    0),
    ("Mass Production Array: Shopping District - Mod (Extended Breach)",    1),
    ("Mass Production Array: Shopping District - Mod (Close Quarters)",    2),
    ("Mass Production Array: Interconnecting Passage - Mod (Relay Amplifier)",    3),
    ("Mass Production Array: Interconnecting Passage - Mod (Long-range Targeting)",    4),
    ("Mass Production Array: Office Space - Mod (Pocket Refinery)",    5),
]]

cartridgeHolderLocations: list[PragmataLocationData] = [PragmataLocationData(location[1] | cartridgeHolderOffset, *location) for location in [
    ("Solar Power Plant: Main Control Lobby - Cartridge Holder 1",    0),
    ("Mass Production Array: Office Space - Cartridge Holder 1",    1),
]]

allLocations = list(chain(escapeHatchLocations,
                          treasureBoxLocations,
                          componentLocations,
                          remLocations,
                          ))
