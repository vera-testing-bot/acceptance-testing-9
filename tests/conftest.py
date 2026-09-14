"""Make ``shard_app`` importable from the in-tree ``src`` layout.

Relocated here from ``test_shard_app.py`` so the test module can keep all of
its imports at the top of the file in a single, conventionally ordered block.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
