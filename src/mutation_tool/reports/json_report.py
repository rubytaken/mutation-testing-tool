from __future__ import annotations

import json
from pathlib import Path

from mutation_tool.models import SessionResult
from mutation_tool.reports.serialize import session_to_dict


def write_json_report(session: SessionResult, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(session_to_dict(session, output_path), indent=2),
        encoding="utf-8",
    )
    return output_path
