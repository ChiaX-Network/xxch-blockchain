from __future__ import annotations

from typing import Any, Dict

from xxch.types.blockchain_format.sized_bytes import bytes32
from xxch.util.ints import uint8, uint32, uint64, uint128

from .constants import ConsensusConstants

DEFAULT_CONSTANTS = ConsensusConstants(
    SLOT_BLOCKS_TARGET=uint32(32),
    MIN_BLOCKS_PER_CHALLENGE_BLOCK=uint8(16),  # Must be less than half of SLOT_BLOCKS_TARGET
    MAX_SUB_SLOT_BLOCKS=uint32(128),  # Must be less than half of SUB_EPOCH_BLOCKS
    NUM_SPS_SUB_SLOT=uint32(64),  # Must be a power of 2
    SUB_SLOT_ITERS_STARTING=uint64(2**27),
    # DIFFICULTY_STARTING is the starting difficulty for the first epoch, which is then further
    # multiplied by another factor of DIFFICULTY_CONSTANT_FACTOR, to be used in the VDF iter calculation formula.
    DIFFICULTY_CONSTANT_FACTOR=uint128(2**66),
    DIFFICULTY_STARTING=uint64(8),
    DIFFICULTY_CHANGE_MAX_FACTOR=uint32(3),  # The next difficulty is truncated to range [prev / FACTOR, prev * FACTOR]
    # These 3 constants must be changed at the same time
    SUB_EPOCH_BLOCKS=uint32(384),  # The number of blocks per sub-epoch, mainnet 384
    EPOCH_BLOCKS=uint32(4608),  # The number of blocks per epoch, mainnet 4608. Must be multiple of SUB_EPOCH_SB
    SIGNIFICANT_BITS=8,  # The number of bits to look at in difficulty and min iters. The rest are zeroed
    DISCRIMINANT_SIZE_BITS=1024,  # Max is 1024 (based on ClassGroupElement int size)
    NUMBER_ZERO_BITS_PLOT_FILTER=9,  # H(plot signature of the challenge) must start with these many zeroes
    MIN_PLOT_SIZE=32,  # 32 for mainnet
    MAX_PLOT_SIZE=50,
    SUB_SLOT_TIME_TARGET=600,  # The target number of seconds per slot, mainnet 600
    NUM_SP_INTERVALS_EXTRA=3,  # The number of sp intervals to add to the signage point
    MAX_FUTURE_TIME2=2 * 60,  # The next block can have a timestamp of at most these many seconds in the future
    NUMBER_OF_TIMESTAMPS=11,  # Than the average of the last NUMBER_OF_TIMESTAMPS blocks
    # Used as the initial cc rc challenges, as well as first block back pointers, and first SES back pointer
    # We override this value based on the chain being run (testnet0, testnet1, mainnet, etc)
    # Default used for tests is std_hash(b'')
    GENESIS_CHALLENGE=bytes32.fromhex("e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"),
    # Forks of xxch should change this value to provide replay attack protection. This is set to mainnet genesis chall
    AGG_SIG_ME_ADDITIONAL_DATA=bytes.fromhex("4c942ec7c30d7e28c6a755a971dc82f4a66ec297982996453a938df2c0fe1c88"),
    GENESIS_PRE_FARM_POOL_PUZZLE_HASH=bytes32.fromhex(
        "fe20d6d8f5735fbf3e25f08d570cc7906f61881a90abda9f76a7ec9e7a4cc5ce"
    ),
    GENESIS_PRE_FARM_FARMER_PUZZLE_HASH=bytes32.fromhex(
        "fcd909c1685850a7e341e246406aec79e58bc9ec0b09b02842dea9f166293fba"
    ),
    GENESIS_COMMUNITY_PUZZLE_HASH=bytes32.fromhex(
        "580f643b96a42601bef2af874861dc9b78a5559e2bda03a1214eaa1c05ec79fe"
    ),
    FEES_PUZZLE_HASH=bytes32.fromhex(
        "8888888888888888888888888888888888888888888888888888888888888888"
    ),
    MAX_VDF_WITNESS_SIZE=64,
    # Size of mempool = 10x the size of block
    MEMPOOL_BLOCK_BUFFER=10,
    # Max coin amount, fits into 64 bits
    MAX_COIN_AMOUNT=uint64((1 << 64) - 1),
    # Max block cost in clvm cost units
    MAX_BLOCK_COST_CLVM=11000000000,
    # The cost per byte of generator program
    COST_PER_BYTE=(12000),
    WEIGHT_PROOF_THRESHOLD=uint8(2),
    BLOCKS_CACHE_SIZE=uint32(4608 + (128 * 4)),
    WEIGHT_PROOF_RECENT_BLOCKS=uint32(1000),
    # Allow up to 33 blocks per request. This defines the max allowed difference
    # between start and end in the block request message. But the range is
    # inclusive, so the max allowed range of 32 is a request for 33 blocks
    # (which is allowed)
    MAX_BLOCK_COUNT_PER_REQUESTS=uint32(32),
    MAX_GENERATOR_SIZE=uint32(1000000),
    MAX_GENERATOR_REF_LIST_SIZE=uint32(512),  # Number of references allowed in the block generator ref list
    POOL_SUB_SLOT_ITERS=uint64(37600000000),  # iters limit * NUM_SPS
    SOFT_FORK2_HEIGHT=uint32(0),
    # June 2024
    HARD_FORK_HEIGHT=uint32(1016000),
    HARD_FORK_FIX_HEIGHT=uint32(1016000),
    # June 2027
    PLOT_FILTER_128_HEIGHT=uint32(6062000),
    # June 2030
    PLOT_FILTER_64_HEIGHT=uint32(11112000),
    # June 2033
    PLOT_FILTER_32_HEIGHT=uint32(16163000),
)


def update_testnet_overrides(network_id: str, overrides: Dict[str, Any]) -> None:
    if network_id != "testnet0":
        return
    # activate softforks immediately on testnet
    # these numbers are supposed to match initial-config.yaml
    if "SOFT_FORK2_HEIGHT" not in overrides:
        overrides["SOFT_FORK2_HEIGHT"] = 3000000
    if "HARD_FORK_HEIGHT" not in overrides:
        overrides["HARD_FORK_HEIGHT"] = 2997292
    if "HARD_FORK_FIX_HEIGHT" not in overrides:
        overrides["HARD_FORK_FIX_HEIGHT"] = 3426000
    if "PLOT_FILTER_128_HEIGHT" not in overrides:
        overrides["PLOT_FILTER_128_HEIGHT"] = 3061804
    if "PLOT_FILTER_64_HEIGHT" not in overrides:
        overrides["PLOT_FILTER_64_HEIGHT"] = 8010796
    if "PLOT_FILTER_32_HEIGHT" not in overrides:
        overrides["PLOT_FILTER_32_HEIGHT"] = 13056556
