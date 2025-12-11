# Contributing

Thanks for your interest in contributing!

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/dev-tools-hooks.git
   cd dev-tools-hooks
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install in development mode:
   ```bash
   pip install -e .
   ```

## Code Style

- Follow PEP 8 guidelines
- Use type hints where possible
- Keep functions focused and small

## Submitting Changes

1. Create a new branch: `git checkout -b feat/your-feature`
2. Make your changes
3. Test locally: `dev-hooks install && dev-hooks list`
4. Commit using conventional commits: `feat: add new feature`
5. Push and create a Pull Request

## Adding New Hooks

1. Create your hook script in `hooks/`
2. Copy it to `src/dev_tools_hooks/hooks/`
3. Add the hook name to `AVAILABLE_HOOKS` in `installer.py`
4. Update the `cmd_list` function in `cli.py` with a description
