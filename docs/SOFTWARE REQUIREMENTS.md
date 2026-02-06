# Requirements

## System Requirements
### Operating System
- Windows 7 or later
- macOS 10.12 or later
- Linux (any modern distribution)

### Python Version
- Python 3.7 or higher (recommended: Python 3.9+)

## Dependencies
### Required Python Packages
Install all dependencies using:
```bash
pip install -r requirements.txt
```

#### Core Dependencies
- CoolProp (>=6.4.1)
  - Thermophysical property library
  - Installation: `pip install CoolProp`

#### Standard Library Modules
The following are included with Python (no installation needed):
- `json` - For exporting calculation history
- `csv` - For CSV export functionality
- `datetime` - For timestamping calculations
- `typing` - For type hints
- `sys` - For command-line arguments

## Installation Instructions
### Step 1: Install Python
Download and install Python from [python.org](https://www.python.org/downloads/)
Verify installation:
```bash
python --version
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install --upgrade pip
pip install CoolProp
```

## requirements.txt File
```
CoolProp>=6.4.1
```

## Troubleshooting
### CoolProp Installation Issues
Windows:
```bash
pip install --upgrade pip setuptools wheel
pip install CoolProp
```

Linux (compilation issues):
```bash
sudo apt-get install python3-dev build-essential
pip install CoolProp
```

macOS (M1/M2 chips):
```bash
arch -arm64 pip install CoolProp
```

### Import Errors
If you encounter `ModuleNotFoundError: No module named 'CoolProp'`:
1. Ensure you're in the correct virtual environment
2. Reinstall CoolProp: `pip install --force-reinstall CoolProp`
3. Check Python version: `python --version` (must be 3.7+)

## Optional Dependencies
For enhanced functionality, you may want to install:
- numpy - For numerical array operations (if extending the calculator)
- matplotlib - For plotting property diagrams (future feature)
- pandas - For advanced data table manipulation

```bash
pip install numpy matplotlib pandas
```

## Hardware Requirements
- RAM: Minimum 512 MB (1 GB recommended)
- Disk Space: Approximately 50 MB for installation
- Processor: Any modern CPU (no special requirements)

## Verification
Test your installation:
```bash
python -c "import CoolProp; print(CoolProp.__version__)"
```

Expected output: Version number (e.g., `6.4.1` or higher)

## Additional Resources
- [CoolProp Official Documentation](http://www.coolprop.org/)
- [CoolProp GitHub Repository](https://github.com/CoolProp/CoolProp)
- [Python Package Index - CoolProp](https://pypi.org/project/CoolProp/)
