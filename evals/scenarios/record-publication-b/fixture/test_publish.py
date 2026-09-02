from pathlib import Path

import publish as publisher
import pytest


def test_validation_error_removes_private_stage(tmp_path: Path) -> None:
    stage = tmp_path / "private-stage"
    destination = tmp_path / "reserved-record"

    def reject(_: Path) -> None:
        raise ValueError("invalid")

    with pytest.raises(ValueError, match="invalid"):
        publisher.publish(b"example\n", stage, destination, reject)

    assert not stage.exists()
    assert not destination.exists()


def test_cleanup_failure_is_surfaced(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
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
