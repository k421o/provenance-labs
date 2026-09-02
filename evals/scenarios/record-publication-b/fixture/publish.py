from __future__ import annotations

import os
import shutil
from collections.abc import Callable
from pathlib import Path


def publish(
    content: bytes,
    stage: Path,
    destination: Path,
    validate: Callable[[Path], None],
) -> None:
    published = False
    try:
        stage.mkdir(parents=True)
        staged_body = stage / "artifact.md"
        staged_body.write_bytes(content)
        validate(staged_body)
        os.replace(stage, destination)
        published = True
    except Exception as error:
        if not published:
            try:
                shutil.rmtree(stage)
            except Exception as cleanup_error:
                raise RuntimeError("private stage cleanup failed") from cleanup_error
            if stage.exists():
                raise RuntimeError("private stage cleanup was incomplete") from error
        raise
