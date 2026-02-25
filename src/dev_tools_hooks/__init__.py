"""
Dev Tools Hooks - Git hooks for development workflow.

This package provides git hooks for:
- Conventional Commits validation (commit-msg)
- Custom commands for lint, type check, format (pre-commit)
- Branch naming validation and custom commands (pre-push)
"""

__version__ = "1.2.0"
__author__ = "Swapps"

from .installer import install_hooks, uninstall_hooks

__all__ = ["install_hooks", "uninstall_hooks", "__version__"]
