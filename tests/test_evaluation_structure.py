from __future__ import annotations

from pathlib import Path

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = ROOT / "evals/scenarios"
EXPECTATIONS = ROOT / "evals/expectations"


def _headings(path: Path) -> set[str]:
    tokens = MarkdownIt("commonmark").parse(path.read_text(encoding="utf-8"))
    headings: set[str] = set()
    for index, token in enumerate(tokens):
        if token.type == "heading_open" and tokens[index + 1].type == "inline":
            headings.add(tokens[index + 1].content)
    return headings


def test_each_scenario_has_separate_held_out_expectations() -> None:
    scenarios = sorted(path for path in SCENARIOS.iterdir() if path.is_dir())
    assert len(scenarios) >= 2
    for scenario in scenarios:
        assert (scenario / "prompt.md").is_file()
        fixture = scenario / "fixture"
        assert fixture.is_dir()
        assert any(fixture.iterdir())

        expectation = EXPECTATIONS / f"{scenario.name}.md"
        assert expectation.is_file()
        assert not expectation.resolve().is_relative_to(scenario.resolve())
        assert {
            "Required review behavior",
            "Forbidden assertions",
        } <= _headings(expectation)


def test_agent_visible_scenarios_do_not_embed_scorecard_language() -> None:
    forbidden = (
        "expected disposition:",
        "required review behavior",
        "forbidden assertions",
    )
    for path in SCENARIOS.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".py"}:
            continue
        text = path.read_text(encoding="utf-8").lower()
        assert not any(marker in text for marker in forbidden), path


def test_pair_contains_finding_and_no_finding_controls() -> None:
    dispositions = {
        path.stem: next(
            line for line in path.read_text(encoding="utf-8").splitlines()
            if line.startswith("Expected disposition:")
        )
        for path in EXPECTATIONS.glob("*.md")
    }
    assert any(
        "at least one material finding" in value
        for value in dispositions.values()
    )
    assert any("no material findings" in value for value in dispositions.values())
