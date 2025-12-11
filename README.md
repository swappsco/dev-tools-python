# Dev Tools Hooks

Git hooks for development workflow automation.

## Features

- **commit-msg**: Validates commit messages follow [Conventional Commits](https://www.conventionalcommits.org/) format (with optional ClickUp ID)
- **pre-commit**: Runs custom commands (lint, type check, format) from config file
- **pre-push**: Validates branch naming + runs custom commands (tests) from config file

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
CU-xxxxxxxxx - <type>(<optional-scope>): <description>
```

Valid types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`

Examples:
- `feat: add user authentication`
- `fix(api): resolve timeout issue`
- `CU-86b7kybxx - feat: add git hooks`
- `CU-86b7kybxx - fix(auth): resolve login bug`

### pre-commit

Runs custom commands defined in `.dev-hooks.yml` before each commit:
- Lint checks
- Type checking
- Format validation

### pre-push

1. **Branch validation** - Validates branch names follow one of these formats:
   - ClickUp ID: `CU-xxxxxxxxx`
   - Conventional: `<type>/<description>` (e.g., `feat/user-login`, `fix/header-bug`)
   - Special branches: `master`, `main`, `develop`, `staging`, `production`

2. **Custom commands** - Runs commands defined in `.dev-hooks.yml` (tests, build, etc.)

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
  commands:
    - name: "Lint Check"
      run: "ruff check src/"
    - name: "Type Check"
      run: "mypy src/"

# Pre-push commands (run before push)
pre-push:
  enabled: true
  skip_branch_validation: false
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
