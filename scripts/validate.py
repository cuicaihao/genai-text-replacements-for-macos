#!/usr/bin/env python3
"""Validate the text replacement plist and its README documentation."""

from __future__ import annotations

import plistlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PLIST_PATH = ROOT / "Text Substitutions.plist"
README_PATHS = (ROOT / "README.md", ROOT / "README.zh-CN.md")
EXPECTED_SHORTCUT_COUNT = 50
SHORTCUT_PATTERN = re.compile(r"`(zz[a-z]+)`")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_replacements() -> list[dict[str, object]]:
    try:
        with PLIST_PATH.open("rb") as plist_file:
            replacements = plistlib.load(plist_file)
    except (OSError, plistlib.InvalidFileException) as exc:
        fail(f"could not load {PLIST_PATH.name}: {exc}")

    if not isinstance(replacements, list):
        fail(f"{PLIST_PATH.name} must contain a top-level array")

    return replacements


def validate_replacements(replacements: list[dict[str, object]]) -> set[str]:
    shortcuts: list[str] = []

    for index, replacement in enumerate(replacements):
        if not isinstance(replacement, dict):
            fail(f"entry {index} must be a dictionary")

        if set(replacement) != {"shortcut", "phrase"}:
            fail(f"entry {index} must contain only shortcut and phrase fields")

        shortcut = replacement["shortcut"]
        phrase = replacement["phrase"]

        if not isinstance(shortcut, str) or not shortcut:
            fail(f"entry {index} has an invalid shortcut")
        if not shortcut.startswith("zz"):
            fail(f"shortcut {shortcut!r} must start with 'zz'")
        if not isinstance(phrase, str) or not phrase.strip():
            fail(f"shortcut {shortcut!r} has an empty phrase")

        shortcuts.append(shortcut)

    if len(shortcuts) != EXPECTED_SHORTCUT_COUNT:
        fail(
            f"expected {EXPECTED_SHORTCUT_COUNT} shortcuts, "
            f"found {len(shortcuts)}"
        )

    unique_shortcuts = set(shortcuts)
    if len(unique_shortcuts) != len(shortcuts):
        duplicates = sorted(
            shortcut for shortcut in unique_shortcuts if shortcuts.count(shortcut) > 1
        )
        fail(f"duplicate shortcuts found: {', '.join(duplicates)}")

    return unique_shortcuts


def validate_readme(readme_path: Path, shortcuts: set[str]) -> None:
    try:
        contents = readme_path.read_text(encoding="utf-8")
    except OSError as exc:
        fail(f"could not read {readme_path.name}: {exc}")

    documented_shortcuts = set(SHORTCUT_PATTERN.findall(contents))
    missing = sorted(shortcuts - documented_shortcuts)
    unknown = sorted(documented_shortcuts - shortcuts)

    if missing:
        fail(f"{readme_path.name} is missing shortcuts: {', '.join(missing)}")
    if unknown:
        fail(f"{readme_path.name} lists unknown shortcuts: {', '.join(unknown)}")


def main() -> None:
    replacements = load_replacements()
    shortcuts = validate_replacements(replacements)

    for readme_path in README_PATHS:
        validate_readme(readme_path, shortcuts)

    print(
        f"Validated {len(shortcuts)} unique shortcuts, "
        f"{PLIST_PATH.name}, and {len(README_PATHS)} README files."
    )


if __name__ == "__main__":
    main()
