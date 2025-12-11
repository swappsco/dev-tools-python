"""
Command-line interface for dev-tools-hooks.

Usage:
    dev-hooks install [--force] [--hooks HOOKS]
    dev-hooks uninstall [--hooks HOOKS]
    dev-hooks list
    dev-hooks --help
"""

import argparse
import sys
from typing import List, Optional

from . import __version__
from .installer import (
    AVAILABLE_HOOKS,
    install_hooks,
    uninstall_hooks,
    list_installed_hooks,
)

# ANSI colors
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[0;34m"
CYAN = "\033[0;36m"
BOLD = "\033[1m"
NC = "\033[0m"  # No Color


def print_banner():
    """Print the tool banner."""
    print(f"{BLUE}{'='*60}{NC}")
    print(f"{BOLD}  Dev Tools Hooks v{__version__}{NC}")
    print(f"{BLUE}{'='*60}{NC}")
    print()


def cmd_install(args: argparse.Namespace) -> int:
    """Handle the install command."""
    print_banner()

    hooks = args.hooks.split(",") if args.hooks else None

    try:
        installed, skipped, errors = install_hooks(
            repo_path=args.path,
            hooks=hooks,
            force=args.force
        )
    except RuntimeError as e:
        print(f"{RED}Error: {e}{NC}")
        return 1

    if installed:
        print(f"{GREEN}Installed hooks:{NC}")
        for hook in installed:
            print(f"  {GREEN}+{NC} {hook}")
        print()

    if skipped:
        print(f"{YELLOW}Skipped (already exist, use --force to overwrite):{NC}")
        for hook in skipped:
            print(f"  {YELLOW}-{NC} {hook}")
        print()

    if errors:
        print(f"{RED}Errors:{NC}")
        for error in errors:
            print(f"  {RED}!{NC} {error}")
        print()

    if installed:
        print(f"{GREEN}Git hooks installed successfully!{NC}")
    elif not errors:
        print(f"{YELLOW}No hooks were installed.{NC}")

    return 1 if errors else 0


def cmd_uninstall(args: argparse.Namespace) -> int:
    """Handle the uninstall command."""
    print_banner()

    hooks = args.hooks.split(",") if args.hooks else None

    try:
        removed, not_found = uninstall_hooks(
            repo_path=args.path,
            hooks=hooks
        )
    except RuntimeError as e:
        print(f"{RED}Error: {e}{NC}")
        return 1

    if removed:
        print(f"{GREEN}Removed hooks:{NC}")
        for hook in removed:
            print(f"  {GREEN}-{NC} {hook}")
        print()

    if not_found:
        print(f"{YELLOW}Not found:{NC}")
        for hook in not_found:
            print(f"  {YELLOW}?{NC} {hook}")
        print()

    if removed:
        print(f"{GREEN}Git hooks uninstalled successfully!{NC}")

    return 0


def cmd_list(args: argparse.Namespace) -> int:
    """Handle the list command."""
    print_banner()

    try:
        installed = list_installed_hooks(repo_path=args.path)
    except Exception:
        installed = []

    print(f"{CYAN}Available hooks:{NC}")
    for hook in AVAILABLE_HOOKS:
        if hook in installed:
            print(f"  {GREEN}[x]{NC} {hook}")
        else:
            print(f"  {YELLOW}[ ]{NC} {hook}")

    print()
    print(f"{CYAN}Hook descriptions:{NC}")
    print(f"  {BOLD}commit-msg{NC}   - Validates Conventional Commits format")
    print(f"  {BOLD}pre-commit{NC}   - Runs PHPCS for Drupal/WordPress projects")
    print(f"  {BOLD}pre-push{NC}     - Validates branch naming conventions")

    return 0


def main(argv: Optional[List[str]] = None) -> int:
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        prog="dev-hooks",
        description="Git hooks for development workflow",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  dev-hooks install              Install all hooks
  dev-hooks install --force      Overwrite existing hooks
  dev-hooks install --hooks commit-msg,pre-push
  dev-hooks uninstall            Remove all hooks
  dev-hooks list                 Show hook status
        """
    )

    parser.add_argument(
        "-V", "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )

    parser.add_argument(
        "-p", "--path",
        help="Path to the git repository (default: current directory)",
        default=None
    )

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Install command
    install_parser = subparsers.add_parser(
        "install",
        help="Install git hooks"
    )
    install_parser.add_argument(
        "-f", "--force",
        action="store_true",
        help="Overwrite existing hooks"
    )
    install_parser.add_argument(
        "--hooks",
        help=f"Comma-separated list of hooks to install (available: {', '.join(AVAILABLE_HOOKS)})"
    )

    # Uninstall command
    uninstall_parser = subparsers.add_parser(
        "uninstall",
        help="Uninstall git hooks"
    )
    uninstall_parser.add_argument(
        "--hooks",
        help="Comma-separated list of hooks to uninstall"
    )

    # List command
    subparsers.add_parser(
        "list",
        help="List available and installed hooks"
    )

    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    if args.command == "install":
        return cmd_install(args)
    elif args.command == "uninstall":
        return cmd_uninstall(args)
    elif args.command == "list":
        return cmd_list(args)

    return 0


if __name__ == "__main__":
    sys.exit(main())
