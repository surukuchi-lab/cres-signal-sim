from __future__ import annotations

from pathlib import Path

from cres_signal_sim.config import load_config
from cres_signal_sim.nodes.pipeline import run_pipeline


def test_smoke_runs_with_placeholder(tmp_path: Path):
    # Minimal config: use placeholder field (no map) and short duration
    cfg_text = """
simulation:
  starting_time_s: 0.0
  track_length_s: 1.0e-3
electron:
  pitch_angle_deg: 89.0
trap:
  field_map_npz: "does_not_exist.npz"
  generate_if_missing: false
  placeholder_if_missing: true
signal:
  fs_if_hz: 1.0e6
  if_decim: 1
output:
  out_dir: "{out_dir}"
  basename: "t"
  write_npz: true
  write_root: false
"""
    cfg_path = tmp_path / "cfg.yaml"
    cfg_path.write_text(cfg_text.format(out_dir=str(tmp_path / "out")))

    cfg = load_config(cfg_path)
    ctx = run_pipeline(cfg)

    assert "signal_result" in ctx
    assert Path(ctx["npz_path"]).exists()
