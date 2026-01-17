#!/usr/bin/env python3
"""Validate a machine template for completeness and correctness."""

import argparse
import json
import re
import sys
from pathlib import Path


class ValidationError:
    """Represents a validation error."""

    def __init__(self, level: str, message: str, file: str | None = None):
        self.level = level  # "error" or "warning"
        self.message = message
        self.file = file

    def __str__(self):
        icon = "\u274c" if self.level == "error" else "\u26a0\ufe0f"
        if self.file:
            return f"{icon} [{self.file}] {self.message}"
        return f"{icon} {self.message}"


def validate_machine_name(name: str) -> list[ValidationError]:
    """Validate machine name follows conventions."""
    errors = []

    if not name:
        errors.append(ValidationError("error", "Machine name is empty"))
        return errors

    if name != name.lower():
        errors.append(ValidationError(
            "error",
            f"Machine name must be lowercase: '{name}' -> '{name.lower()}'"
        ))

    if " " in name:
        errors.append(ValidationError(
            "error",
            "Machine name cannot contain spaces, use hyphens instead"
        ))

    if "_" in name:
        errors.append(ValidationError(
            "warning",
            "Machine name uses underscores, prefer hyphens for consistency"
        ))

    if not name[0].isalpha():
        errors.append(ValidationError(
            "error",
            "Machine name must start with a letter"
        ))

    return errors


def validate_json_file(file_path: Path, required_keys: list[str] = None) -> list[ValidationError]:
    """Validate a JSON file exists and is valid."""
    errors = []
    filename = file_path.name

    if not file_path.exists():
        errors.append(ValidationError("error", f"Required file missing: {filename}"))
        return errors

    try:
        with open(file_path) as f:
            data = json.load(f)

        if required_keys:
            for key in required_keys:
                if key not in data:
                    errors.append(ValidationError(
                        "warning",
                        f"Missing recommended key: '{key}'",
                        filename
                    ))

    except json.JSONDecodeError as e:
        errors.append(ValidationError("error", f"Invalid JSON: {e}", filename))

    return errors


def validate_claude_md(file_path: Path) -> list[ValidationError]:
    """Validate CLAUDE.md file content."""
    errors = []
    filename = file_path.name

    if not file_path.exists():
        errors.append(ValidationError("error", f"Required file missing: {filename}"))
        return errors

    content = file_path.read_text()

    # Check for workspace section
    if "workspace" not in content.lower():
        errors.append(ValidationError(
            "warning",
            "Missing 'Workspace' section - machines should document the workspace path",
            filename
        ))

    # Check for heading
    if not content.strip().startswith("#"):
        errors.append(ValidationError(
            "warning",
            "CLAUDE.md should start with a heading",
            filename
        ))

    # Check for TODO markers (indicate incomplete setup)
    todo_count = len(re.findall(r"<!--\s*TODO:", content, re.IGNORECASE))
    todo_count += len(re.findall(r"\bTODO\b", content))
    if todo_count > 0:
        errors.append(ValidationError(
            "warning",
            f"Contains {todo_count} TODO marker(s) - remember to complete these",
            filename
        ))

    # Check minimum content length
    if len(content.strip()) < 100:
        errors.append(ValidationError(
            "warning",
            "CLAUDE.md seems too short - consider adding more detail",
            filename
        ))

    return errors


def validate_readme(file_path: Path) -> list[ValidationError]:
    """Validate README.md file."""
    errors = []

    if not file_path.exists():
        errors.append(ValidationError(
            "warning",
            "Missing README.md - recommended for documentation"
        ))
        return errors

    content = file_path.read_text()

    if len(content.strip()) < 50:
        errors.append(ValidationError(
            "warning",
            "README.md seems too short",
            "README.md"
        ))

    return errors


def validate_settings(file_path: Path) -> list[ValidationError]:
    """Validate .claude/settings.json file."""
    errors = validate_json_file(file_path, required_keys=["permissions"])

    if file_path.exists():
        try:
            with open(file_path) as f:
                data = json.load(f)

            permissions = data.get("permissions", {})
            if "defaultMode" not in permissions and "allow" not in permissions:
                errors.append(ValidationError(
                    "warning",
                    "No permission mode configured - consider setting defaultMode or allow list",
                    file_path.name
                ))
        except (json.JSONDecodeError, KeyError):
            pass  # Already reported by validate_json_file

    return errors


def validate_mcp(file_path: Path) -> list[ValidationError]:
    """Validate .mcp.json file."""
    return validate_json_file(file_path, required_keys=["mcpServers"])


def validate_self_update_skill(machine_path: Path) -> list[ValidationError]:
    """Validate the self-update skill is present."""
    errors = []
    skill_path = machine_path / ".claude" / "skills" / "self-update" / "SKILL.md"

    if not skill_path.exists():
        errors.append(ValidationError(
            "warning",
            "Missing self-update skill - machines should include .claude/skills/self-update/SKILL.md"
        ))
    elif skill_path.stat().st_size < 100:
        errors.append(ValidationError(
            "warning",
            "Self-update skill seems too short",
            ".claude/skills/self-update/SKILL.md"
        ))

    return errors


def validate_machine(machine_path: Path) -> tuple[list[ValidationError], list[ValidationError]]:
    """Validate a complete machine template.

    Returns:
        Tuple of (errors, warnings)
    """
    all_errors = []

    # Validate machine name
    all_errors.extend(validate_machine_name(machine_path.name))

    # Validate required files
    all_errors.extend(validate_claude_md(machine_path / "CLAUDE.md"))
    all_errors.extend(validate_settings(machine_path / ".claude" / "settings.json"))
    all_errors.extend(validate_mcp(machine_path / ".mcp.json"))

    # Validate optional files
    all_errors.extend(validate_readme(machine_path / "README.md"))

    # Validate self-update skill
    all_errors.extend(validate_self_update_skill(machine_path))

    # Check .claude directory exists
    if not (machine_path / ".claude").is_dir():
        all_errors.append(ValidationError(
            "error",
            "Missing .claude/ directory"
        ))

    # Separate errors and warnings
    errors = [e for e in all_errors if e.level == "error"]
    warnings = [e for e in all_errors if e.level == "warning"]

    return errors, warnings


def main():
    parser = argparse.ArgumentParser(
        description="Validate a machine template for completeness",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s machines/my-machine
  %(prog)s machines/code-reviewer --strict
        """
    )
    parser.add_argument(
        "path",
        type=Path,
        help="Path to the machine directory"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors"
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Only output errors, not warnings"
    )

    args = parser.parse_args()

    machine_path = args.path.resolve()

    if not machine_path.exists():
        print(f"\u274c Machine directory not found: {machine_path}")
        sys.exit(1)

    if not machine_path.is_dir():
        print(f"\u274c Path is not a directory: {machine_path}")
        sys.exit(1)

    print(f"\ud83d\udd0d Validating machine: {machine_path.name}\n")

    errors, warnings = validate_machine(machine_path)

    # Print errors
    if errors:
        print("Errors:")
        for error in errors:
            print(f"  {error}")
        print()

    # Print warnings
    if warnings and not args.quiet:
        print("Warnings:")
        for warning in warnings:
            print(f"  {warning}")
        print()

    # Summary
    error_count = len(errors)
    warning_count = len(warnings)

    if args.strict:
        error_count += warning_count

    if error_count == 0 and warning_count == 0:
        print("\u2705 Machine template is valid!")
        sys.exit(0)
    elif error_count == 0:
        print(f"\u2705 Machine template is valid with {warning_count} warning(s)")
        sys.exit(0)
    else:
        print(f"\u274c Validation failed: {error_count} error(s), {warning_count} warning(s)")
        sys.exit(1)


if __name__ == "__main__":
    main()
