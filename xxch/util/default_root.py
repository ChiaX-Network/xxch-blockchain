from __future__ import annotations

import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("XXCH_ROOT", "~/.xxch/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("XXCH_KEYS_ROOT", "~/.xxch_keys"))).resolve()

SIMULATOR_ROOT_PATH = Path(os.path.expanduser(os.getenv("XXCH_SIMULATOR_ROOT", "~/.xxch/simulator"))).resolve()
