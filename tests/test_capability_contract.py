from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CAPABILITY = ROOT / "capabilities/provenance-realism-review"


def _frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    assert lines[0] == "---", f"{path} must begin with YAML frontmatter"
    try:
        closing = lines.index("---", 1)
    except ValueError as error:
        raise AssertionError(f"{path} has no closing frontmatter delimiter") from error
    metadata = yaml.safe_load("\n".join(lines[1:closing]))
    assert isinstance(metadata, dict)
    return metadata


def test_skill_identity_matches_its_directory_and_metadata() -> None:
    metadata = _frontmatter(CAPABILITY / "SKILL.md")
    assert metadata["name"] == CAPABILITY.name
    description = metadata["description"]
    assert isinstance(description, str)
    assert description.strip() and len(description) <= 1024

    agent_metadata = yaml.safe_load(
        (CAPABILITY / "agents/openai.yaml").read_text(encoding="utf-8")
    )
    default_prompt = agent_metadata["interface"]["default_prompt"]
    assert f"${CAPABILITY.name}" in default_prompt


def test_skill_references_are_local_and_present() -> None:
    skill = (CAPABILITY / "SKILL.md").read_text(encoding="utf-8")
    references = {
        "claim-lineage.md",
        "failure-semantics.md",
        "finding-standard.md",
    }
    for reference in references:
        assert f"references/{reference}" in skill
        assert (CAPABILITY / "references" / reference).is_file()


def test_only_one_canonical_skill_copy_exists() -> None:
    skill_paths = sorted(
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("SKILL.md")
        if ".venv" not in path.parts
    )
    assert skill_paths == ["capabilities/provenance-realism-review/SKILL.md"]
