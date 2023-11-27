from __future__ import annotations

from xxch.util.ints import uint32, uint64

# 1 Xxch coin = 1,000,000,000,000 = 1 trillion mojo.
MOJO_PER_XXCH = 1000000000000
_height_change = 1000000
_reward_per = [
    (7000000, 0.2),
    (14000000, 0.1),
    (21000000, 0.05),
    (28000000, 0.025),
    (50000000, 0.0125),
]


def __calculate_reward(height: uint32, index: int = -1) -> int:
    _height, _reward = _reward_per[index]
    if height >= _height if index == -1 else height < _height:
        return int(_reward * MOJO_PER_XXCH)
    else:
        index += 1
        return __calculate_reward(height, index)


def calculate_stake_farm_reward(height: uint32) -> int:
    return __calculate_reward(height) * 4


def calculate_pool_reward(height: uint32) -> uint64:
    """
    Returns the pool reward at a certain block height. The pool earns 7/8 of the reward in each block. If the farmer
    is solo farming, they act as the pool, and therefore earn the entire block reward.
    They will likely come early, if the network space and VDF
    rates increase continuously.
    """
    if height == 0:
        return uint64(int((7 / 8) * 1000000 * MOJO_PER_XXCH))
    return uint64(int((7 / 8 if height > _height_change else 0) * __calculate_reward(height)))


def calculate_base_farmer_reward(height: uint32) -> uint64:
    """
    Returns the base farmer reward at a certain block height.
    The base fee reward is 1/8 of total block reward

    Returns the coinbase reward at a certain block height. They will likely come early, if the network space and VDF
    rates increase continuously.
    """
    if height == 0:
        return uint64(int((1 / 8) * 1000000 * MOJO_PER_XXCH))
    return uint64(int((1 / 8 if height > _height_change else 1) * __calculate_reward(height)))


def calculate_community_reward(height: uint32) -> uint64:
    """
    Community Rewards: 6% every block
    """
    return uint64(int((6 / 100) * calculate_stake_farm_reward(height)))

