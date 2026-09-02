from pathlib import Path

import pytest
from transfer import admit


def test_admission_rolls_back_when_manifest_verification_fails(
    tmp_path: Path,
) -> None:
    source = tmp_path / "checkout" / "README.md"
    source.parent.mkdir()
    source.write_text("example\n", encoding="utf-8")

    with pytest.raises(ValueError, match="did not verify"):
        admit(
            source,
            tmp_path / "records",
            tmp_path / "manifest.txt",
            lambda _: False,
        )

    assert source.read_text(encoding="utf-8") == "example\n"
    assert not (tmp_path / "records").exists() or not any(
        (tmp_path / "records").iterdir()
    )
