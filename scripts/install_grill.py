#!/usr/bin/env python3
"""Install the Grill skills required by PraxFlow into ~/.agents/skills.

This script intentionally installs from the upstream mattpocock/skills repository
instead of vendoring third-party skill content into PraxFlow.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


UPSTREAM = "https://github.com/mattpocock/skills.git"
SKILLS = {
    "grill-me": Path("skills/productivity/grill-me"),
    "grilling": Path("skills/productivity/grilling"),
    "grill-with-docs": Path("skills/engineering/grill-with-docs"),
    "domain-modeling": Path("skills/engineering/domain-modeling"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install PraxFlow's required Grill skills into ~/.agents/skills"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace existing Grill skill directories at the destination.",
    )
    parser.add_argument(
        "--destination",
        default="~/.agents/skills",
        help="Destination skill root (default: ~/.agents/skills).",
    )
    return parser.parse_args()


def copy_skill(src: Path, dst: Path, force: bool) -> None:
    if not (src / "SKILL.md").is_file():
        raise RuntimeError(f"Upstream skill is missing SKILL.md: {src}")

    if dst.exists() or dst.is_symlink():
        if not force:
            raise FileExistsError(
                f"Destination already exists: {dst}. Re-run with --force to replace it."
            )
        if dst.is_symlink() or dst.is_file():
            dst.unlink()
        else:
            shutil.rmtree(dst)

    shutil.copytree(src, dst)


def main() -> int:
    args = parse_args()
    destination = Path(args.destination).expanduser().resolve()
    destination.mkdir(parents=True, exist_ok=True)

    if shutil.which("git") is None:
        print("git is required but was not found in PATH.", file=sys.stderr)
        return 1

    with tempfile.TemporaryDirectory(prefix="praxflow-grill-") as temp_dir:
        checkout = Path(temp_dir) / "skills"
        try:
            subprocess.run(
                ["git", "clone", "--depth", "1", UPSTREAM, str(checkout)],
                check=True,
            )
        except subprocess.CalledProcessError as exc:
            print(f"Failed to clone {UPSTREAM}: {exc}", file=sys.stderr)
            return 1

        installed: list[str] = []
        for name, relative in SKILLS.items():
            src = checkout / relative
            dst = destination / name
            try:
                copy_skill(src, dst, args.force)
            except Exception as exc:  # noqa: BLE001 - CLI needs readable errors.
                print(f"Failed to install {name}: {exc}", file=sys.stderr)
                return 1
            installed.append(name)
            print(f"installed {name} -> {dst}")

    print()
    print(f"Grill skills installed in: {destination}")
    print(f"Skills installed: {len(installed)}")
    print("Codex and DeepSeek Harness can share this same Agent Skills directory.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
