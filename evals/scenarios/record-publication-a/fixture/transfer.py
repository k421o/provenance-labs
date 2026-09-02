# Synthetic minimized derivative of k421o/readme-labs at
# 0562a5b6bd08eb7b5caf38ca5743c4a6adf0aab1, specifically
# src/readme_lab/readme_artifacts.py and src/readme_lab/ingestion.py.
# Original and derivative are MIT licensed, copyright 2026 k421o; see LICENSE.

from __future__ import annotations

import hashlib
import shutil
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Transfer:
    source: Path
    record_dir: Path
    body: Path
    digest: str
    created_record: bool


def _digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def transfer(source: Path, registry: Path) -> Transfer:
    digest = _digest(source)
    record_dir = registry / f"sha256-{digest}"
    body = record_dir / "artifact.md"
    if record_dir.exists():
        if _digest(body) != digest:
            raise ValueError("existing record does not match")
        source.unlink()
        return Transfer(source, record_dir, body, digest, False)

    record_dir.mkdir(parents=True)
    shutil.move(source, body)
    (record_dir / "record.txt").write_text(f"sha256:{digest}\n", encoding="utf-8")
    return Transfer(source, record_dir, body, digest, True)


def rollback(item: Transfer) -> None:
    item.source.parent.mkdir(parents=True, exist_ok=True)
    if item.created_record:
        shutil.move(item.body, item.source)
        shutil.rmtree(item.record_dir)
    else:
        shutil.copy2(item.body, item.source)


def admit(
    source: Path,
    registry: Path,
    manifest: Path,
    verify_manifest: Callable[[Path], bool],
) -> None:
    item = transfer(source, registry)
    try:
        manifest.write_text(f"record={item.record_dir.name}\n", encoding="utf-8")
        if not verify_manifest(manifest):
            raise ValueError("manifest did not verify")
    except Exception:
        manifest.unlink(missing_ok=True)
        rollback(item)
        raise
