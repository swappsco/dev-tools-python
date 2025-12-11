# Dev Tools Hooks

Git hooks for development workflow automation.

## Features

- **commit-msg**: Validates commit messages follow [Conventional Commits](https://www.conventionalcommits.org/) format (with optional ClickUp ID)
- **pre-commit**: Runs PHPCS code quality checks for Drupal and WordPress projects
- **pre-push**: Validates branch naming + runs custom commands from config file

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
CU-xxxxxxxxx - <type>(<optional-scope>): <description>
```

Valid types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`

Examples:
- `feat: add user authentication`
- `fix(api): resolve timeout issue`
- `CU-86b7kybxx - feat: add git hooks`
- `CU-86b7kybxx - fix(auth): resolve login bug`

### pre-commit

For PHP projects (Drupal/WordPress), automatically:
- Detects project type from `config.yml`
- Installs PHPCS and coding standards if needed
- Validates staged PHP files against coding standards

### pre-push

1. **Branch validation** - Validates branch names follow one of these formats:
   - ClickUp ID: `CU-xxxxxxxxx`
   - Conventional: `<type>/<description>` (e.g., `feat/user-login`, `fix/header-bug`)
   - Special branches: `master`, `main`, `develop`, `staging`, `production`

2. **Custom commands** - Runs commands defined in `.dev-hooks.yml` before pushing

## Configuration File

Create a `.dev-hooks.yml` file in your project root to configure custom pre-push commands.

Copy the example file to get started:

```bash
cp .dev-hooks.example.yml .dev-hooks.yml
```

### Example Configuration

```yaml
# Pre-push commands
pre-push:
  enabled: true
  skip_branch_validation: false

  commands:
    - name: "Run Tests"
      run: "pytest"

    - name: "Lint Check"
      run: "ruff check src/"

    - name: "Type Check"
      run: "mypy src/"

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
  container: "php"

pre-push:
  commands:
    - name: "PHPUnit"
      run: "vendor/bin/phpunit"
```

Commands will be executed inside the container:
```bash
docker-compose exec -T php vendor/bin/phpunit
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

MIT
