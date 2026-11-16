## Installation

InfraGuard requires Python 3.10 or later and Git.

### Linux (Ubuntu/Debian)

**1. Install the prerequisites**

```bash
sudo apt update
sudo apt install -y git python3 python3-venv python3-pip
```

**2. Clone the repository**

```bash
git clone https://github.com/samuelshow1234/infraguard.git
cd infraguard
```

**3. Create a virtual environment**

```bash
python3 -m venv .venv
```

**4. Activate the virtual environment**

```bash
source .venv/bin/activate
```

**5. Install InfraGuard**

```bash
python -m pip install --upgrade pip
pip install .
```

Pip automatically installs the required dependencies, including Typer, Rich and psutil.

**6. Run InfraGuard**

```bash
infraguard
```

### Windows (PowerShell)

**1. Install Python 3.10+ and Git.**

**2. Clone the repository**

```powershell
git clone https://github.com/samuelshow1234/infraguard.git
cd infraguard
```

**3. Create a virtual environment**

```powershell
py -3 -m venv .venv
```

**4. Activate the environment**

```powershell
.\.venv\Scripts\Activate.ps1
```

**5. Install InfraGuard**

```powershell
python -m pip install --upgrade pip
pip install .
```

**6. Run InfraGuard**

```powershell
infraguard
```

If PowerShell execution policies prevent environment activation, you can use the virtual environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install .
.\.venv\Scripts\python.exe -m infraguard.cli
```

### Windows Subsystem for Linux (WSL)

WSL users can follow the Linux installation instructions from their WSL terminal.

```bash
sudo apt update
sudo apt install -y git python3 python3-venv python3-pip

git clone https://github.com/samuelshow1234/infraguard.git
cd infraguard

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
pip install .

infraguard
```

### Usage

Run a standard infrastructure audit:

```bash
infraguard
```

Generate JSON output:

```bash
infraguard --format json
```

Generate Markdown output:

```bash
infraguard --format markdown
```

### Development Installation

Contributors who want to modify InfraGuard or run its tests should install the development dependencies:

```bash
pip install -e ".[dev]"
```

Run tests:

```bash
pytest -v
```

Run code quality checks:

```bash
ruff check .
```

Format the source code:

```bash
ruff format .
```

## Dependencies

InfraGuard manages its Python dependencies through `pyproject.toml`.

| Package | Purpose |
|---|---|
| Python | Runtime |
| Typer | Command-line interface |
| Rich | Terminal output and formatting |
| psutil | System and resource monitoring |
| pytest | Automated testing |
| Ruff | Linting and code formatting |

The development dependencies are installed separately using the `.[dev]` option.
