from BaseClasses import Entrance, Region
from rule_builder.rules import Has, Rule
import typing
import pkgutil
import json

# from .__init__  import PragmataWorld
from .items     import PragmataItem
from .locations import PragmataLocation, create_locations
from .rules     import missionRuleDict, escapeHatchRuleDict

if typing.TYPE_CHECKING:
    from .__init__ import PragmataWorld
else:
    PragmataWorld = object

class PragmataRegionData(dict):
    @property
    def name(self) -> str:
        return self["name"]
    @property
    def id(self) -> int:
        return self["id"]
    @property
    def escapeHatches(self) -> list[int]:
        return self.get("escape_hatches")
    @property
    def treasureBoxes(self) -> list[int]:
        return self.get("treasure_boxes")
    @property
    def components(self) -> list[int]:
        return self.get("components")
    @property
    def rem(self) -> list[int]:
        return self.get("rem")
    @property
    def storageExpanders(self) -> list[int]:
        return self.get("storage_expanders")
    @property
    def trainingData(self) -> list[int]:
        return self.get("training_data")
    @property
    def miniCabin(self) -> list[int]:
        return self.get("mini_cabin")
    @property
    def cartridgeHolders(self) -> list[int]:
        return self.get("cartridge_holders")
    @property
    def leadsTo(self) -> list[int]:
        return self.get("leads_to")
    @property
    def missionRules(self) -> list[str]:
        return self.get("mission_rules")
    @property
    def escapeHatchRules(self) -> list[int]:
        return self.get("escape_hatch_rules")


# ---------------------------------------------------------------------------- #
#                                Region Creation                               #
# ---------------------------------------------------------------------------- #

def create_regions(world: PragmataWorld, player: int) -> None:
    # shelter = Region("The Shelter", player, world.multiworld)
    # world.multiworld.regions.append(shelter)

    regionFile = pkgutil.get_data(__name__, "data/regions.json")
    regionDataList = json.loads(regionFile)
    regionDataList = [PragmataRegionData(x) for x in regionDataList]
    
    regionDict: dict[int, Region] = dict()
    missionRules: dict[int, list[str]] = dict()
    escapeHatchRules: dict[int, int] = dict()

    # ------------------------ Create Regions & Locations ------------------------ #
    for regionData in regionDataList:
        newRegion = Region(regionData.name, player, world.multiworld)
        regionDict[regionData.id] = newRegion
        world.multiworld.regions.append(newRegion)
        create_locations(player, newRegion, regionData)
        if len(regionData.missionRules) > 0:
            missionRules[regionData.id] = regionData.missionRules
        if len(regionData.escapeHatchRules) > 0:
            escapeHatchRules[regionData.id] = regionData.escapeHatchRules
    
    # ------------------------------ Entrance Rules ------------------------------ #
    for regionData in regionDataList:
        if regionData.leadsTo:
            currentRegion = regionDict[regionData.id]
            for regionId in regionData.leadsTo:
                otherRegion = regionDict[regionId]
                entrance: Entrance = currentRegion.connect(otherRegion)
                
                rules: int | list[str] = None
                ruleDict: dict
                if world.options.escapeHatches.value:
                    rules = escapeHatchRules.get(regionId)
                    ruleDict = escapeHatchRuleDict
                else:
                    rules = missionRules.get(regionId)
                    ruleDict = missionRuleDict
                newRule: Rule = None

                if rules is not None:
                    for rule in rules:
                        regionRule: Rule | None = ruleDict.get(rule)
                        if newRule is not None:
                            newRule &= regionRule
                        else:
                            newRule = regionRule

                if newRule is not None:
                    world.set_rule(entrance, newRule)

    # -------------------------- Top Level Entrace Rules ------------------------- #
    # top_level_regions: list[tuple[Region, Entrance]] = []
    # for regionId, otherRegion in regionDict.items():
    #     if regionId == 0:
    #         continue
    #     if len(otherRegion.entrances) == 0:
    #         shelterEntrance: Entrance = regionDict[0].connect(otherRegion)
            
    #         rules: int | list[str] = None
    #         ruleDict: dict
    #         if world.options.escapeHatches.value:
    #             rules = escapeHatchRules.get(regionId)
    #             ruleDict = escapeHatchRuleDict
    #         else:
    #             rules = missionRules.get(regionId)
    #             ruleDict = missionRuleDict
    #         newRule: Rule = None

    #         if rules is not None:
    #             for rule in rules:
    #                 regionRule: Rule | None = ruleDict.get(rule)
    #                 if newRule is not None:
    #                     newRule &= regionRule
    #                 else:
    #                     newRule = regionRule

    #         if newRule is not None:
    #             world.set_rule(shelterEntrance, newRule)
    #         top_level_regions.append((otherRegion, shelterEntrance))

    # ---------------------------------------------------------------------------- #
    #                               Victory Condition                              #
    # ---------------------------------------------------------------------------- #
    
    regionDict[0].add_event("Goal", "Victory", rule=Has("Progressive Mission Unlock", count=5), location_type=PragmataLocation, item_type=PragmataItem)
    world.set_completion_rule(Has("Victory"))