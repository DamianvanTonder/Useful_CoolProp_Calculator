# _CoolProp Calculator_
A comprehensive Python tool for thermophysical property calculations with an interactive command-line interface. Calculate properties for water, refrigerants, gases, and other fluids using the CoolProp library.

## _Features_
- Single Property Calculations - Calculate any thermophysical property given two state variables
- Complete State Analysis - Get all properties at once for a given state point
- Critical & Triple Point Data - Access critical and triple point properties for substances
- Batch Processing - Process multiple calculations simultaneously
- Calculation History - Track and export your calculations (JSON/CSV)
- Property Tables - Generate tables across temperature and pressure ranges
- Interactive CLI - User-friendly command-line interface with guided inputs

## _Supported Properties_
- Temperature, Pressure, Density
- Enthalpy, Entropy, Internal Energy
- Specific Heat (Cp, Cv)
- Viscosity, Thermal Conductivity
- Speed of Sound, Prandtl Number
- Surface Tension, Quality (vapor fraction)
- And more...

## _Supported Substances_
Water, Air, Nitrogen, Oxygen, Hydrogen, Helium, Ammonia, Carbon Dioxide, Methane, Ethane, Propane, Butane, R134a, R410A, R404A, R407C, R32, R1234yf, Argon, Ethanol, Methanol, Toluene, Benzene, and many more.

## _Installation_
```bash
# Clone the repository
git clone https://github.com/yourusername/coolprop-calculator.git
cd coolprop-calculator

# Install dependencies
pip install -r requirements.txt
```

## _Quick Start_
```bash
# Run the interactive calculator
python coolprop_calculator.py

# Run in simple mode
python coolprop_calculator.py --simple
```

## _Usage Example_
```python
from coolprop_calculator import CoolPropCalculator

calc = CoolPropCalculator()

# Calculate density of water at 300K and 101325 Pa
result = calc.calculate_property(
    output_prop='D',
    input1_prop='T',
    input1_value=300,
    input2_prop='P',
    input2_value=101325,
    substance='Water'
)

print(f"Density: {result['output_value']:.2f} kg/m³")
```

## _Documentation_
- [User Guide](USER_GUIDE.md) - Detailed usage instructions
- [Requirements](REQUIREMENTS.md) - System requirements and dependencies
- [CoolProp Documentation](http://www.coolprop.org/) - Official CoolProp docs

## _Contributing_
Contributions are welcome! Please feel free to submit a Pull Request.

## _License_
This project is licensed under the MIT License - see the LICENSE file for details.

## _Acknowledgments_
- Built with [CoolProp](http://www.coolprop.org/) - Open-source thermophysical property library
- Designed for engineers, researchers, and students in thermodynamics and fluid mechanics
