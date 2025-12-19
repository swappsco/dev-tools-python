# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-12-19

### Added
- **Django Smart Tests**: Automatically run tests only for modified Django apps/modules instead of the entire test suite
  - `pre-push.django_smart_tests`: Enable/disable smart test detection (default: true)
  - `pre-push.django_test_command`: Configure test command (default: "pytest")
- **Django Test Detection**: Warn about modified Python files without corresponding tests
  - `pre-commit.django_check_tests`: Enable/disable test detection warnings (default: true)
  - Shows warning message but doesn't block the commit
- **Tag Push Support**: Allow pushing git tags without branch validation in pre-push hook
- **Detached HEAD Support**: Allow push operations when in detached HEAD state

### Changed
- ClickUp ID pattern in commit-msg is now disabled by default (kept commented for future use)
- Simplified commit message format examples (removed ClickUp references from error messages)

## [1.0.0] - 2025-12-11

### Added
- Initial release
- `commit-msg` hook for Conventional Commits validation (with ClickUp ID support)
- `pre-commit` hook for custom commands (lint, type check, format)
- `pre-push` hook for branch naming validation and custom commands (tests)
- CLI commands: `install`, `uninstall`, `list`
- Support for selective hook installation
- Force overwrite option for existing hooks
- Docker support for running commands in containers
- File filtering with `only_for_files` option
