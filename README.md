# _CoolProp Calculator_
A comprehensive Python tool for thermophysical property calculations with an interactive command-line interface. Calculate properties for water, refrigerants, gases, and other fluids using the CoolProp library with high precision output.

## _Features_
- Single Property Calculations - Calculate any thermophysical property given two state variables with 12 decimal place precision
- Complete State Analysis - Get all properties at once for a given state point
- Critical & Triple Point Data - Access critical and triple point properties for substances
- Batch Processing - Process multiple calculations simultaneously
- Property Tables - Generate tables across temperature and pressure ranges with CSV export
- Interactive CLI - User-friendly command-line interface with guided inputs
- 100+ Substances - Comprehensive library of refrigerants, hydrocarbons, alcohols, and more

## _Supported Properties_
- Temperature, Pressure, Density
- Enthalpy, Entropy, Internal Energy
- Specific Heat (Cp, Cv)
- Viscosity, Thermal Conductivity
- Speed of Sound, Prandtl Number
- Surface Tension, Quality (vapor fraction)
- And more...

## _Supported Substances_
100+ substances including:
- Pure Fluids: Water, Air, Nitrogen, Oxygen, Hydrogen, Helium, Argon, and noble gases
- Hydrocarbons: Methane through Decane, Ethylene, Propylene, Acetone
- HFC Refrigerants: R134a, R32, R125, R143a, R152a, R227ea, R245fa
- HFO Refrigerants: R1234yf, R1234ze(E), R1233zd(E), R1336mzz(Z)
- Refrigerant Blends: R404A, R407C, R410A, R507A, R448A, R449A, R450A, R452A, R513A
- Natural Refrigerants: Ammonia, CO2, Propane, Isobutane
- Alcohols: Methanol, Ethanol, Propanol, IsoButanol
- Aromatics: Benzene, Toluene, Xylene, EthylBenzene
- Siloxanes: D4, D5, D6, MD2M, MD3M, MD4M
- Heat Transfer Fluids: HFE series, Novec649
- Cryogenic Fluids: ParaHydrogen, OrthoHydrogen, Deuterium

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

print(f"Density: {result['output_value']:.12e} kg/m³")
# Output: Density: 9.965326583930e+02 kg/m³
```

## _Menu Options_
```
[1] Single Property Calculation
[2] All Properties at State Point
[3] Critical Properties
[4] Triple Point Properties
[5] Batch Calculations
[6] Property Table Generator
[7] List Available Substances
[8] Property Reference Guide
[0] Exit
```

## _High Precision Output_
All calculations provide high-precision results:
- 12 decimal places in scientific notation for most properties
- 10 decimal places for temperatures and densities
- Perfect for engineering calculations and research

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
