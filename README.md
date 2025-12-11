# Dev Tools Hooks

Git hooks for development workflow automation.

## Features

- **commit-msg**: Validates commit messages follow [Conventional Commits](https://www.conventionalcommits.org/) format
- **pre-commit**: Runs PHPCS code quality checks for Drupal and WordPress projects
- **pre-push**: Validates branch naming conventions (ClickUp IDs or conventional format)

## Installation

```bash
pip install dev-tools-hooks
```

Or install from source:

```bash
pip install -e .
```

## Usage

### Install hooks in your repository

```bash
# Navigate to your git repository
cd /path/to/your/repo

# Install all hooks
dev-hooks install

# Install specific hooks only
dev-hooks install --hooks commit-msg,pre-push

# Force overwrite existing hooks
dev-hooks install --force
```

### Uninstall hooks

```bash
# Remove all hooks
dev-hooks uninstall

# Remove specific hooks
dev-hooks uninstall --hooks commit-msg
```

### List hooks status

```bash
dev-hooks list
```

## Hook Details

### commit-msg

Validates that commit messages follow Conventional Commits format:

```
<type>(<optional-scope>): <description>
```

Valid types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`

Examples:
- `feat: add user authentication`
- `fix(api): resolve timeout issue`
- `docs: update installation guide`

### pre-commit

For PHP projects (Drupal/WordPress), automatically:
- Detects project type from `config.yml`
- Installs PHPCS and coding standards if needed
- Validates staged PHP files against coding standards

### pre-push

Validates branch names follow one of these formats:
- ClickUp ID: `CU-xxxxxxxxx` (9 alphanumeric characters)
- Conventional: `<type>/<description>` (e.g., `feat/user-login`, `fix/header-bug`)
- Special branches: `master`, `main`, `develop`, `staging`, `production`

## Development

```bash
# Install in development mode
pip install -e .

# Run the CLI
dev-hooks --help
```

## License

MIT
