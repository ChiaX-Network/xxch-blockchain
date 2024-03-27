from __future__ import annotations

from xxch.util.ints import uint32, uint64

# 1 Xxch coin = 1,000,000,000,000 = 1 trillion mojo.
MOJO_PER_XXCH = 1000000000000
STAKE_FORK_HEIGHT = 600000


def calculate_pool_reward(height: uint32) -> uint64:
    """
    Returns the pool reward at a certain block height. The pool earns 7/8 of the reward in each block. If the farmer
    is solo farming, they act as the pool, and therefore earn the entire block reward.
    These halving events will not be hit at the exact times
    (3 years, etc), due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """

    if height == 0:
        return uint64(int((7 / 8) * 1000000 * MOJO_PER_XXCH))
    return uint64(0)


def calculate_base_farmer_reward(height: uint32) -> uint64:
    """
    Returns the base farmer reward at a certain block height.
    The base fee reward is 1/8 of total block reward

    Returns the coinbase reward at a certain block height. These halving events will not be hit at the exact times
    (3 years, etc), due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """

    if height == 0:
        return uint64(int((1 / 8) * 1000000 * MOJO_PER_XXCH))
    return uint64(int(0.2 * MOJO_PER_XXCH))


def calculate_community_reward(height: uint32) -> uint64:
    if height < STAKE_FORK_HEIGHT:
        return uint64(int(0.048 * MOJO_PER_XXCH))
    return uint64(48 * MOJO_PER_XXCH)


def calculate_stake_farm_reward(height: uint32) -> uint64:
    return uint64(int(0.8 * MOJO_PER_XXCH))


def calculate_stake_lock_reward(scale: float) -> int:
    return int(4608 * scale * MOJO_PER_XXCH)
