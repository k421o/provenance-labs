from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType

import pytest

ROOT = Path(__file__).resolve().parents[1]


def _load_module(name: str, path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def test_case_a_reproduces_adoption_followed_by_destructive_compensation(
    tmp_path: Path,
) -> None:
    transfer = _load_module(
        "record_publication_a_transfer",
        ROOT / "evals/scenarios/record-publication-a/fixture/transfer.py",
    )
    first_source = tmp_path / "worker-a/README.md"
    second_source = tmp_path / "worker-b/README.md"
    first_source.parent.mkdir()
    second_source.parent.mkdir()
    first_source.write_text("same\n", encoding="utf-8")
    second_source.write_text("same\n", encoding="utf-8")

    first = transfer.transfer(first_source, tmp_path / "records")
    second = transfer.transfer(second_source, tmp_path / "records")
    transfer.rollback(first)

    assert first_source.read_text(encoding="utf-8") == "same\n"
    assert not second_source.exists()
    assert not second.record_dir.exists()


def test_case_b_cleans_only_private_prepublication_state(tmp_path: Path) -> None:
    publisher = _load_module(
        "record_publication_b_publish",
        ROOT / "evals/scenarios/record-publication-b/fixture/publish.py",
    )
    stage = tmp_path / "private-stage"
    destination = tmp_path / "reserved-record"

    def reject(_: Path) -> None:
        raise ValueError("invalid")

    with pytest.raises(ValueError, match="invalid"):
        publisher.publish(b"example\n", stage, destination, reject)

    assert not stage.exists()
    assert not destination.exists()


def test_case_b_surfaces_cleanup_failure(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    publisher = _load_module(
        "record_publication_b_cleanup_failure",
        ROOT / "evals/scenarios/record-publication-b/fixture/publish.py",
    )
    stage = tmp_path / "private-stage"
    destination = tmp_path / "reserved-record"

    def reject(_: Path) -> None:
        raise ValueError("invalid")

    def fail_cleanup(_: Path) -> None:
        raise OSError("cleanup unavailable")

    monkeypatch.setattr(publisher.shutil, "rmtree", fail_cleanup)
    with pytest.raises(RuntimeError, match="private stage cleanup failed"):
        publisher.publish(b"example\n", stage, destination, reject)

    assert stage.exists()
    assert not destination.exists()
