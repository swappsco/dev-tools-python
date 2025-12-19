# Dev Tools Hooks

Git hooks for development workflow automation.

## Features

- **commit-msg**: Validates commit messages follow [Conventional Commits](https://www.conventionalcommits.org/) format
- **pre-commit**: Runs custom commands (lint, type check, format) from config file
- **pre-push**: Validates branch naming + runs custom commands (tests) from config file
- **Django Smart Tests**: Run tests only for modified apps/modules instead of all tests
- **Test Detection**: Warns about modified files without corresponding tests
- **File filtering**: Only run commands when specific file types are changed
- **Tag Support**: Allows pushing git tags without validation

## Installation

```bash
pip install git+https://github.com/swapps/dev-tools-hooks.git
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
- `docs: update README`

### pre-commit

Runs custom commands defined in `.dev-hooks.yml` before each commit:
- Lint checks
- Type checking
- Format validation
- **Django test detection**: Warns if modified Python files don't have corresponding tests (configurable)

### pre-push

1. **Tag support** - Allows pushing git tags without any validation

2. **Branch validation** - Validates branch names follow one of these formats:
   - ClickUp ID: `CU-xxxxxxxxx`
   - Conventional: `<type>/<description>` (e.g., `feat/user-login`, `fix/header-bug`)
   - Special branches: `master`, `main`, `develop`, `staging`, `production`

3. **Django Smart Tests** - Runs tests only for modified apps/modules (configurable)

4. **Custom commands** - Runs commands defined in `.dev-hooks.yml` (tests, build, etc.)

## Configuration File

Create a `.dev-hooks.yml` file in your project root to configure custom commands.

Copy the example file to get started:

```bash
cp .dev-hooks.example.yml .dev-hooks.yml
```

### Example Configuration

```yaml
# Pre-commit commands (run on every commit)
pre-commit:
  enabled: true
  only_for_files: "*.py"  # Only run if .py files are staged
  commands:
    - name: "Lint Check"
      run: "ruff check src/"
    - name: "Type Check"
      run: "mypy src/"

# Pre-push commands (run before push)
pre-push:
  enabled: true
  skip_branch_validation: false
  only_for_files: "*.py"  # Only run tests if .py files changed
  commands:
    - name: "Run Tests"
      run: "pytest"

# Docker support (optional)
docker:
  enabled: false
  compose: true
  container: "app"
  compose_file: "docker-compose.yml"
```

### File Filtering

Use `only_for_files` to run commands only when specific file types are changed:

```yaml
pre-commit:
  only_for_files: "*.py"           # Single pattern

pre-push:
  only_for_files: "*.py, *.js"     # Multiple patterns (comma-separated)
```

If no matching files are found, commands are skipped with a message:
```
Skipping pre-push commands (no matching files: *.py)
```

### Django Smart Tests

For Django/Python projects, enable smart test features:

```yaml
pre-commit:
  # Warn about modified files without tests (default: true)
  django_check_tests: true

pre-push:
  # Run tests only for modified apps (default: true)
  django_smart_tests: true
  # Test command (default: "pytest")
  django_test_command: "pytest"
```

**How it works:**

1. **pre-commit**: Analyzes staged Python files and warns if they don't have corresponding test files (e.g., `test_<filename>.py`). This is just a warning and won't block the commit.

2. **pre-push**: Detects which Django apps/modules were modified and runs tests only for those apps instead of the entire test suite:
   ```bash
   # Instead of: pytest
   # Runs: pytest app1 app2
   ```

Example output:
```
┌──────────────────────────────────────────────────────────────┐
│  Running Django Smart Tests...                               │
└──────────────────────────────────────────────────────────────┘

Modified apps: users api payments

▶ Smart Tests
  pytest users api payments
  ✔ Passed
```

### Docker Support

For dockerized projects, enable docker execution:

```yaml
docker:
  enabled: true
  compose: true
  container: "app"

pre-commit:
  commands:
    - name: "Lint"
      run: "npm run lint"

pre-push:
  commands:
    - name: "Tests"
      run: "npm test"
```

Commands will be executed inside the container:
```bash
docker-compose exec -T app npm run lint
```

## Development

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install in development mode
pip install -e .

# Run the CLI
dev-hooks --help
```

## License

MIT - Copyright (c) 2025 Swapps
