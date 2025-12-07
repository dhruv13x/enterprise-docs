<div align="center">
  <img src="https://raw.githubusercontent.com/dhruv13x/enterprise-docs/main/enterprise-docs_logo.png" alt="enterprise-docs logo" width="200"/>
</div>

<div align="center">

# 🧱 Enterprise Docs

**Unified enterprise documentation suite for Dhruv13x organization — providing policy, compliance, and automation templates for enterprise-grade Python projects.**

<!-- Package Info -->
[![PyPI version](https://img.shields.io/pypi/v/enterprise-docs.svg)](https://pypi.org/project/enterprise-docs/)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
![Wheel](https://img.shields.io/pypi/wheel/enterprise-docs.svg)
[![Release](https://img.shields.io/badge/release-PyPI-blue)](https://pypi.org/project/enterprise-docs/)

<!-- Build & Quality -->
[![Build status](https://github.com/dhruv13x/enterprise-docs/actions/workflows/publish.yml/badge.svg)](https://github.com/dhruv13x/enterprise-docs/actions/workflows/publish.yml)
[![Codecov](https://codecov.io/gh/dhruv13x/enterprise-docs/graph/badge.svg)](https://codecov.io/gh/dhruv13x/enterprise-docs)
[![Test Coverage](https://img.shields.io/badge/coverage-90%25%2B-brightgreen.svg)](https://github.com/dhruv13x/enterprise-docs/actions/workflows/test.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/badge/linting-ruff-yellow.svg)](https://github.com/astral-sh/ruff)
![Security](https://img.shields.io/badge/security-CodeQL-blue.svg)

<!-- Usage -->
![Downloads](https://img.shields.io/pypi/dm/enterprise-docs.svg)
![OS](https://img.shields.io/badge/os-Linux%20%7C%20macOS%20%7C%20Windows-blue.svg)
[![Python Versions](https://img.shields.io/pypi/pyversions/enterprise-docs.svg)](https://pypi.org/project/enterprise-docs/)

<!-- License -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

## ⚡ Quick Start

Get your documentation up to enterprise standards in less than 5 minutes.

### Prerequisites
-   **Python 3.10** or higher
-   `pip` or `poetry`

### Installation
```bash
pip install enterprise-docs
```

### Run
To immediately see what templates are available:
```bash
enterprise-docs list
```

### Demo
Set up your security and governance policies with a single command:
```bash
# Sync critical templates to your ./docs folder
enterprise-docs sync SECURITY.md --to ./docs
enterprise-docs sync GOVERNANCE.md --to ./docs

# Or sync the entire suite
enterprise-docs sync --to ./docs
```

---

## ✨ Features

**enterprise-docs** is more than just a template collection; it's a compliance engine.

-   **Core Documentation**: Over 30+ industry-standard templates including `SECURITY.md`, `GOVERNANCE.md`, `CHANGELOG.md`, and `CONTRIBUTING.md`.
-   **Automated Sync**: Keep your documentation standardized across hundreds of repositories with a single CLI command.
-   **Custom Sources**: Point the tool to your own local template directory to enforce your organization's specific standards.
-   **CI/CD Ready**: Designed to integrate into your build pipelines to ensure documentation presence and freshness.
-   **Extensible Architecture**: Built with a plugin-ready structure to easily add new template types or validation logic.

---

## 🛠️ Configuration

The tool works out-of-the-box with sensible defaults, but can be customized via CLI arguments.

### CLI Arguments

| Command | Argument | Default | Description |
| :--- | :--- | :--- | :--- |
| `list` | N/A | N/A | Lists all available documentation templates in the library. |
| `sync` | `template_name` | All | Specific template file to sync (e.g., `SECURITY.md`). If omitted, syncs all. |
| `sync` | `--to` | `./docs` | Destination directory where files will be copied. Created if it doesn't exist. |
| `sync` | `--source` | Internal | Path to a custom directory containing your own markdown templates. |
| `version`| N/A | N/A | Displays the current installed version of `enterprise-docs`. |

### Environment Variables
Currently, `enterprise-docs` relies primarily on CLI arguments for configuration. Future versions may support `ENTERPRISE_DOCS_HOME` for global configuration.

---

## 🏗️ Architecture

The project follows a clean `src` layout with `rich` for terminal output and `setuptools_scm` for versioning.

### Directory Tree
```text
src
├── __init__.py
└── enterprise_docs
    ├── __init__.py
    ├── banner.py           # Logo and banner rendering
    ├── cli.py              # Main CLI entry point (argparse logic)
    └── templates           # The "Gold Standard" template library
        ├── ARCHITECTURE.md
        ├── SECURITY.md
        ├── GOVERNANCE.md
        ├── ... (40+ files)
        └── default_pyproject.toml
```

### Data Flow
1.  **User invokes CLI**: `enterprise-docs sync --to ./docs`
2.  **CLI Parsing**: `cli.py` detects the `sync` command and optional arguments.
3.  **Resource Loading**: The tool identifies the source of templates (internal `importlib.resources` or external `--source`).
4.  **Execution**: Files are filtered (if a specific name is requested) and copied to the target directory.
5.  **Feedback**: Success or error messages are printed to the console using standard output.

---

## 🐞 Troubleshooting

| Error Message | Possible Cause | Solution |
| :--- | :--- | :--- |
| `❌ Template 'X' not found` | Typo in template name or template does not exist. | Run `enterprise-docs list` to see valid names. Check spelling carefully. |
| `❌ Source directory 'X' not found` | The path provided to `--source` does not exist. | Verify the path is absolute or correctly relative to your current working directory. |
| `ModuleNotFoundError` | Package not installed in the current environment. | Ensure you are in the correct virtual environment and run `pip install .` |

### Debug Mode
If you encounter unexpected behavior, ensure you are running the latest version:
```bash
enterprise-docs version
```
Issues can be reported on our [GitHub Issues](https://github.com/dhruv13x/enterprise-docs/issues) page.

---

## 🤝 Contributing

We welcome contributions to expand the template library or improve the CLI!

1.  **Fork** the repository.
2.  **Clone** your fork locally.
3.  **Install** dependencies: `pip install -e ".[dev]"`
4.  **Run Tests**: `pytest`
5.  **Submit** a Pull Request.

Please review the `CONTRIBUTING.md` file (available via `enterprise-docs sync CONTRIBUTING.md`) for detailed guidelines.

---

## 🗺️ Roadmap

We have exciting plans for the future of `enterprise-docs`. Check out our [ROADMAP.md](ROADMAP.md) for details on upcoming features like:
-   Template variable substitution (Jinja2 support).
-   Interactive setup wizard (`init` command).
-   Validation checks for existing documentation.

---

<div align="center">
  <sub>Built with ❤️ by <a href="https://github.com/dhruv13x">Dhruv13x</a></sub>
</div>
