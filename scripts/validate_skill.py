#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "dosen-pembimbing-skripsi-ta"
REFERENCE_FILES = [
    "academic-writing.md",
    "research-methodology.md",
    "literature-review.md",
    "data-analysis.md",
    "scientific-discussion.md",
    "critical-thinking.md",
    "source-verification.md",
    "citation-management.md",
    "thesis-consistency.md",
    "quality-control.md",
]
REQUIRED_TERMS = [
    "Anti-halusinasi",
    "Konfirmasi",
    "Data mentah",
    "Sumber belum ditemukan",
]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_frontmatter(text: str, errors: list[str]) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail(errors, "SKILL.md harus diawali YAML frontmatter.")
        return {}

    parts = text.split("---", 2)
    if len(parts) < 3:
        fail(errors, "YAML frontmatter SKILL.md tidak ditutup.")
        return {}

    frontmatter = parts[1].strip()
    fields: dict[str, str] = {}
    current_key: str | None = None
    for line in frontmatter.splitlines():
        if re.match(r"^[A-Za-z][A-Za-z0-9_-]*:", line):
            key, value = line.split(":", 1)
            current_key = key.strip()
            fields[current_key] = value.strip().strip('"').strip("'")
        elif current_key and line.strip():
            fields[current_key] += " " + line.strip().strip('"').strip("'")
    return fields


def validate() -> list[str]:
    errors: list[str] = []
    skill_file = ROOT / "SKILL.md"
    is_distribution = (ROOT / "LICENSE").is_file() and not (ROOT / "adapters").exists()
    if not skill_file.is_file():
        fail(errors, "SKILL.md tidak ditemukan.")
        return errors

    text = skill_file.read_text(encoding="utf-8")
    fields = parse_frontmatter(text, errors)
    name = fields.get("name", "")
    if name != SKILL_NAME:
        fail(errors, f"Metadata name harus '{SKILL_NAME}', ditemukan '{name}'.")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        fail(errors, "Metadata name tidak mengikuti format Agent Skills.")
    description = fields.get("description", "")
    if not description or len(description) > 1024:
        fail(errors, "Metadata description harus ada dan maksimal 1024 karakter.")

    for required in REQUIRED_TERMS:
        if required not in text:
            fail(errors, f"Aturan wajib tidak ditemukan di SKILL.md: {required}")

    for filename in REFERENCE_FILES:
        path = ROOT / "references" / filename
        if not path.is_file():
            fail(errors, f"File referensi wajib tidak ditemukan: references/{filename}")

    if not is_distribution:
        for adapter in ("claude", "gemini", "chatgpt", "github-copilot", "generic"):
            path = ROOT / "adapters" / adapter / "README.md"
            if not path.is_file():
                fail(errors, f"Adapter tidak ditemukan: adapters/{adapter}/README.md")

    for md_file in ROOT.rglob("*.md"):
        if ".git" in md_file.parts:
            continue
        content = md_file.read_text(encoding="utf-8")
        for match in re.finditer(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)", content):
            target = match.group(1)
            if "://" in target or target.startswith("mailto:"):
                continue
            resolved = (md_file.parent / target).resolve()
            if not resolved.exists():
                fail(errors, f"Tautan internal rusak: {md_file.relative_to(ROOT)} -> {target}")
    return errors


def package_skill(destination: Path) -> None:
    destination = destination.resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for filename in ["SKILL.md"] + [f"references/{name}" for name in REFERENCE_FILES]:
            archive.write(ROOT / filename, Path(SKILL_NAME) / filename)
        archive.write(ROOT / "LICENSE", Path(SKILL_NAME) / "LICENSE")
        archive.write(ROOT / "scripts" / "validate_skill.py",
                      Path(SKILL_NAME) / "scripts" / "validate_skill.py")
    print(f"Paket dibuat: {destination}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validasi dan paketkan skill skripsi.")
    parser.add_argument("--package", type=Path, help="Path ZIP paket distribusi.")
    args = parser.parse_args()

    errors = validate()
    if errors:
        print("Validasi gagal:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validasi berhasil:")
    print("- metadata SKILL.md valid")
    print("- file referensi wajib tersedia")
    if (ROOT / "adapters").exists():
        print("- adapter wajib tersedia")
    else:
        print("- paket distribusi tidak menyertakan adapter repository")
    print("- tautan internal tidak rusak")

    if args.package:
        package_skill(args.package)
    return 0


if __name__ == "__main__":
    sys.exit(main())
