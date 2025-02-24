from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from blspy import G1Element
from chia.pools.pool_wallet_info import PoolState
from chia.types.blockchain_format.sized_bytes import bytes32
from chia.types.coin_spend import CoinSpend
from chia.util.ints import uint64
from chia.util.streamable import streamable, Streamable


@streamable
@dataclass(frozen=True)
class FarmerRecord(Streamable):
    launcher_id: bytes32  # This uniquely identifies the singleton on the blockchain (ID for this farmer)
    p2_singleton_puzzle_hash: bytes32  # Derived from the launcher id, delay_time and delay_puzzle_hash
    delay_time: uint64  # Backup time after which farmer can claim rewards directly, if pool unresponsive
    delay_puzzle_hash: bytes32  # Backup puzzlehash to claim rewards
    authentication_public_key: G1Element  # This is the latest public key of the farmer (signs all partials)
    singleton_tip: CoinSpend  # Last coin spend that is buried in the blockchain, for this singleton
    singleton_tip_state: PoolState  # Current state of the singleton
    points: uint64  # Total points accumulated since last rest (or payout)
    difficulty: uint64  # Current difficulty for this farmer
    payout_instructions: str  # This is where the pool will pay out rewards to the farmer
    is_pool_member: bool  # If the farmer leaves the pool, this gets set to False
    left_at: Optional[str]
    left_last_at: Optional[str]
    email: Optional[str]
    estimated_size: uint64
    last_block_timestamp: Optional[uint64]
    last_block_etw: Optional[uint64]
    name: Optional[str]
    fcm_token: Optional[str]
    push_missing_partials_hours: Optional[uint64]
    push_block_farmed: Optional[bool]
    custom_difficulty: Optional[str]
    minimum_payout: Optional[uint64]

    @property
    def left_at_datetime(self):
        if self.left_at:
            return datetime.fromisoformat(self.left_at)

    @property
    def left_last_at_datetime(self):
        if self.left_last_at:
            return datetime.fromisoformat(self.left_last_at)
