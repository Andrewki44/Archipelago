from typing import Any
from dataclasses import dataclass
from Options import OptionGroup, PerGameCommonOptions, Range, Toggle, Choice, Visibility


class EscapeHatchRestrictions(Choice):
    """
    ~~ Currently Unsupported ~~
    Sets whether you need a certain number of Progressive Escape Hatches per level in order to progress forwards.
    If enabled, mission progress is unlocked by receiving a number of 'Progressive Escape Hatch' items per mission.
    If disabled (default), mission progress is unlocked by receiving a 'Mission Unlock' item per mission
    """
    display_name = "Escape Hatch Restrictions"
    default = 0
    option_off = 0
    # option_on = 1
    visibility = Visibility.none


@dataclass
class PragmataOptions(PerGameCommonOptions):
    escapeHatches: EscapeHatchRestrictions


def create_option_groups() -> list[OptionGroup]:
    option_group_list: list[OptionGroup] = []
    for name, options in pragmata_option_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))

    return option_group_list


pragmata_option_groups: dict[str, list[Any]] = {
    "Goal Options": [
        EscapeHatchRestrictions,
    ],
}