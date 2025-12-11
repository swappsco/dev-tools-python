"""
Dev Tools Hooks - Git hooks for development workflow.

This package provides git hooks for:
- Conventional Commits validation (commit-msg)
- PHPCS code quality checks for Drupal/WordPress (pre-commit)
- Branch naming conventions (pre-push)
"""

__version__ = "1.0.0"
__author__ = "Swapps"

from .installer import install_hooks, uninstall_hooks

__all__ = ["install_hooks", "uninstall_hooks", "__version__"]
