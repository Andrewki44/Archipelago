from typing import Any
from dataclasses import dataclass
from Options import OptionGroup, PerGameCommonOptions, Range


class ScoreRequirement(Range):
    """
    Sets the score requirement to goal
    """
    display_name = "Score Requirement"
    default = 1000
    range_start = 100
    range_end = 10000


@dataclass
class DorfOptions(PerGameCommonOptions):
    score_requirement = ScoreRequirement


def create_option_groups() -> list[OptionGroup]:
    option_group_list: list[OptionGroup] = []
    for name, options in dorf_option_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))

    return option_group_list


dorf_option_groups: dict[str, list[Any]] = {
    "Goal Options": [
        ScoreRequirement,
    ],
}