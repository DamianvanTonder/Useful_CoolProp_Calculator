# _Requirements_

## _System Requirements_
### _Operating System_
- Windows 7 or later
- macOS 10.12 or later
- Linux (any modern distribution)

### _Python Version_
- Python 3.7 or higher (recommended: Python 3.9+)

## _Dependencies_
### _Required Python Packages_
Install all dependencies using:
```bash
pip install -r requirements.txt
```

#### _Core Dependencies_
- CoolProp (>=6.4.1)
  - Thermophysical property library
  - Installation: `pip install CoolProp`

#### _Standard Library Modules_
The following are included with Python (no installation needed):
- `json` - For exporting calculation history
- `csv` - For CSV export functionality
- `datetime` - For timestamping calculations
- `typing` - For type hints
- `sys` - For command-line arguments

## _Installation Instructions_
### _Step 1: Install Python_
Download and install Python from [python.org](https://www.python.org/downloads/)
Verify installation:
```bash
python --version
```

### _Step 2: Create Virtual Environment (Recommended)_
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### _Step 3: Install Dependencies_
```bash
pip install --upgrade pip
pip install CoolProp
```

## _requirements.txt File_
```
CoolProp>=6.4.1
```

## _Troubleshooting_
### _CoolProp Installation Issues_
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

### _Import Errors_
If you encounter `ModuleNotFoundError: No module named 'CoolProp'`:
1. Ensure you're in the correct virtual environment
2. Reinstall CoolProp: `pip install --force-reinstall CoolProp`
3. Check Python version: `python --version` (must be 3.7+)

## _Optional Dependencies_
For enhanced functionality, you may want to install:
- numpy - For numerical array operations (if extending the calculator)
- matplotlib - For plotting property diagrams (future feature)
- pandas - For advanced data table manipulation

```bash
pip install numpy matplotlib pandas
```

## _Hardware Requirements_
- RAM: Minimum 512 MB (1 GB recommended)
- Disk Space: Approximately 50 MB for installation
- Processor: Any modern CPU (no special requirements)

## _Verification_
Test your installation:
```bash
python -c "import CoolProp; print(CoolProp.__version__)"
```

Expected output: Version number (e.g., `6.4.1` or higher)

## Additional Resources
- [CoolProp Official Documentation](http://www.coolprop.org/)
- [CoolProp GitHub Repository](https://github.com/CoolProp/CoolProp)
- [Python Package Index - CoolProp](https://pypi.org/project/CoolProp/)
