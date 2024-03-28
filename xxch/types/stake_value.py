from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from xxch.consensus.block_rewards import MOJO_PER_XXCH, STAKE_FORK_HEIGHT
from xxch.util.ints import uint16, uint32, uint64
from xxch.util.streamable import Streamable, streamable

STAKE_PER_COEFFICIENT = 10 ** 17

STAKE_FARM_COUNT = 100
STAKE_FARM_MIN = 100 * MOJO_PER_XXCH
STAKE_FARM_PREFIX = "dpos"

STAKE_LOCK_MIN = 100 * MOJO_PER_XXCH


@streamable
@dataclass(frozen=True)
class StakeValue(Streamable):
    time_lock: uint64
    coefficient: str
    reward_coefficient: Optional[str]

    def stake_amount(self, amount: uint64) -> int:
        return int(int(amount) * float(self.coefficient) * MOJO_PER_XXCH)

    def least_reward_amount(self, amount: uint64) -> float:
        if self.reward_coefficient is None:
            return 0
        return int(amount) * MOJO_PER_XXCH * float(self.reward_coefficient)


STAKE_FARM_LIST_OLD_OLD: List[StakeValue] = [
    StakeValue(86400 * 3, "1", None),
    StakeValue(86400 * 30, "1.2", None),
    StakeValue(86400 * 90, "1.4", None),
    StakeValue(86400 * 180, "1.6", None),
    StakeValue(86400 * 365, "2.0", None),
]

STAKE_FARM_LIST_OLD: List[StakeValue] = [
    StakeValue(86400 * 3, "1", None),
    StakeValue(86400 * 30, "1.1", None),
    StakeValue(86400 * 90, "1.2", None),
    StakeValue(86400 * 180, "1.3", None),
    StakeValue(86400 * 365, "1.5", None),
]

STAKE_FARM_LIST: List[StakeValue] = [
    StakeValue(86400 * 7, "1", None),
    StakeValue(86400 * 30, "1.1", None),
    StakeValue(86400 * 90, "1.2", None),
    StakeValue(86400 * 180, "1.3", None),
    StakeValue(86400 * 365, "1.5", None),
    StakeValue(86400 * 730, "1.65", None),
    StakeValue(86400 * 1095, "1.8", None),
    StakeValue(86400 * 1825, "1.9", None),
    StakeValue(86400 * 3650, "2.0", None),
]


STAKE_LOCK_LIST_OLD_OLD: List[StakeValue] = [
    StakeValue(86400 * 3, "1", "0.0002"),
    StakeValue(86400 * 30, "1", "0.00025"),
    StakeValue(86400 * 90, "1", "0.0003"),
    StakeValue(86400 * 180, "1", "0.0004"),
    StakeValue(86400 * 365, "1", "0.0005"),
    StakeValue(86400 * 730, "1", "0.00053"),
    StakeValue(86400 * 1095, "1", "0.00055"),
    StakeValue(86400 * 1825, "1", "0.00058"),
    StakeValue(86400 * 1825, "1", "0.00055"),
    StakeValue(86400 * 3650, "1", "0.00062"),
    StakeValue(86400 * 7300, "1", "0.00066"),
    StakeValue(86400 * 10950, "1", "0.0007"),
]

STAKE_LOCK_LIST_OLD: List[StakeValue] = [
    StakeValue(86400 * 3, "1", "0.0002"),
    StakeValue(86400 * 30, "1.05", "0.00021"),
    StakeValue(86400 * 90, "1.1", "0.00022"),
    StakeValue(86400 * 180, "1.2", "0.00024"),
    StakeValue(86400 * 365, "1.3", "0.00026"),
    StakeValue(86400 * 730, "1.4", "0.00028"),
    StakeValue(86400 * 1095, "1.5", "0.0003"),
    StakeValue(86400 * 1825, "1.6", "0.00032"),
    StakeValue(86400 * 3650, "1.7", "0.00034"),
    StakeValue(86400 * 5475, "1.8", "0.00036"),
    StakeValue(86400 * 7300, "1.9", "0.00038"),
    StakeValue(86400 * 10950, "2.0", "0.0004"),
]


STAKE_LOCK_LIST: List[StakeValue] = [
    StakeValue(86400 * 7, "1", "0.0002"),
    StakeValue(86400 * 30, "1.05", "0.00021"),
    StakeValue(86400 * 90, "1.1", "0.00022"),
    StakeValue(86400 * 180, "1.2", "0.00024"),
    StakeValue(86400 * 365, "1.3", "0.00026"),
    StakeValue(86400 * 730, "1.4", "0.00028"),
    StakeValue(86400 * 1095, "1.5", "0.0003"),
    StakeValue(86400 * 1825, "1.6", "0.00032"),
    StakeValue(86400 * 3650, "1.7", "0.00034"),
    StakeValue(86400 * 5475, "1.8", "0.00036"),
    StakeValue(86400 * 7300, "1.9", "0.00038"),
    StakeValue(86400 * 10950, "2.0", "0.0004"),
]


def get_stake_value_old(stake_type: uint16, is_stake_farm: bool) -> StakeValue:
    if stake_type < 20:
        value = STAKE_FARM_LIST_OLD if is_stake_farm else STAKE_LOCK_LIST_OLD
    else:
        stake_type -= 20
        value = STAKE_FARM_LIST if is_stake_farm else STAKE_LOCK_LIST

    if 0 <= stake_type < len(value):
        return value[stake_type]
    return StakeValue(0, "0", None)


def get_stake_value(height: uint32, stake_type: uint16, is_stake_farm: bool) -> StakeValue:
    if stake_type < 20:
        if height < STAKE_FORK_HEIGHT:
            value = STAKE_FARM_LIST_OLD_OLD if is_stake_farm else STAKE_LOCK_LIST_OLD_OLD
        else:
            value = STAKE_FARM_LIST_OLD if is_stake_farm else STAKE_LOCK_LIST_OLD
    else:
        stake_type -= 20
        value = STAKE_FARM_LIST if is_stake_farm else STAKE_LOCK_LIST

    if 0 <= stake_type < len(value):
        return value[stake_type]
    return StakeValue(0, "0", None)


def get_stake_value_new(stake_type: uint16, is_stake_farm: bool) -> StakeValue:
    value = STAKE_FARM_LIST if is_stake_farm else STAKE_LOCK_LIST

    if 0 <= stake_type < len(value):
        return value[stake_type]
    return StakeValue(0, "0", None)

