# InfraGuard

**InfraGuard** is a lightweight, cross-platform infrastructure auditing CLI built with Python. It helps system administrators and infrastructure engineers quickly inspect essential system information and resource utilization directly from their terminals.

InfraGuard provides structured audit reports with support for terminal, JSON, and Markdown output.

## Features

- Hostname identification
- Operating system and platform detection
- CPU utilization monitoring
- Memory utilization monitoring
- Disk usage monitoring across mounted filesystems
- Formatted terminal audit reports
- JSON output for automation and integrations
- Markdown output for documentation and reporting
- Cross-platform support

## Requirements

- Python 3.10 or later
- Git
- pipx (recommended for installation)

## Installation

InfraGuard uses **pipx** for installation. pipx installs Python CLI applications in isolated virtual environments and makes their commands available globally without requiring manual environment activation.

### Linux (Ubuntu/Debian)

**1. Install the prerequisites**

```bash
sudo apt update
sudo apt install -y git python3 python3-pip pipx
```

Ensure Python 3.10 or later is installed.

**2. Configure pipx**

```bash
pipx ensurepath
```

Reload your shell:

```bash
source ~/.bashrc
```

If you use another shell, restart it or reload its configuration.

**3. Install InfraGuard**

```bash
pipx install git+https://github.com/samuelshow1234/infraguard.git
```

**4. Run InfraGuard**

```bash
infraguard
```

No virtual environment activation is required.

### Oracle Linux / RHEL

**1. Install Python and Git**

Install Python 3.10 or later and Git using your distribution's supported package repositories.

For example, on Oracle Linux 9 with Python 3.12 available:

```bash
sudo dnf install -y python3.12 python3.12-pip git
```

**2. Install pipx**

```bash
python3.12 -m pip install --user pipx
```

If your distribution provides pipx through its package repositories, you can install it using the system package manager instead.

**3. Add pipx to your PATH**

```bash
python3.12 -m pipx ensurepath
```

Reload your shell:

```bash
source ~/.bashrc
```

**4. Install InfraGuard**

```bash
pipx install git+https://github.com/samuelshow1234/infraguard.git
```

**5. Run InfraGuard**

```bash
infraguard
```

### Windows (PowerShell)

**1. Install Python 3.10 or later and Git.**

**2. Install pipx**

```powershell
py -m pip install --user pipx
```

**3. Configure pipx**

```powershell
py -m pipx ensurepath
```

Restart PowerShell so the PATH changes take effect.

**4. Install InfraGuard**

```powershell
pipx install git+https://github.com/samuelshow1234/infraguard.git
```

**5. Run InfraGuard**

```powershell
infraguard
```

### Windows Subsystem for Linux (WSL)

WSL users can follow the Linux installation instructions from their WSL terminal.

## Usage

Once installed, InfraGuard can be executed directly from any terminal.

**Run a standard infrastructure audit:**

```bash
infraguard
```

**Generate JSON output:**

```bash
infraguard --format json
```

**Generate Markdown output:**

```bash
infraguard --format markdown
```

## Updating InfraGuard

To upgrade to the latest version from GitHub:

```bash
pipx upgrade infraguard
```

## Uninstallation

To uninstall InfraGuard:

```bash
pipx uninstall infraguard
```

## Development Installation

Contributions are welcome!

Developers who want to modify InfraGuard or run its tests can clone the repository and install it in editable mode.

**1. Clone the repository**

```bash
git clone https://github.com/samuelshow1234/infraguard.git
cd infraguard
```

**2. Create a virtual environment**

Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**3. Install development dependencies**

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

**4. Run tests**

```bash
pytest -v
```

**5. Run code quality checks**

```bash
ruff check .
```

**6. Format the source code**

```bash
ruff format .
```

## Dependencies

InfraGuard manages its application dependencies through `pyproject.toml`.

| Package | Purpose |
|---|---|
| Python | Runtime |
| Typer | Command-line interface |
| Rich | Terminal output and formatting |
| psutil | System and resource monitoring |
| pytest | Automated testing |
| Ruff | Linting and code formatting |

Development dependencies are installed separately using the `.[dev]` option.

## Contributing

Contributions, bug reports, feature requests, and suggestions are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Run the tests and code quality checks.
5. Submit a pull request.

## License
InfraGuard is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.
