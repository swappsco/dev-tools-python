"""
Hook installer module.

Provides functions to install and uninstall git hooks in a repository.
"""

import os
import shutil
import stat
import subprocess
from pathlib import Path
from typing import Optional, List, Tuple

# Available hooks in this package
AVAILABLE_HOOKS = ["commit-msg", "pre-commit", "pre-push"]


def get_hooks_source_dir() -> Path:
    """Get the directory containing the hook templates."""
    return Path(__file__).parent / "hooks"


def get_git_hooks_dir(repo_path: Optional[str] = None) -> Optional[Path]:
    """
    Get the .git/hooks directory for a repository.

    Args:
        repo_path: Path to the repository. If None, uses current directory.

    Returns:
        Path to the hooks directory, or None if not a git repository.
    """
    if repo_path is None:
        repo_path = os.getcwd()

    try:
        result = subprocess.run(
            ["git", "rev-parse", "--git-dir"],
            cwd=repo_path,
            capture_output=True,
            text=True,
            check=True
        )
        git_dir = result.stdout.strip()
        if not os.path.isabs(git_dir):
            git_dir = os.path.join(repo_path, git_dir)
        return Path(git_dir) / "hooks"
    except subprocess.CalledProcessError:
        return None


def install_hooks(
    repo_path: Optional[str] = None,
    hooks: Optional[List[str]] = None,
    force: bool = False
) -> Tuple[List[str], List[str], List[str]]:
    """
    Install git hooks in a repository.

    Args:
        repo_path: Path to the repository. If None, uses current directory.
        hooks: List of hooks to install. If None, installs all available hooks.
        force: If True, overwrite existing hooks.

    Returns:
        Tuple of (installed, skipped, errors) hook names.
    """
    hooks_dir = get_git_hooks_dir(repo_path)
    if hooks_dir is None:
        raise RuntimeError("Not a git repository")

    # Create hooks directory if it doesn't exist
    hooks_dir.mkdir(parents=True, exist_ok=True)

    source_dir = get_hooks_source_dir()
    hooks_to_install = hooks if hooks else AVAILABLE_HOOKS

    installed = []
    skipped = []
    errors = []

    for hook_name in hooks_to_install:
        if hook_name not in AVAILABLE_HOOKS:
            errors.append(f"{hook_name} (unknown hook)")
            continue

        source_file = source_dir / hook_name
        dest_file = hooks_dir / hook_name

        if not source_file.exists():
            errors.append(f"{hook_name} (source not found)")
            continue

        # Check if hook already exists
        if dest_file.exists() and not force:
            skipped.append(hook_name)
            continue

        try:
            # Copy the hook file
            shutil.copy2(source_file, dest_file)

            # Make it executable
            dest_file.chmod(dest_file.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

            installed.append(hook_name)
        except Exception as e:
            errors.append(f"{hook_name} ({str(e)})")

    return installed, skipped, errors


def uninstall_hooks(
    repo_path: Optional[str] = None,
    hooks: Optional[List[str]] = None
) -> Tuple[List[str], List[str]]:
    """
    Uninstall git hooks from a repository.

    Args:
        repo_path: Path to the repository. If None, uses current directory.
        hooks: List of hooks to uninstall. If None, uninstalls all available hooks.

    Returns:
        Tuple of (removed, not_found) hook names.
    """
    hooks_dir = get_git_hooks_dir(repo_path)
    if hooks_dir is None:
        raise RuntimeError("Not a git repository")

    hooks_to_remove = hooks if hooks else AVAILABLE_HOOKS

    removed = []
    not_found = []

    for hook_name in hooks_to_remove:
        hook_file = hooks_dir / hook_name

        if hook_file.exists():
            hook_file.unlink()
            removed.append(hook_name)
        else:
            not_found.append(hook_name)

    return removed, not_found


def list_installed_hooks(repo_path: Optional[str] = None) -> List[str]:
    """
    List installed hooks in a repository.

    Args:
        repo_path: Path to the repository. If None, uses current directory.

    Returns:
        List of installed hook names from this package.
    """
    hooks_dir = get_git_hooks_dir(repo_path)
    if hooks_dir is None:
        return []

    installed = []
    for hook_name in AVAILABLE_HOOKS:
        if (hooks_dir / hook_name).exists():
            installed.append(hook_name)

    return installed
