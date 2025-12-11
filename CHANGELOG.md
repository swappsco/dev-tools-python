# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-12-10

### Added
- Initial release
- `commit-msg` hook for Conventional Commits validation
- `pre-commit` hook for PHPCS code quality (Drupal/WordPress)
- `pre-push` hook for branch naming conventions
- CLI commands: `install`, `uninstall`, `list`
- Support for selective hook installation
- Force overwrite option for existing hooks
