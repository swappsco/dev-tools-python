# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
