"""
cres_signal_sim

Synthetic CRES signal + track simulator.

Primary entry points:
- cres_signal_sim.nodes.pipeline.run_from_config
- CLI: `cres-sim <config.yaml>`
"""
from __future__ import annotations

__version__ = "0.1.0"

from .nodes.pipeline import run_from_config  # noqa: E402

__all__ = ["__version__", "run_from_config"]
